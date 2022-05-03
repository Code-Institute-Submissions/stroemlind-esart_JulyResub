from django.test import TestCase
from .models import RequestPoster


class TestRequestPosterModel(TestCase):
    """
    Test the PostModel
    """
    @classmethod
    def setUpTestData(cls):
        RequestPoster.objects.create(
            full_name='Test Out',
            email='test@mail.com',
            phone_number='123949596',
            date='2022.05.03',
            motive='I want to request',
            image='placeholder',
        )

    def test_full_name_max_length(self):
        """ test full_name max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 70)

    def test_email_max_length(self):
        """ test email max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('email').max_length
        self.assertEqual(max_length, 200)

    def test_phone_number_max_length(self):
        """ test email max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_motive_max_length(self):
        """ test email max length """
        poster_request = RequestPoster.objects.get(id=1)
        max_length = poster_request._meta.get_field('motive').max_length
        self.assertEqual(max_length, 500)
