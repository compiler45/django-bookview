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
        # And some large text in the left corner that is the website's branding
        bookview_brand_text = self.browser.find_element_by_css_selector('.navbar__home-link-text')
        self.assertEqual(bookview_brand_text.value_of_css_property("font-size"), "20px")
        self.assertEqual(bookview_brand_text.text, "Bookview")

    def test_clicking_navbar_home_link_takes_user_to_view_all_articles_page(self):
        # Maetel clicks the big bold navbar link
        self.browser.get(self.live_server_url + '/articles')
        bookview_brand_link = self.browser.find_element_by_css_selector('.navbar__home-link')
        bookview_brand_link.click()

        self.assertEqual(self.browser.current_url, self.live_server_url + '/articles')


