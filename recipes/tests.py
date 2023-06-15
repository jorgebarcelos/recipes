from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
# Create your tests here.

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


class RecipeViewTest(TestCase):
    def test_home_view(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    def test_category_view(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
