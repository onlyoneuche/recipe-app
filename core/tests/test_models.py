from django.db.models.expressions import Value
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_is_successful(self):
        """Test creating a new user with email is successful"""

        email = "email@email.com"
        password = "p@ssword"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_create_user_with_normalized_email(self):
        """Test user email is normalized"""

        email = "hello@EMAIL.COM"
        user = get_user_model().objects.create_user(email, "abc1231")

        self.assertEqual(user.email, email.lower())

    
    def test_creating_user_without_email_fails(self):
        """Test raises Value error if email is not provided"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "ioioasw23")
