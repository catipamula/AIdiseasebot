from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AuthenticationFlowTests(TestCase):
    def test_chat_requires_login(self):
        response = self.client.get(reverse('chat'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_register_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'StrongPass123!',
                'password2': 'StrongPass123!',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_login_with_valid_credentials_redirects_to_chat(self):
        user = get_user_model().objects.create_user(username='alice', password='StrongPass123!')
        response = self.client.post(
            reverse('login'),
            {'username': 'alice', 'password': 'StrongPass123!'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('chat'))
        self.assertIn('_auth_user_id', self.client.session)

    def test_password_reset_page_accepts_registered_email(self):
        get_user_model().objects.create_user(username='bob', email='bob@example.com', password='StrongPass123!')
        response = self.client.post(
            reverse('password_reset'),
            {'email': 'bob@example.com'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('password_reset_done'))
