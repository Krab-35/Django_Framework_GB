from django.test import TestCase
from django.test.client import Client
from users.models import User
from django.core.management import call_command


class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django2@geekshop.local', 'geekbrains')

        self.user = User.objects.create_user('tarantino', 'tarantino@geekshop.local', 'geekbrains')

        self.user_with__first_name = User.objects.create_user(
            'umaturman',
            'umaturman@geekshop.local',
            'geekbrains',
            first_name='Ума',
            last_name='Турман',
        )

    def test_user_login(self):
        # главная без логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title'], 'GeekShop')
        self.assertNotContains(response, 'Пользователь', status_code=200)
        # self.assertNotIn('Пользователь', response.content.decode())

        # данные пользователя
        self.client.login(username='tarantino', password='geekbrains')

        # логинимся
        response = self.client.get('/users/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # главная после логина
        response = self.client.get('/')
        self.assertContains(response, 'Корзина пуста', status_code=200)
        self.assertEqual(response.context['user'], self.user)
        # self.assertIn('Пользователь', response.content.decode())

    def test_basket_login_redirect(self):
        # без логина должен переадресовать
        response = self.client.get('/users/profile/')
        self.assertEqual(response.url, '/users/login/?next=/users/profile/')
        self.assertEqual(response.status_code, 302)

        # с логином все должно быть хорошо
        self.client.login(username='tarantino', password='geekbrains')

        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(list(response.context['baskets']), [])
        self.assertEqual(response.request['PATH_INFO'], '/users/profile/')
        self.assertIn('Корзина пуста', response.content.decode())

    def tearDown(self):
        call_command('sqlsequencereset', 'products', 'users', 'orders', 'baskets')
