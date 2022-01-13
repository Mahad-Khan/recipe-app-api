from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class ModelTests(APITestCase):

    def test_create_user_with_email_successful(self):
        """ test creating a new user with an eamil and password is successful"""
        email = "qwe@asd.com"
        password = "pass@123"
        user_model = get_user_model()
        user = user_model.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """ test the new user email is normalized"""
        email = "asd@Yahoo.com"
        password = "pass123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_with_invalid_email(self):
        """ test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password="pass123")
