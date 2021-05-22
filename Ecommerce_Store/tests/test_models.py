from django.contrib.auth.models import User
from django.test import TestCase

from Ecommerce_Store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Habilles', slug='Habilles')

    def test_category_model_entry(self):
        """
        Test Category model insertion/types/field attriutes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_return(self):
        """
        Test Category model return name
        """
        data = self.data1
        self.assertEqual(str(data), 'Habilles')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='Habilles', slug='Habilles')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Chemise Bleu', created_by_id=1, slug='Chemise-Bleu', price='19.99', image='chemise')

    def test_product_model_entry(self):
        """
        Test Product model insertion/types/field attriutes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Chemise Bleu')
