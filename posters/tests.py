from django.test import TestCase
from .models import Poster


class TestViews(TestCase):
    """ Test the code for the views """
    @classmethod
    def setUpTestData(cls):

        Poster.objects.create(
            name='Test Name',
            description='Test and test',
            size=True,
            quantity=1,
            price=50.00,
            image='placeholder'
        )

    def test_get_posters_page(self):
        """ Test to get the right template for the view """
        response = self.client.get('/posters/posters/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'posters/posters-page.html',
            'base.html'
        )
