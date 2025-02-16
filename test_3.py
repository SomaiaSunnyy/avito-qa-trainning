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
    
    
    
def test_create_and_find_ad(driver):
    """
    Проверка поиска объявления
    -----
    1. Создается объявление для последующего поиска
    2. По названию нового объявления происходит поиск в каталоге
    3. Сравнивается название найденного объявления с тем, что было создано
    """
    
    catalog_page = CatalogPage(driver)
    catalog_page.open(catalog_link)
    
    ad_name = f"Объявление №{random.randint(0, 999)}"
    
    # Для отладки. Можно найти объявление на сайте вручную и проверить
    # print(ad_name) 
    
    # Заполнение данных для создания объявления
    catalog_page.open_widget_for_create_new_ad()
    catalog_page.enter_name(ad_name)
    catalog_page.enter_price(random.randint(250, 99999))
    catalog_page.enter_description("Тут когда-нибудь будет описание товара :)")
    catalog_page.enter_image_url("https://www.modi.ru/upload/product/107/ue4i547epw6ml1m1r5y8ncrvvzq1t93x.jpg")
    catalog_page.click_submit_button()
    
    # Поиск по каталогу
    # На этом шаге тест должен падать, т.к. кнопка поиска некликабельная, но не знаю как проверить
    catalog_page.search_ad(ad_name) 
    
    ad_catalog_name = catalog_page.get_ad_name()
    
    assert ad_catalog_name == ad_name, f"Тест не пройден! Ожидалось название объявления: \"{ad_name}\", найдено: \"{ad_catalog_name}\""
    
