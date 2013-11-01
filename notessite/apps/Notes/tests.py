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
        note1 = Note.objects.latest('updated')
        page = self.app.get(reverse('notes_list'))
        self.assertTrue(note1.title in page)
        self.assertTrue(note1.content in page)
        #test symbols counter
        text_counter = 'You have ' + str(Note.objects.count()) + ' notes'
        self.assertTrue(text_counter in page)

    def test_forms(self):
        c = Note.objects.count()
        send = {'title': 'example', 'content': 'exampleqwe123'}
        resp = self.client.post(reverse('add'), send,
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertContains(resp, 'Note was added')
        self.assertEqual(Note.objects.count(), c+1)
        note = Note.objects.latest('updated')
        self.assertEqual(note.title, 'example')
        self.assertEqual(note.content, 'exampleqwe123')
        c = Note.objects.count()
        self.client.get(reverse('add'), send,
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(Note.objects.count(), c)
        #test if content < 10 characters
        c = Note.objects.count()
        send = {'title': 'example', 'content': 'example'}
        resp = self.client.post(reverse('add'), send,
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertNotContains(resp, 'Note was added')
        self.assertEqual(Note.objects.count(), c)


class TagTests(TestCase):
    fixtures = ['notes_views_testdata.json']

    def testTags(self):
        note = Note.objects.get(pk=1)
        t = Template('{% load render_notes%}{% search id %}')
        c = Context({"id": 1111111})
        self.assertTrue("Note doesn't exist ;(" in t.render(c))
        c = Context({"id": 1})
        self.assertTrue(note.title in t.render(c))
