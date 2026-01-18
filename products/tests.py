from django.test import TestCase
from django.urls import reverse

from products.models import Product

# Create your tests here.

class ShowProductsTests(TestCase):
    def test_should_return_200(self):
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
    def test_should_return_200(self):
        url = reverse('products_list')
        Product.objects.create(
            name='test',
            description='test description',
            price='3',
            stock='5.5' ,         
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['products'].count(),1)