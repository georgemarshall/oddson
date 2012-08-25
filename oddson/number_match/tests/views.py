from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewsTestCase(TestCase):
    fixtures = ['test_number_match.json']
    urls = 'number_match.tests.urls'

    def test_view_resources(self):
        url = reverse('number_match:index')

        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_view_game_list(self):
        url = reverse('number_match:list')

        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_view_game_detail(self):
        url = reverse('number_match:detail', kwargs={'id': 1})

        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

    def test_view_attempt_list(self):
        url = reverse('number_match:attempt_list', kwargs={'game_id': 1})

        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)

        # No POST data
        r = self.client.post(url)
        self.assertEqual(r.status_code, 400)

        # Invalid POST data
        r = self.client.post(url, {'number': 'two'})
        self.assertEqual(r.status_code, 400)

        # Valid POST data
        r = self.client.post(url, {'number': 1})
        self.assertEqual(r.status_code, 201)

        # Out of range number
        r = self.client.post(url, {'number': 100})
        self.assertEqual(r.status_code, 400)

    def test_view_attempt_detail(self):
        url = reverse('number_match:attempt_detail', kwargs={'game_id': 1, 'id': 1})

        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
