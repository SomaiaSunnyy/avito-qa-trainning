import pytest
import random
import time
from selenium import webdriver
from catalog_page import CatalogPage

catalog_link = "http://tech-avito-intern.jumpingcrab.com/"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)
    driver.quit()



def test_ad_create(driver):
    """
    Проверка создания объявления
    ------
    1. Переход на сайт
    2. Открытие модального окна создания объявления
    3. Заполнение полей и создание объявления
    4. Проверка, что модальное окно закрылось
    """
    
    catalog_page = CatalogPage(driver)
    catalog_page.open(catalog_link)
    
    ad_name = f"Объявление №{random.randint(0, 999)}"
    
    # Заполнение данных для создания объявления
    catalog_page.open_widget_for_create_new_ad()
    catalog_page.enter_name(ad_name)
    catalog_page.enter_price(random.randint(250, 99999))
    catalog_page.enter_description("Тут когда-нибудь будет описание товара :)")
    catalog_page.enter_image_url("https://www.modi.ru/upload/product/107/ue4i547epw6ml1m1r5y8ncrvvzq1t93x.jpg")
    catalog_page.click_submit_button()
    
    # Проверка закрытия модального окна --> успешная отработка создания
    assert not catalog_page.is_modal_displayed(), f"Модальное окно не закрылось после создания товара"



def test_modal_validation_form(driver):
    """
    Проверка валидации полей в модальном окне создания объявления
    ------
    1. Переход на сайт
    2. Открытие модального окна создания объявления
    3. Поочередная проверка валидации полей
    """
    
    catalog_page = CatalogPage(driver)
    catalog_page.open(catalog_link)
    
    ad_name = f"Объявление №{random.randint(0, 999)}"
    
    # Проверка валидации всех незаполненных полей
    catalog_page.open_widget_for_create_new_ad()
    catalog_page.click_submit_button()
    assert catalog_page.is_validation_name_field(), f"Неверно сработала валидация поля \"Название *\" (на шаге с проверкой 4 пустых полей)"
    assert catalog_page.is_validation_price_field(), f"Неверно сработала валидация поля \"Цена *\" (на шаге с проверкой 4 пустых полей)"
    assert catalog_page.is_validation_description_field(), f"Неверно сработала валидация поля \"Описание *\" (на шаге с проверкой 4 пустых полей)"
    assert catalog_page.is_validation_image_url_field(), f"Неверно сработала валидация поля \"Ссылка на изображение *\" (на шаге с проверкой 4 пустых полей)"
    
    
    # Проверка валидации после заполнения поля с названием
    catalog_page.enter_name(ad_name)
    catalog_page.click_submit_button()
    assert not catalog_page.is_validation_name_field(), f"Неверно сработала валидация поля \"Название *\" (на шаге с проверкой заполнения только имени)"
    assert catalog_page.is_validation_price_field(), f"Неверно сработала валидация поля \"Цена *\" (на шаге с проверкой заполнения только имени)"
    assert catalog_page.is_validation_description_field(), f"Неверно сработала валидация поля \"Описание *\" (на шаге с проверкой заполнения только имени)"
    assert catalog_page.is_validation_image_url_field(), f"Неверно сработала валидация поля \"Ссылка на изображение *\" (на шаге с проверкой заполнения только имени)"


    # Проверка валидации после заполнения поля с ценой
    catalog_page.enter_price(random.randint(250, 99999))
    catalog_page.click_submit_button()
    assert not catalog_page.is_validation_name_field(), f"Неверно сработала валидация поля \"Название *\" (на шаге с проверкой заполнения имени и цены)"
    assert not catalog_page.is_validation_price_field(), f"Неверно сработала валидация поля \"Цена *\" (на шаге с проверкой заполнения имени и цены)"
    assert catalog_page.is_validation_description_field(), f"Неверно сработала валидация поля \"Описание *\" (на шаге с проверкой заполнения имени и цены)"
    assert catalog_page.is_validation_image_url_field(), f"Неверно сработала валидация поля \"Ссылка на изображение *\" (на шаге с проверкой заполнения имени и цены)"


    # Проверка валидации после заполнения поля с описанием
    catalog_page.enter_description("Тут когда-нибудь будет описание товара :)")
    catalog_page.click_submit_button()
    assert not catalog_page.is_validation_name_field(), f"Неверно сработала валидация поля \"Название *\" (на шаге с проверкой заполнения имени и цены, и описания)"
    assert not catalog_page.is_validation_price_field(), f"Неверно сработала валидация поля \"Цена *\" (на шаге с проверкой заполнения имени и цены, и описания)"
    assert not catalog_page.is_validation_description_field(), f"Неверно сработала валидация поля \"Описание *\" (на шаге с проверкой заполнения имени и цены, и описания)"
    assert catalog_page.is_validation_image_url_field(), f"Неверно сработала валидация поля \"Ссылка на изображение *\" (на шаге с проверкой заполнения имени и цены, и описания)"


    # Проверка валидации после заполнения поля с URL изображения --> все поля заполнены и объявление успешн осоздалось
    catalog_page.enter_image_url("https://www.modi.ru/upload/product/107/ue4i547epw6ml1m1r5y8ncrvvzq1t93x.jpg")
    catalog_page.click_submit_button()
    assert not catalog_page.is_modal_displayed(), f"Модальное окно не закрылось после создания товара"
