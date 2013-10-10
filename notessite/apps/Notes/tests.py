"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse


class NotesViewsTestCase(TestCase):
    fixtures = ['notes_views_testdata.json']

    def test_index(self):
        resp = self.client.get(reverse('notes_list'))
        self.assertEqual(resp.status_code, 200)
        resp1 = self.client.get(reverse('home'))
        self.assertEqual(resp1.status_code, 200)
