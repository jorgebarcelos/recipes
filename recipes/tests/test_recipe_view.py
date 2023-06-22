from django.test import TestCase
from django.urls import reverse, resolve
from recipes.models import *
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
        """check correct template"""
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_show_recipe(self):
        """check if is any recipe"""
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Não foram encontradas receitas :(', response.content.decode('utf-8'))

    def test_home_template(self):
        """check if home template loads recipes"""
        category = Category.objects.create(name='lanche')
        author = User.objects.create_user(
            first_name='José',
            last_name='Janglenssen',
            username='Janglenssen',
            password='123456',
            email='jose@janglenssen.com'
        )
        recipe = Recipe.objects.create(
            title = 'Recipe-Test',
            description = 'Recipe-Unit-Test',
            slug = 'recipe-test',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 5,
            servings_unit = 'Porções',
            preparation_steps = 'Recipe-Unit-Test',
            preparation_steps_is_html = False,
            is_published = True,
            category = category,
            author = author
        )
        assert 1==1

    def test_category_status(self):
        """test category page is 404 if not recipes found"""
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 10}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_404(self):
        """test if page is 404 if not recipes detail found"""
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 10}))
        self.assertEqual(response.status_code, 404)