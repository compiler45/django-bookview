from django.contrib.auth.models import User
from django.urls import reverse
from django.test import LiveServerTestCase

from selenium import webdriver


class AdminLoginTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.user = User.objects.create_superuser(username='ryuz', email='ryuz@fogs.com',
                                                  password='manyfogs')

    def tearDown(self):
        self.browser.quit()

    def test_admin_can_login_to_admin_site(self):
        # Ryuz, a lone citizen of her foggy and distant world, has
        # taken up reading, and enjoyed many books. She decides to write
        # about them on Bookview, seeing as she's an admin

        # First, she must go to the login page
        self.browser.get(self.live_server_url + reverse('admin:login'))

        # She sees a login form with a title, as well as username and password fields
        login_form_title = self.browser.find_element_by_id("site-name")
        self.assertEqual(login_form_title.text, "Bookview Admin")
        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')

        # She types in her username and password
        username_input.send_keys('ryuz')
        password_input.send_keys('manyfogs')
        # And clicks the 'Login' button 
        self.browser.find_element_by_css_selector("input[type='submit']").click()

        # She happily finds herself on the admin's index page, ready to share
        # what she has enjoyed
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse('admin:index'))

    def test_admin_enteres_incorrect_username_password_pair(self):
        # Ryuz is feeling a bit tired, but unwisely tries to log
        # in to Bookview anyway
        login_url = self.live_server_url + reverse('admin:login')
        self.browser.get(login_url)

        username_input = self.browser.find_element_by_name('username')
        password_input = self.browser.find_element_by_name('password')

        # She types in her username and password
        username_input.send_keys('ryuz')
        password_input.send_keys('manyfogd')
        self.browser.find_element_by_css_selector("input[type='submit']").click()

        # To her dismay, she hasn't moved an inch!
        self.assertEqual(self.browser.current_url, login_url)

        error_message = self.browser.find_element_by_class_name("errornote")
        self.assertIn("Please enter the correct username and password for a staff account", error_message.text)

