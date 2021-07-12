from django.test import TestCase
from .models import Users


# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.user = Users.objects.create(name='Mubashir', desc='abc')

    def test_users_model(self):
        d = self.user
        self.assertTrue(isinstance(d, Users))
        self.assertEqual(str(d.name), 'Mubashir')
