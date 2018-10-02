from django.test import LiveServerTestCase

from selenium import webdriver


class AdminLoginTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # setup admin user

    def tearDown(self):
        self.browser.quit()

    def test_admin_can_login_to_admin_site(self):
        # Ryuz, a lone citizen of her foggy and distant world, has
        # taken up reading, and enjoyed many books. She decides to write
        # about them on Bookview, seeing as she's an admin

        # First, she must go to the login page
        self.browser.get(self.live_server_url + '/login')

        # She sees a login form with a title, as well as username and password fields
        login_form_title = self.browser.find_element_by_class_name('login-form__title')
        self.assertEqual(login_form_title.text, "Bookview Admin Login")
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')

        # She types in her username and password
        username_input.send_keys('ryuz')
        password_input.send_keys('manyfogs')
        # And clicks the 'Login' button 
        self.browser.find_element_by_id('submit').click()

        # She happily finds herself in the admin section, ready to share
        # what she has enjoyed
        self.assertEqual(self.browser.curernt_url, self.live_server_url + '/admin')

