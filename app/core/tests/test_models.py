from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import User, Tag


class ModelsTest(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating  NEW USER is successfull."""
        email = "crycetruly@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        email = "test@ghtngnGM.COM"
        user = get_user_model().objects.create_user(
            email=email, password="test1234/.")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Ceating an invalid email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '')

    def test_create_new_super_user_success(self):
        """Test creating superuser"""
        user = get_user_model().objects.create_superuser(
            "email@email.com",
            "test1234"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        "test string representation"
        user = get_user_model().objects.create_user("test@test.com", "password")
        tag = Tag.objects.create(
            user=user, name="TestName")
        self.assertEqual(str(tag), "TestName")
