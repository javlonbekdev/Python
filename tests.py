from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='yangilik matni ')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_objects_title = f'{post.title}'
        expected_objects_text = f'{post.text}'
        self.assertEqual(expected_objects_text, 'yangilik matni ')
        self.assertEqual(expected_objects_title, 'Mavzu')

class HomePageview(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text='boshqa yangilik')

    def test_views_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')



