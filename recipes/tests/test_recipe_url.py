from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_home(self):
        """Recipe Home"""
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_category(self):
        """Recipe category"""
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')


    def test_recipe(self):
        """Recipe details"""
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

