#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from urlparse import urljoin
from selenium.webdriver.common.by import By
from pages.page import Page

class Base(Page):

    def go_to_page(self):
        url = urljoin(self.base_url, self._url)
        self.selenium.get(url)

    @property
    def header(self):
        return self.Header(self.testsetup)


    class Header(Page):
        _user_account_locator = (By.CSS_SELECTOR, 'div.navbar ul.nav.pull-right > .user')
        _sing_out_locator = (By.CSS_SELECTOR, 'div.navbar ul.nav.pull-right > li > a')

        @property
        def is_user_logged_in(self):
            return self.is_element_visible(*self._user_account_locator)

        @property
        def user_account(self):
            return self.selenium.find_element(*self._user_account_locator).text

        def sing_out(self):
            self.selenium.find_element(*self._sing_out_locator).click()
            from pages.login import Login
            return Login(self.testsetup)

