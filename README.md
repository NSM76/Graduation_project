# Graduation_project
## Rostelecom

## О проекте:

В репозитории содержится проект тестирования сайта Ростелеком, разделы:
##### 1. Регистрация в продуктах:
         1.	ЕЛК Web ( https://lk.rt.ru/ ), 
         2.	Старт Web ( https://start.rt.ru/ ), 
         3.	Ключ Web ( https://key.rt.ru/ )
##### 2. Авторизация в продуктах:
         1.	ЕЛК Web( https://lk.rt.ru/ ) , 
         2.	Онлайм Web ( https://my.rt.ru/ ),
         3.	Старт Web ( https://start.rt.ru/ ), 
         4.	Умный дом Web ( https://lk.smarthome.rt.ru/ ), 
         5.	Ключ Web ( https://key.rt.ru/ )
   
Тест-кейсы разрабатывались на основании требований заказчика - “[Требования_SSO_для_тестирования_last.doc](https://docs.google.com/document/d/1fOjYGOBZP10ssxL4jrEq3bG2wLUD_IKq/edit?usp=sharing&ouid=114969839533758832510&rtpof=true&sd=true)" и произведена их автоматизация для выполнения задания - Модуль 32. Дополнительные возможности Selenium. 12 Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии» 

### 1. Проект разделен на блоки «Регистрация» и «Авторизация».            
           Каждый блок разделен на модули по видам тестируемого продукта Ростелеком.

### 2. Проект содержит 89 [тест-кейсов](https://docs.google.com/spreadsheets/d/1jtPFhUiteMamwrttJVYrLK5jQ92eRWFx/edit?usp=sharing&ouid=114969839533758832510&rtpof=true&sd=true)

### 3. При составлении тест-кейсов применены:                                                                                                                                                                                            
      1. Метод «черного ящика» - применялся при составлении всех тест-кейсов.                            
      2. Техники позитивного и негативного тестирования – применялась для тестирования всех полей ввода форм регистрации и
         авторизации. Позитивное тестирование – при вводе корректных данных, негативное тестирование – при вводе некорректных данных.                
      3. Техники выделения классов эквивалентности и анализа граничных значений – применялась при тестировании полей ввода
         формы регистрации (поля ввода «Имя», «Фамилия», «Пароль»).       
      4. Техника тест-дизайна «таблица решений» («причина—следствие») или таблица альтернатив – применялась для составления позитивных
         и негативных тест-кейсов,  с помощью таблиц из требований с продуктами и их атрибутами (условия (входы) - логин, телефон,
         электронная почта, лицевой счет, пароль, ФИО, одноразовый код и результирующие действия системы (выходы) - регистрация ,
         аутентификация и авторизация)         
      5. Техника предугадывание или прогнозирование ошибок – применялась для тестирования полей ввода формы регистрации
         (для проверки двойных фамилий и имен)        

### 4. Написан 21 автотест (458 проверок). 
         Для написания автотестов были использованы:
          1.Язык программирования Python3
          2.Библиотеки PyTest , PyTest - Selenium
          3.Паттерн PageObject
          4.Фреймворк Smart Page Object (автор Тимур Нурлыгаянов) с дописанным методом очистки полей ввода
### 5. Описание файлов проекта:
    1. Из фреймворка Smart Page Object:
        1. pages/base.py – содержит базовый класс с методами для работы со страницей 
        2. pages/elements.py – содержит класс с методами для работы с элементами страницы
        3. conftest.py – содержит фикстуры , для работы с Selenium драйвером , настройками браузера , 
            для информативного вывода отчетов в терминале, для «перехвата» неудачных тестовых случаев
    2. pages/auth_page.py – содержит класс с элементами страницы авторизации
    3. pages/reg_page.py – содержит класс с элементами страницы регистрации
    4. tests/test_auth_page.py – содержит тесты для страницы авторизации
        1.	test_auth_form – проверка содержания формы авторизации в соответствии с требованиями
        2.	test_auth_log_and_pass_positive – проверка авторизации с валидными логином и паролем
        3.	test_auth_mail_and_pass_positive – проверка авторизации по валидным почте и паролю
        4.	test_auth_phone_and_pass_positive – проверка авторизации по валидным номеру телефона и паролю
        5.	test_auth_invalid_data_negative – проверка авторизации с невалидными данными
    5. tests/test_reg_page.py – содержит тесты для страницы регистрации
        1.	test_reg_form - проверка содержания формы регистрации в соответствии с требованиями
        2.	test_field_name_negative – проверка работы поля «Имя» в форме регистрации, при вводе невалидных данных
        3.	test_field_name_positive - проверка работы поля «Имя» в форме регистрации, при вводе валидных данных
        4.	test_field_name_latin_negative – проверка работы поля "Имя" в форме регистрации, при вводе невалидных данных латиницей
        5.	test_field_surname_negative – проверка работы поле "Фамилия" в форме регистрации, при вводе невалидных данных кирилицей
        6.	test_field_surname_positive - проверка работы поле "Фамилия" в форме регистрации, при вводе валидных данных кирилицей
        7.	test_field_surname_latin_negative - проверка работы поле "Фамилия" в форме регистрации, при вводе невалидных данных латиницей
        8.	test_reg_all_fields_empty_negative - проверка работы поле "Фамилия" в форме регистрации с пустыми полями
        9.	test_field_name2_positive - проверка работы поля «Имя» в форме регистрации, при вводе валидного двойного имени кирилицей
       10.	test_field_surname2_positive - проверка работы поле "Фамилия" в форме регистрации , при вводе валидной двойной фамилии кирилицей
       11.	test_field_email_or_phone_negative – проверка работы поля "E-mail или мобильный телефон" в форме регистрации при вводе невалидного email
       12.	test_field_email_or_phone_negative2 – проверка работы поля "E-mail или мобильный телефон" в форме регистрации при вводе невалидного номера телефона
       13.	test_field_password_negative – проверка работы поля "Пароль" в форме регистрации при вводе невалидных данных латиницей
       14.	test_field_password_negative2 – проверка работы поля "Пароль" в форме регистрации при вводе данных не латиницей (разных языковых групп)
       15.	test_field_pass_confirmation_negative – проверка работы поля "Подтверждения пароля" в форме регистрации при вводе данных не латиницей (разных языковых групп)
       16.	test_fields_pass_and_pass_confirmation_negative – проверка появления предупреждения "Пароли не совпадают" под полем
            "Подтверждение пароля" в форме регистрации, при вводе в поля "Пароль" и "Подтверждение пароля" несовпадающих валидных паролей
    6. config_data.py – содержит информационные данные
    7. Test documentation - содержит файл с  тест-кейсами, файл с баг-репортами, папку со скриншотами багов.
   
### 5. Запуск тестов для Windows:
        1. Установить requirements: pip3 install -r requirements.txt
        2. Скачать драйвер для вашей версии браузера - https://chromedriver.chromium.org/downloads
        3. Запустить тесты: 
            1. pytest -v --driver Chrome --driver-path ~/chromedriver_win32 tests
              или
            2. python -m pytest -v --driver Chrome --driver-path ~/chromedriver_win32 tests
              где chromedriver_win32 – это скачанный и разархивированный драйвер из пункта 2 

### 6. Описано 8 багов.

### 7. Инструменты, которые применялись
       1. PyCharm - IDE для разработки на Python
       2. ChroPath – плагин Google Chrome, для построения локаторов
       3. https://tempmail.plus - сервис для создания одноразового почтового ящика
       4. https://text.ru/seo - для анализа текста (подсчета символов, слов, …)
       5. http://www.unit-conversion.info/texttools/random-string-generator/ - для генерирования текста определенной
           длины из определенных символов

### 8. На Google [диске](https://drive.google.com/drive/folders/1wKqnLvgNVtM_iMqDvgW0_ZrEiSqiqr1E?usp=sharing) расположены:
       1. Набор тест-кейсов
       2. Баг-репорты
       3. Скриншоты

