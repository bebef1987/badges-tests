#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import Home
from pages.login import Login


class TestLogin():

    @pytest.mark.nondestructive
    @pytest.mark.credentials
    def test_login_logout(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.go_to_page()

        login_page = Login(mozwebqa)
        Assert.true(login_page.is_the_current_page)

        login_page.click_login()
        login_page.login(user='default')

        Assert.true(home_page.is_the_current_page)
        Assert.true(home_page.header.is_user_logged_in)
        Assert.equal(mozwebqa.credentials['default']['email'], home_page.header.user_account)

        login_page = home_page.header.sing_out()

        Assert.true(login_page.is_the_current_page)
        Assert.true(login_page.is_login_visible)

    def test_creating_a_new_user_logging_in_and_logingout(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.go_to_page()

        login_page = Login(mozwebqa)
        Assert.true(login_page.is_the_current_page)

        new_user = login_page.create_new_user()
        login_page.click_login()
        login_page.login(user=new_user)

        Assert.true(home_page.is_the_current_page)
        Assert.true(home_page.header.is_user_logged_in)
        Assert.equal(new_user['email'], home_page.header.user_account)

        login_page = home_page.header.sing_out()

        Assert.true(login_page.is_the_current_page)
        Assert.true(login_page.is_login_visible)