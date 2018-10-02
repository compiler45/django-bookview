from django.test import LiveServerTestCase

from selenium import webdriver


class UserVisitiTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_user_sees_splash_page_and_uses_that_to_go_to_articles_page(self):
        # Maetel is interested in finding out about some interesting books
        # She recalls someone mentioning Bookview, and decides to check it
        # out
        self.browser.get(self.live_server_url)
        # She lands on a splash page, where she sees nice introductory text,
        # and a prominent link directing her to the main site
        greeting = self.browser.find_element_by_class_name("intro__greeting")
        self.assertEqual(greeting.text , "Welcome to Bookview")

        go_to_main_site = self.browser.find_element_by_css_selector("a.intro__go-to-main-site")
        # Actual link has a little arrow beside the text...
        self.assertIn("Go to Main Site", go_to_main_site.text)
        # She clicks it 
        go_to_main_site.click()

        # And she ends up on the main view, where she can see the latest articles
        self.assertEqual(self.browser.current_url, self.live_server_url + '/articles')
        # And some text telling her that she is looking at the latest articles
        latest_articles = self.browser.find_element_by_css_selector("h3.main-page-heading")
        self.assertEqual(latest_articles.text, "Latest Articles")

