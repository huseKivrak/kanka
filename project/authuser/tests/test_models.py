from rest_framework.test import APITestCase

from authuser.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user(
            'testuser', 'test@email.com', 'password!@#'
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'test@email.com')

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",
                          email='test@email.com', password='password!@#')

    def test_raises_error_with_message_when_no_username_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Username must be provided.'):
            User.objects.create_user(
                username=None,
                email='test@email.com',
                password='password!@#'
            )

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="testuser", email='', password='password!@#')

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Email must be provided.'):
            User.objects.create_user(
                username='testuser', email='', password='password!@#')

    def test_cant_create_superuser_without_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='testuser',
                email='test@email.com',
                password='password',
                is_staff=False
            )

    def test_cant_create_superuser_without_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='testuser',
                email='test@email.com',
                password='password',
                is_superuser=False
            )

    def test_creates_superuser(self):
        user = User.objects.create_superuser(
            'testuser', 'test@email.com', 'password!@#'
        )
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
