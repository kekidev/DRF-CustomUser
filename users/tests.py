from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):
    def test_superuser(self):
        db = get_user_model()
        superuser = db.objects.create_superuser(
            'testuser@super.com', 'username', 'password'
        )
        
        self.assertEqual(superuser.email, "testuser@super.com")
        self.assertEqual(superuser.username, 'username')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertEqual(str(superuser), "testuser@super.com")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', username='username1', password='password', is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testuser@super.com', username='username1', password='password', is_staff=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', username='username1', password='password', is_superuser=True)

                
    def test_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@user.com', 'username', 'password')
        self.assertEqual(user.email, 'testuser@user.com')
        self.assertEqual(user.username, 'username')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='a', password='password')