from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls.base import reverse

from Ecommerce_Store.models import Category, Product
from Ecommerce_Store.views import all_products


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='cloths', slug='cloths')
        Product.objects.create(category_id=1, title='Chemise Bleu', created_by_id=1, slug='Chemise-Bleu', price='19.99', image='chemise')

    def test_url_allowed_hosts(self):
        """
        Test hosts allowed
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test the statut response of a Product request
        """
        response = self.c.get(reverse('ecommerce_store:product_detail', args=['Chemise-Bleu']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test the statut response of a category request
        """
        response = self.c.get(reverse('ecommerce_store:category_list', args=['cloths']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn('<title>  Home  </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('product/Chemise-Bleu')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>  Home  </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
