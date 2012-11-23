#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base


class Login(Base):

    _page_title = 'Open Badge Backpack'
    _url = '/backpack/login/'

    _login_locator=(By.CSS_SELECTOR, '.js-browserid-link > img')

    @property
    def is_login_visible(self):
        return self.is_element_visible(*self._login_locator)

    def click_login(self):
        self.selenium.find_element(*self._login_locator).click()

    def login(self, user = "default"):
        if isinstance(user, dict):
            credentials = {'email': user['email'], 'password':user['pass']}
        if isinstance(user, str):
            credentials = self.testsetup.credentials[user]

        from browserid import BrowserID
        pop_up = BrowserID(self.selenium, self.timeout)
        pop_up.sign_in(credentials['email'], credentials['password'])

        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.header.is_user_logged_in)

    def create_new_user(self):
        import urllib
        import json
        user = urllib.urlopen('http://personatestuser.org/email/').read()

        return json.loads(user)
