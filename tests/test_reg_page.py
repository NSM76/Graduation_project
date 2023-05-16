import pytest

from pages.reg_page import RegPage
from config_data import Info


# 1 RT-1, RT-19, RT-37
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ЕLK_Web", "URL_START_Web", "URL_Key_Web"])
def test_reg_form(web_browser, url_product):
    """1 Сhecking the content of the registration page"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    assert page.name_page_reg.is_presented(), "The element is missing on the page"
    assert page.first_name_field.is_presented(), "The element is missing on the page"
    assert page.surname_field.is_presented(), "The element is missing on the page"
    assert page.email_phone.is_presented(), "The element is missing on the page"
    assert page.pass_for_reg.is_presented(), "The element is missing on the page"
    assert page.pass_for_reg_confirm.is_presented(), "The element is missing on the page"
    assert page.agreement_reg.is_presented(), "The element is missing on the page"
    assert page.button_continue_on_reg_page.get_text() == Info.reg_text, "The element is missing on the page"
    assert page.tagline_reg.is_presented(), "The element is missing on the page"


# 2 RT-4, RT-22, RT-40
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name", ["ц", "ПщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШц"], ids=["1 cyrillic", "31 cyrillic"])
def test_field_name_negative(web_browser, url_product, name):
    """2 Сhecking the field "Name" with invalid Cyrillic data"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"


# 3 RT-5, RT-23, RT-41
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name", ["цл", "цЦл", "ПщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекн", "ПщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШ"],
                         ids=["1 cyrillic", "2 cyrillic", "29 cyrillic", "30 cyrillic"])
def test_field_name_positive(web_browser, url_product, name):
    """3 Checking the "Name" field with valid data in Cyrillic"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"


# 4 RT-6, RT-24, RT-42
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name", ["r", "re", "reg", "QixxYeymUnAkcwZYcpBnMJhBzQYQI", "QixxYeymUnAkcwZYcpBnMJhBzQYQIs",
                                  "QixxYeymUnAkcwZYcpBnMJhBzQYQIsS"],
                         ids=["1 latin", "2 latin", "3 latin", "29 latin", "30 latin", "31 latin"])
def test_field_name_latin_negative(web_browser, url_product, name):
    """4 Checking the "Name" field with invalid data in Latin"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"


# 5 RT-7, RT-25, RT-43
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("surname", ["ц", "ПщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШц"], ids=["1 cyrillic", "31 cyrillic"])
def test_field_surname_negative(web_browser, url_product, surname):
    """5 Checking the field "Last name" with invalid Cyrillic data"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"


# 6 RT-8, RT-26, RT-44
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("surname", ["цл", "цЦл", "ПщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекн", "ПщЧЫОЧеММДЩЗЦящьРбАХцЙЫчаЮекнШ"],
                         ids=["1 cyrillic", "2 cyrillic", "29 cyrillic", "30 cyrillic"])
def test_field_surname_positive(web_browser, url_product, surname):
    """6 Сhecking the field "Last name" with valid data in Cyrillic"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"


# 7 RT-9, RT-27, RT-45
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("surname",
                         ["r", "re", "reg", "QixxYeymUnAkcwZYcpBnMJhBzQYQI", "QixxYeymUnAkcwZYcpBnMJhBzQYQIs",
                          "QixxYeymUnAkcwZYcpBnMJhBzQYQIsS"],
                         ids=["1 latin", "2 latin", "3 latin", "29 latin", "30 latin", "31 latin"])
def test_field_surname_latin_negative(web_browser, url_product, surname):
    """7 Checking the "Last name" field with invalid data in Latin"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(surname)

    page.first_name_field.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"


# 8 RT-10, RT-28, RT-46
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
def test_reg_all_fields_empty_negative(web_browser, url_product):
    """8 Registration with empty fields"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.clear_field()
    page.surname_field.clear_field()
    page.email_phone.clear_field()
    page.pass_for_reg.clear_field()
    page.pass_for_reg_confirm.clear_field()
    page.button_continue_on_reg_page.click()

    assert page.tooltip_first_name_field.is_presented(), "The tooltip was not found"
    assert page.tooltip_surname_field.is_presented(), "The tooltip was not found"
    assert page.tooltip_email_phone.is_presented(), "The tooltip was not found"
    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"
    assert page.tooltip_pass_for_reg_confirm.is_presented(), "The tooltip was not found"


# 9 RT-11, RT-29, RT-47
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name",
                         ["цл-гЧчЗНАЗыЛьмЛтьЭ", "цл-гЧчЗНАЗыЛьмЛтьЭц", "гЧчЗНАЗыЛьмЛтьЭ-цл", "гЧчЗНАЗыЛьмЛтьЭц-цл"],
                         ids=["2 cyrillic+dash+15 cyrillic", "2 cyrillic+dash+16 cyrillic",
                              "15 cyrillic+dash+2 cyrillic", "16 cyrillic+dash+2 cyrillic"])
