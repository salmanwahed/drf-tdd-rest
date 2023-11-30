from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from .models import Toy
# Create your tests here.

class ToyModelTest(TestCase):
    def setUp(self) -> None:
        # Create a Toy instance for testing
        self.toy = Toy.objects.create(name='Test Toy', description='A test toy.')

    def test_create_toy(self):
        url = reverse('toy-detail', kwargs={'id': self.toy.id})
        rsp = self.client.get(url)

        self.assertEqual(rsp.status_code, status.HTTP_200_OK)
        self.assertEqual(rsp.data['id'], self.toy.id)
        self.assertEqual(rsp.data['name'], self.toy.name)

    def test_update_toy(self):
        url = reverse('toy-detail', kwargs={'id': self.toy.id})
        data = {'description': 'Updated Toy Description'}
        rsp = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(rsp.status_code, status.HTTP_200_OK)
        self.assertEqual(rsp.data['id'], self.toy.id)
        self.assertEqual(rsp.data['description'], data.get('description'))

    def test_delete_toy(self):
        url = reverse('toy-detail', kwargs={'id': self.toy.id})
        rsp = self.client.delete(url, content_type='application/json')
        self.assertEqual(rsp.status_code, status.HTTP_204_NO_CONTENT)