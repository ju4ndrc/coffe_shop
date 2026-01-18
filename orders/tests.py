from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class MyOrderViewTests(TestCase):
    def test_no_logged_user(self):
        url = reverse('my_order')
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.url,'/users/login?next=/orders/my_order')
