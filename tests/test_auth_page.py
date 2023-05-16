import pytest

from pages.auth_page import AuthPage
from config_data import Info
import time


# 17 RT-55, RT-62, RT-69 , RT-76 , RT-83
@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_Onlaim_Web, Info.URL_START_Web, Info.URL_SmartHome_Web,
                          Info.URL_Key_Web],
                         ids=["URL_ЕLK_Web", "URL_Onlaim_Web", "URL_START_Web", "URL_SmartHome_Web", "URL_Key_Web"])
def test_auth_form(web_browser, url_product):
    """17 Сhecking the content of the authorization page:."""

    page = AuthPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    assert page.name_page_auth.is_presented()

    assert page.tab_phone.is_presented()
    assert page.tab_mail.is_presented()
    assert page.tab_login.is_presented()

    assert page.field_username.is_presented()
    assert page.field_password.is_presented()

    assert page.show_password.is_presented()
    assert page.checkbox.is_presented()
    assert page.link_forgot_password.is_presented()
    assert page.button_enter_auth.is_presented()
    assert page.button_enter_with_temp_code.is_presented()
    assert page.agreement_auth.is_presented()

    assert page.link_vk.is_presented()
    assert page.link_ok.is_presented()
    assert page.link_mail.is_presented()
    assert page.link_google.is_presented()
    assert page.link_ya.is_presented()

    assert page.tab_mail.get_text() == Info.tab_mail_text
    assert page.tab_login.get_text() == Info.tab_login_text

    if url_product in [Info.URL_ELK_Web, Info.URL_START_Web]:
        assert page.tab_personal_account.is_presented()
        assert page.tab_personal_account.get_text() == Info.tab_personal_account_text

    if url_product == Info.URL_Onlaim_Web:
        assert not page.tab_personal_account.is_presented()
        assert not page.link_reg.is_presented()
    else:
        assert page.link_reg.is_presented()

    if url_product in [Info.URL_SmartHome_Web, Info.URL_Key_Web]:
        assert not page.tab_personal_account.is_presented()

    assert page.tab_phone.get_text() == Info.tab_phone_text


# 18 RT-56, RT-63, RT-70 , RT-77 , RT-84
@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_Onlaim_Web, Info.URL_START_Web, Info.URL_SmartHome_Web,
                          Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_Onlaim_Web", "URL_START_Web", "URL_SmartHome_Web", "URL_Key_Web"])
def test_auth_log_and_pass_positive(web_browser, url_product):
    """18 User authorization with a valid login and password."""

    page = AuthPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.tab_login.click()

    page.field_username.send_keys(Info.login_lc)
    page.field_password.send_keys(Info.valid_password1)

    page.button_enter_auth.click()

    if url_product == Info.URL_ELK_Web:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    elif url_product == Info.URL_Onlaim_Web:
        page.button_pass_onlime_lc.click()
        assert page.personal_acc_onlime.is_presented()

    elif url_product == Info.URL_START_Web:
        assert page.personal_acc_start.is_presented()

    elif url_product == Info.URL_SmartHome_Web:
        assert page.personal_acc_SmartHome.is_presented()

    elif url_product == Info.URL_Key_Web:
        page.link_key_login.click()
        assert page.personal_acc_key_login.is_presented()


# 19 RT-57, RT-64, RT-71 , RT-78, RT-85
@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_Onlaim_Web, Info.URL_START_Web, Info.URL_SmartHome_Web,
                          Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_Onlaim_Web", "URL_START_Web", "URL_SmartHome_Web", "URL_Key_Web"])
def test_auth_mail_and_pass_positive(web_browser, url_product):
    """19 User authorization with a valid mail and password."""

    page = AuthPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.tab_mail.click()

    page.field_username.send_keys(Info.mail_lc)
    page.field_password.send_keys(Info.valid_password1)

    page.button_enter_auth.click()

    if url_product == Info.URL_ELK_Web:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    if url_product == Info.URL_Onlaim_Web:
        page.button_pass_onlime_lc.click()
        assert page.personal_acc_onlime.is_presented()

    if url_product == Info.URL_START_Web:
        assert page.personal_acc_start.is_presented()

    if url_product == Info.URL_SmartHome_Web:
        assert page.personal_acc_SmartHome.is_presented()

    if url_product == Info.URL_Key_Web:
        page.link_key_login.click()
        assert page.personal_acc_key_login.is_presented()


# 20 RT-58, RT-65, RT-72 , RT-79, RT-86
@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_Onlaim_Web, Info.URL_START_Web, Info.URL_SmartHome_Web,
                          Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_Onlaim_Web", "URL_START_Web", "URL_SmartHome_Web", "URL_Key_Web"])
def test_auth_phone_and_pass_positive(web_browser, url_product):
    """20 User authorization with a valid phone and password."""

    page = AuthPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.tab_phone.click()

    page.field_username.send_keys(Info.phone_lc)
    page.field_password.send_keys(Info.valid_password1)

    page.button_enter_auth.click()

    if url_product == Info.URL_ELK_Web:
        page.personal_acc_elk.wait_to_be_clickable()
        assert page.personal_acc_elk.is_presented()

    if url_product == Info.URL_Onlaim_Web:
        page.button_pass_onlime_lc.click()
        assert page.personal_acc_onlime.is_presented()

    if url_product == Info.URL_START_Web:
        assert page.personal_acc_start.is_presented()

    if url_product == Info.URL_SmartHome_Web:
        assert page.personal_acc_SmartHome.is_presented()

    if url_product == Info.URL_Key_Web:
        assert page.link_key_phone.is_presented()


# 21 RT-59, RT-60, RT-61, RT-66, RT-67, RT-68, RT-73, RT-74, RT-75, RT-80, RT-81, RT-82, RT-87, RT-88, RT-89
@pytest.mark.parametrize("url_product",
                         [Info.URL_ELK_Web, Info.URL_Onlaim_Web, Info.URL_START_Web, Info.URL_SmartHome_Web,
                          Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_Onlaim_Web", "URL_START_Web", "URL_SmartHome_Web", "URL_Key_Web"])
@pytest.mark.parametrize(("login", "password"),
                         [(Info.login_lc, Info.invalid_password2), (Info.invalid_login_lc, Info.valid_password1),
                          (Info.invalid_login_lc, Info.invalid_password2)],
                         ids=["valid_login-invalid_password", "invalid_login-valid_password",
                              "invalid_login-invalid_password"])
def test_auth_invalid_data_negative(web_browser, url_product, login, password):
    """21 Authorization with negative data."""

    page = AuthPage(web_browser)

    # для избегания капчи вход с валидными данными
    page.enter_with_password.click()
    page.tab_login.click()
    page.field_username.send_keys(Info.login_lc)
    page.field_password.send_keys(Info.valid_password1)
    page.button_enter_auth.click()
    page.enter_to_mini_lc_elk.wait_to_be_clickable()
    if page.enter_to_mini_lc_elk.is_clickable():
        page.enter_to_mini_lc_elk.click()
    page.button_exit_mini_elk.click()
    time.sleep(1)

    page = AuthPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    # вход с невалидными данными
    page.enter_with_password.click()
    page.tab_login.click()

    page.field_username.send_keys(login)
    page.field_password.send_keys(password)
    page.button_enter_auth.click()

    assert page.error_message.is_presented()
