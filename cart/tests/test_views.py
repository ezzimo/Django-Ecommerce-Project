from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from Ecommerce_Store.models import Category, Product


class TestCartView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='cloths', slug='cloths')
        Product.objects.create(category_id=1, title='Chemise Bleu', created_by_id=1, slug='Chemise-Bleu', price='10.00', image='chemise')
        Product.objects.create(category_id=1, title='Chemise Rouge', created_by_id=1, slug='Chemise-Bleu', price='10.00', image='chemise')
        Product.objects.create(category_id=1, title='Chemise Vert', created_by_id=1, slug='Chemise-Bleu', price='10.00', image='chemise')
        self.client.post(
            reverse('cart:cart_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('cart:cart_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_cart_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('cart:cart_summary'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """
        Test adding product to the Cart
        """
        response = self.client.post(
            reverse('cart:cart_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('cart:cart_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_cart_delete(self):
        """
        Test deletion of product from cart
        """
        response = self.client.post(
            reverse('cart:cart_delete'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'Success': True, 'qty': 1, 'total': '10.00'})

    def test_cart_update(self):
        """
        Test updating of product in the cart
        """
        response = self.client.post(
            reverse('cart:cart_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'Success': True, 'qty': 2, 'subtotal': '10.00', 'total': '20.00'})
