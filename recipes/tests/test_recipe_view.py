from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
# Create your tests here.

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

    def test_recipe_view_response(self):
        """check view status code"""
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view(self):
        """check crrect template"""
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_show_recipe(self):
        """check if is any recipe"""
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Não foram encontradas receitas :(', response.content.decode('utf-8'))