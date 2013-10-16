"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django_webtest import WebTest
from notessite.apps.Notes.models import Note
from django.template import Context, Template


class NotesViewsTestCase(TestCase):
    fixtures = ['notes_views_testdata.json']

    def test_index(self):
        resp = self.client.get(reverse('notes_list'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)


class ListsTest(WebTest):
    fixtures = ['notes_views_testdata.json']

    def test_list(self):
        note1 = Note.objects.get(pk=1)
        note2 = Note.objects.get(pk=2)
        page = self.app.get(reverse('notes_list'))
        self.assertTrue(note1.title in page)
        self.assertTrue(note2.title in page)
        self.assertTrue(note1.content in page)
        self.assertTrue(note2.content in page)

    def test_forms(self):
        page = self.app.get(reverse('add'))
        form = page.click(u'Add', index= 0).form
        form['title'] = 'example'
        form['content'] = 'exampleqwe123'
        form.submit()
        note = Note.objects.get(pk=3)
        self.assertEqual(note.title, 'example')
        self.assertEqual(note.content, 'exampleqwe123')
        #test if content < 10 characters
        form['title'] = 'example'
        form['content'] = 'examp1'
        form.submit()
        self.assertTrue(Note.objects.all().count, 3)


class TagTests(TestCase):
    fixtures = ['notes_views_testdata.json']

    def testTags(self):
        note = Note.objects.get(pk=1)
        t = Template('{% load render_notes%}{% search id %}')
        c = Context({"id": 1111111})
        self.assertTrue("Note doesn't exist ;(" in t.render(c))
        c = Context({"id": 1})
        self.assertTrue(note.title in t.render(c))
