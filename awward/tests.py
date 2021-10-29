from django.test import TestCase
from models import Profile,Post,Rate
from django.contrib.auth.models import User
import datetime

# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Indeche', password='123456')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        ''' method called before each test case'''
        self.user = User.objects.create_user(username='Water')

    def tearDown(self):
        ''' method to clear all setup instances after each test run '''
        self.user.delete()

    def test_profile_creation(self):
        ''' method to test profile instance is created only once for each user '''
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
class TestRating(TestCase):
    ''' test class for Rating model '''
    def setUp(self):
        ''' method called before all tests '''
        self.test_user = User(username='Andrew', password='123')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()
        self.test_post = Post(image='images/test.jpg', title='some text',description='some info', profile=self.test_profile, live_link='https://www.google.com', created_on=datetime.now())
        self.test_post.save()

        self.test_rate = Rating(interface=5, experience=6, content=5, user=self.test_profile, post=self.test_post)

    def tearDown(self):
        ''' method called after every test '''
        self.test_user.delete() #deletes it's profile too
        Post.objects.all().delete()
        Rating.objects.all().delete()

    def test_instance(self):
        ''' method to test instance creation '''
        self.assertIsInstance(self.test_rate, Rating)

    def test_save_and_delete_rating(self):
        ''' test method to save and delete ratings'''
        self.test_rate.save_rating()
        self.assertEqual(len(Rating.objects.all()), 1)
        self.test_rate.delete_rating()
        self.assertEqual(len(Rating.objects.all()), 0)
