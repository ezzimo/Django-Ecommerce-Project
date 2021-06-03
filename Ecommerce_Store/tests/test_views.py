from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls.base import reverse

from Ecommerce_Store.models import Category, Product
from Ecommerce_Store.views import product_all


@skip("demonstration of skipping test")
class TaskSkip(TestCase):
    def test_skip_exeple(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='cloths', slug='cloths')
        Product.objects.create(category_id=1, title='Chemise Bleu', created_by_id=1, slug='Chemise-Bleu', price='19.99', image='chemise')

    def test_url_allowed_hosts(self):
        """
        Test hosts allowed to use this web-application
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='mydomain.com')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/', HTTP_HOST='mydomaine.com')
        self.assertEqual(response.status_code, 400)

    def test_product_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('ecommerce_store:category_list', args=['cloths']))
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
        """
        Code validation, search HTML for text
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>  Store  </title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
