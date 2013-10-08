"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Note

class NotesViewsTestCase(TestCase):
	fixtures = ['notes_views_testdata.json']	

	def test_index(self):
		resp = self.client.get('/notes/list/')
		self.assertEqual(resp.status_code, 200)
