"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django_webtest import WebTest
from notessite.apps.Notes.models import Note, Book
from django.template import Context, Template
from django.core.files import File


class NotesViewsTestCase(TestCase):
    fixtures = ['notes_views_testdata.json']

    def test_index(self):
        resp = self.client.get(reverse('notes_list'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)


class NotesListsTest(WebTest):
    fixtures = ['notes_views_testdata.json']

    def test_search_form(self):
        search = self.app.get(reverse('search_form'))
        self.assertTrue('Search' in search)
        form = search.forms[0]
        form['id'] = 'c'
        k = form.submit().follow()
        self.assertTrue('Please submit a search term with integer.' in k)
        form = search.forms[0]
        form['id'] = ''
        k = form.submit().follow()
        self.assertTrue('Please submit a search term.' in k)
        form = search.forms[0]
        form['id'] = 1
        k = form.submit().follow()
        note = Note.objects.get(pk=1)
        self.assertTrue(note.title in k)

    def test_list(self):
        note1 = Note.objects.latest('updated')
        page = self.app.get(reverse('notes_list'))
        self.assertTrue(note1.title in page)
        self.assertTrue(note1.content in page)
        #test symbols counter
        text_counter = 'You have ' + str(Note.objects.count()) + ' notes'
        self.assertTrue(text_counter in page)

    def test_forms(self):
        send = {'title': 'example', 'content': 'exampleqwe123', 'image':
                File(open('notessite/templates/media/img/UAbbmEdI4Z8.jpg'))}
        self.client.post(reverse('add'), send,
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        note = Note.objects.latest('updated')
        self.assertEqual(note.title, 'example')
        self.assertEqual(note.content, 'exampleqwe123')
        c = Note.objects.count()
        self.client.get(reverse('add'), send,
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(Note.objects.count(), c)
        #test if content < 10 characters
        c = Note.objects.count()
        send = {'title': 'example', 'content': 'example', 'image':
                File(open('notessite/templates/media/img/UAbbmEdI4Z8.jpg'))}
        self.client.post(reverse('add'), send,
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(Note.objects.count(), c)

    def test_random_note(self):
        page = self.client.get(reverse('insert'))
        self.assertEqual(page.status_code, 200)


class TagTests(TestCase):
    fixtures = ['notes_views_testdata.json']

    def testTags(self):
        note = Note.objects.get(pk=1)
        t = Template('{% load render_notes%}{% search id %}')
        c = Context({"id": 1111111})
        self.assertTrue("Note doesn't exist ;(" in t.render(c))
        c = Context({"id": 1})
        self.assertTrue(note.title in t.render(c))


class ModelTest(TestCase):
    fixtures = ['books_views_testdata.json']

    def testBooks(self):
        note1 = Note.objects.get(pk=2)
        note2 = Note.objects.get(pk=1)
        book = Book.objects.get(pk=1)
        book.notes.add(note1)
        book.notes.add(note2)
        self.assertTrue(note1 in book.notes.all())
        self.assertTrue(note2 in book.notes.all())
