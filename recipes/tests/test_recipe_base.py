from django.test import TestCase
from recipes.models import *

class RecipeTestBase(TestCase):
    def setUp(self) -> None:

        return super().setUp()

    def make_recipe_category(self, name='Lanche'):

        return Category.objects.create(name=name)
    
    def make_recipe_author(self, first_name='José', last_name='Janglenssen', username='Janglenssen', password='123456', email='jose@janglenssen.com'):
        
        return User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
    
    def make_recipe(self, category_data = None, author_data = None, title = 'Recipe-Test', 
                            description = 'Recipe-Unit-Test', slug = 'recipe-test', preparation_time = 10, preparation_time_unit = 'Minutos', servings = 5, servings_unit = 'Porções',
                                preparation_steps = 'Recipe-Unit-Test', preparation_steps_is_html = False, is_published = True,):
        

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category = self.category(**category_data),
            author = self.author(**author_data),
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,  
        )