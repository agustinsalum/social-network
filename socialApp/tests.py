from django.test import TestCase
from django.contrib.auth.models import User
from .models import Lesson, UserProfile, Friendship, TakenLesson

# Create your tests here.

"""

To run the test you must type in your console:

python manage.py test socialApp.tests.ModelsTestCase.test_lesson_creation
"""

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.profile1 = UserProfile.objects.create(user=self.user1)
        self.profile2 = UserProfile.objects.create(user=self.user2)
        self.lesson = Lesson.objects.create(name='Statistics', topic='Math')
        self.taken_lesson = TakenLesson.objects.create(user=self.profile1, lesson=self.lesson, times_taken=2)
        self.friendship = Friendship.objects.create(from_user=self.profile1, to_user=self.profile2)

    def test_lesson_creation(self):
        lesson = Lesson.objects.get(name='Statistics')
        # checks if the topic property of the lesson matches the expected value
        self.assertEqual(lesson.topic, 'Math')

    def test_user_profile_creation(self):
        # Check if the variables are instances of the UserProfile class.
        self.assertIsInstance(self.profile1, UserProfile)
        self.assertIsInstance(self.profile2, UserProfile)
        # Verify that the user field of each profile points to the correct user
        self.assertEqual(self.profile1.user, self.user1)
        self.assertEqual(self.profile2.user, self.user2)

    def test_taken_lesson_creation(self):
        self.assertIsInstance(self.taken_lesson, TakenLesson)
        self.assertEqual(self.taken_lesson.user, self.profile1)
        self.assertEqual(self.taken_lesson.lesson, self.lesson)
        self.assertEqual(self.taken_lesson.times_taken, 2)

    def test_friendship_creation(self):
        self.assertIsInstance(self.friendship, Friendship)
        self.assertEqual(self.friendship.from_user, self.profile1)
        self.assertEqual(self.friendship.to_user, self.profile2)

    def test_friendship_updates_followers_and_following(self):
        # Test if followers and following are updated after Friendship creation
        self.assertEqual(self.profile1.followers.count(), 1)
        self.assertEqual(self.profile2.followers.count(), 0)
        self.assertEqual(self.profile1.following.count(), 0)
        self.assertEqual(self.profile2.following.count(), 1)

