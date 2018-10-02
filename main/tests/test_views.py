from django.test import TestCase


class SplashPageViewUnitTest(TestCase):

    def test_splash_page_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_splash_page_gives_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'splash.html')


class ViewArticlesUnitTest(TestCase):

    def test_view_articles_endpoint_exists(self):
        # main view where all articles are listed by default
        response = self.client.get('/articles')
        self.assertEqual(response.status_code, 200)

    def test_view_articles_page_gives_correct_template(self):
        response = self.client.get('/articles')
        self.assertTemplateUsed(response, 'view_articles.html')
