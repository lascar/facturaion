from django.utils.translation import gettext as _
import re
import pdb
from selenium.webdriver.common.by import By
from django.core import mail
from .base import FunctionalTest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
import time

TEST_EMAIL = 'toto@example.com'
TEST_NAME = 'Testuser'
TEST_PASSWORD = 'XyZzy12345'
SUBJECT = _('Your magic login link')

class FactuTest(FunctionalTest):

    def test_can_list_staff_members(self):
        self.client.force_login(self.test_user)
        self.browser.get(self.live_server_url + '/staff/')
        self.assertIn(_('Staff members'), self.browser.find_element(By.TAG_NAME, 'body').text)
        breakpoint()
        self.browser.get(self.live_server_url + '/auth/send-magic-link/')
        self.browser.find_element(By.NAME, 'email').send_keys(TEST_EMAIL)
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        self.wait_for(lambda: self.assertIn(
            _('A magic link has been sent to your email.'),
            self.browser.find_element(By.TAG_NAME, 'body').text
        ))

        email = mail.outbox[0]  
        self.assertIn(TEST_EMAIL, email.to)
        print('email.subject')
        print(email.subject)
        self.assertEqual(email.subject, SUBJECT)

        self.assertIn(_('Click the link below to log in'), email.body)
        url_search = re.search(r'http://[^/]+/[^/]+/[^/]+/[^/]+/[a-zA-Z0-9]+', email.body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        self.browser.get(url)
        self.assertIn("Hi " + TEST_NAME, self.browser.find_element(By.TAG_NAME, 'body').text)
        
        self.browser.find_element(By.ID, "logout").click()
        # logout_input.submit()
        # logout_input_id = "logout"
        # ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        # logout_input = WebDriverWait(self.browser, 5, ignored_exceptions=ignored_exceptions)\
        #                 .until(expected_conditions.presence_of_element_located((By.ID, logout_input_id)))
        # logout_input.click()
        # WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID, "logout"))).click()
        self.assertIn(_('Do you need an account'), self.browser.find_element(By.TAG_NAME, 'body').text)

        self.browser.find_element(By.ID, "login").click()
        self.browser.find_element(By.NAME, 'username').send_keys(TEST_NAME)
        self.browser.find_element(By.NAME, 'password').send_keys(TEST_PASSWORD)
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        self.assertIn("Hi " + TEST_NAME, self.browser.find_element(By.TAG_NAME, 'body').text)
