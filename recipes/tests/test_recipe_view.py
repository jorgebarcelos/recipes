from django.urls import reverse, resolve
from recipes.models import *
from recipes import views
from .test_recipe_base import RecipeTestBase
# Create your tests here.


class RecipeViewTest(RecipeTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

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
        """check if is no recipes in home page"""
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Não foram encontradas receitas :(', response.content.decode('utf-8'))

    def test_home_template(self):
        """check if home template loads recipes"""
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe-Test', content)
        self.assertEqual(len(response_context_recipes), 1)


    def test_category_status(self):
        """test category page is 404 if not recipes found"""
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 10}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_404(self):
        """test if page is 404 if not recipes detail found"""
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 10}))
        self.assertEqual(response.status_code, 404)