import pytest
import time
import random
from selenium import webdriver
from catalog_page import CatalogPage

catalog_link = "http://tech-avito-intern.jumpingcrab.com/"

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)
    driver.quit()



def test_edit_ad(driver):
    """
    Проверка редактирования объявления
    --------
    Шаги кейса:
    1. Открыть сайт
    2. Открыть объявление
    3. Нажать кнопку редактирования
    4. Проверить, что все нужные для редактирования поля есть на странице
    и что значения из объявления совпадают со значениями в этих полях
    5. Отредактировать значение в поле и сохранить (повторить поочередно со всеми полями)
    """
    
    catalog_page = CatalogPage(driver)
    catalog_page.open(catalog_link)

    # Поиск и переход в первое объявление
    catalog_page.search_ad("Объявление №") # Для поиска точно существующих объявлений и теста на них
    card_name = catalog_page.get_ad_name()
    ad_page = catalog_page.open_ad_page(card_name)

    # Сохраняются атрибуты карточки объявления и то, что записано в полях редактирования
    ad_image_url_before_edit_mode = ad_page.get_ad_image_url()
    ad_name_before_edit_mode = ad_page.get_ad_name()
    ad_price_before_edit_mode = ad_page.get_ad_price()
    ad_description_before_edit_mode = ad_page.get_ad_description()
    
    ad_page.click_start_edit_button()

    ad_image_url_in_edit_mode = ad_page.get_ad_image_url_in_edit_field()
    ad_name_in_edit_mode = ad_page.get_ad_name_in_edit_field()
    ad_price_in_edit_mode = ad_page.get_ad_price_in_edit_field()
    ad_description_in_edit_mode = ad_page.get_ad_description_in_edit_field()

    # Проверка присутствия всех редактируемых полей
    assert ad_page.is_image_url_edit_field_visible(), f"Нет поля для редактирования URL изображения"
    assert ad_page.is_name_edit_field_visible(), f"Нет поля для редактирования имени"
    assert ad_page.is_price_edit_field_visible(), f"Нет поля для редактирования цены"
    assert ad_page.is_description_edit_field_visible(), f"Нет поля для редактирования описания"
    
    # Сверка данных в объявлении данным в режиме редактирования
    assert ad_image_url_before_edit_mode == ad_image_url_in_edit_mode
    assert ad_name_before_edit_mode == ad_name_in_edit_mode
    assert ad_price_before_edit_mode == ad_price_in_edit_mode
    assert ad_description_before_edit_mode == ad_description_in_edit_mode
      
    # Проверка редактирования названия
    new_ad_name = f"Тест редактирования имени {random.randint(0, 999)}"
    ad_page.edit_name_field(new_ad_name)
    ad_page.click_save_edit_button()
    ad_name_after_edit = ad_page.get_ad_name()
    
    assert new_ad_name == ad_name_after_edit
    
    # Проверка редактирования цены
    ad_page.click_start_edit_button()
    new_ad_price = random.randint(500, 999)
    ad_page.edit_price_field(new_ad_price)
    ad_page.click_save_edit_button()
    ad_price_after_edit = ad_page.get_ad_price()
    
    assert new_ad_price == ad_price_after_edit
    
    # Проверка редактирования описания
    ad_page.click_start_edit_button()
    new_ad_description = f"Тест редактирования описания {random.randint(0, 999)}"
    ad_page.edit_description_field(new_ad_description)
    ad_page.click_save_edit_button()
    ad_description_after_edit = ad_page.get_ad_description()
    
    assert new_ad_description == ad_description_after_edit
    
    # Проверка редактирования URL изображения
    ad_page.click_start_edit_button()
    new_ad_image_url = "https://goods-photos.static1-sima-land.com/items/7929061/1/700.jpg?v=1721111834"
    ad_page.edit_image_url_field(new_ad_image_url)
    ad_page.click_save_edit_button()
    ad_image_url_after_edit = ad_page.get_ad_image_url()
    
    assert new_ad_image_url == ad_image_url_after_edit
