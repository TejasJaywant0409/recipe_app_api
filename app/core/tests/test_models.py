from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_user_with_email(self):

        # example.com is specifically used for testing purpose.
        user_email = 'test@example.com'
        user_password = 'test@1234'

        # .objects is reference to manager you are going to create.
        user = get_user_model().objects.create_user(
            email=user_email,
            password=user_password
        )

        self.assertEqual(user.email, user_email)

        # check_password is used for hashing.
        self.assertTrue(user.check_password(user_password))

    def test_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
            ]

        for email, excepted_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'testpass123')
            self.assertEqual(user.email, excepted_email)

    def test_new_user_without_email_raises_valueError(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test@123')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
           'test@example.com', 'test@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
