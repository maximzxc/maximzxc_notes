"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from django_webtest import WebTest
from models import Note


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
        assert note1.title in page
        assert note2.title in page
        assert note1.content in page
        assert note2.content in page