def test_field_name2_positive(web_browser, url_product, name):
    """9 Checking the "Name" field with valid data in Cyrillic+dash"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.first_name_field.send_keys(name)

    page.surname_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"


# 10 RT-12, RT-30, RT-48
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("name",
                         ["цл-гЧчЗНАЗыЛьмЛтьЭ", "цл-гЧчЗНАЗыЛьмЛтьЭц", "гЧчЗНАЗыЛьмЛтьЭ-цл", "гЧчЗНАЗыЛьмЛтьЭц-цл"],
                         ids=["2 cyrillic+dash+15 cyrillic", "2 cyrillic+dash+16 cyrillic",
                              "15 cyrillic+dash+2 cyrillic", "16 cyrillic+dash+2 cyrillic"])
def test_field_surname2_positive(web_browser, url_product, name):
    """10 Checking the "Last name" field with valid data in Cyrillic+dash"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.surname_field.send_keys(name)

    page.first_name_field.click()

    assert not page.tooltip_first_name_field.is_presented(), "A tooltip appeared"


# 11 RT-13, RT-31, RT-49
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("x",
                         ["ascv", "цлпд", "123", ".", "@", ""],
                         ids=["latin", "cyrillic", "digit", "dot", "symbol @", "empty"])
@pytest.mark.parametrize("y",
                         ["@", ""],
                         ids=["symbol @", "empty"])
@pytest.mark.parametrize("d",
                         [".", ""],
                         ids=["dot", "empty"])
@pytest.mark.parametrize("z",
                         ["zxc", "хдп", "123", ""],
                         ids=["latin", "cyrillic", "digit", "empty"])
def test_field_email_or_phone_negative(web_browser, url_product, x, y, d, z):
    """11 Checking the field "Email or mobile phone" with invalid email"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.wait_to_be_clickable()
    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    # запись вариантов проверок в файл
    # with open(f"data_options_email.txt", 'a', encoding="utf8") as MyFile:
    #     MyFile.write(f"{x}{y}{d}{z},\n")

    page.email_phone.send_keys(f"{x}{y}{d}{z}")

    page.button_continue_on_reg_page.click()

    assert page.tooltip_email_phone.is_presented(), "The tooltip was not found"


# 12 RT-14, RT-32, RT-50
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("phone", ["8985683r123"])
def test_field_email_or_phone_negative2(web_browser, url_product, phone):
    """12 Checking the field "Email or mobile phone" with invalid phone"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    # запись вариантов проверок в файл
    # with open(f"data_options_phone.txt", 'a', encoding="utf8") as MyFile:
    #     MyFile.write(f"{x}{y}{d}{z},\n")

    page.email_phone.send_keys(phone)

    page.button_continue_on_reg_page.click()

    assert page.tooltip_email_phone.is_presented(), "The tooltip was not found"


# 13 RT-15, RT-33, RT-51
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("password",
                         ["ifvbmaf", "ifvbmafr", "ifvbmafQ"],
                         ids=["7 lowercase Latin", "8 lowercase Latin", "7 lowercase Latin + 1 uppercase Latin"])
def test_field_password_negative(web_browser, url_product, password):
    """13 Checking the "Password" field with invalid data in Latin characters"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"


# 14 RT-16, RT-34, RT-52
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("password",
                         ["поРлвсГллм1Qr", "龍門大酒家龍門大酒家1Qr", "صسغذئآصسغذئآ1Qr"])
def test_field_password_negative2(web_browser, url_product, password):
    """14 The "Password" field with non-Latin characters """

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(password)

    page.pass_for_reg_confirm.click()

    assert page.tooltip_pass_for_reg.is_presented(), "The tooltip was not found"


# 15 RT-17, RT-35, RT-53
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
@pytest.mark.parametrize("pass_conf",
                         ["поРлвсГллм1Qr", "龍門大酒家龍門大酒家1Qr", "صسغذئآصسغذئآ1Qr"])
def test_field_pass_confirmation_negative(web_browser, url_product, pass_conf):
    """15 The "Password confirmation" field with non-Latin characters"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg_confirm.send_keys(pass_conf)

    page.pass_for_reg.click()

    assert page.tooltip_pass_for_reg_confirm.is_presented(), "The tooltip was not found"


# 16 RT-18, RT-36, RT-54
@pytest.mark.parametrize("url_product", [Info.URL_ELK_Web, Info.URL_START_Web, Info.URL_Key_Web],
                         ids=["URL_ELK_Web", "URL_START_Web", "URL_Key_Web"])
def test_fields_pass_and_pass_confirmation_negative(web_browser, url_product):
    """16 Fields "Password" and "Confirm password" with mismatched valid data"""

    page = RegPage(web_browser, url_product)

    if url_product == Info.URL_Key_Web:
        page.button_enter.click()

    page.enter_with_password.click()

    page.link_reg_on_auth_page.click()

    page.pass_for_reg.send_keys(Info.valid_password1)
    page.pass_for_reg_confirm.send_keys(Info.invalid_password2)

    page.first_name_field.click()

    assert page.tooltip_pass_for_reg_confirm.is_presented(), "The tooltip was not found"
