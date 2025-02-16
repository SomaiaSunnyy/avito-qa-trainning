from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base_page import BasePage

class AdPage(BasePage):
    """
    Класс страницы объявления
    ------
    Описаны селекторы элементов страницы объявления и методы: 
    - получения атрибутов из различных полей карточки объявления 
    (как из самой, так и из режима редактирования)
    - редактирования атрибутов объявления
    """

    """ Селекторы страницы объявления """
    AD_EDIT_BUTTON = (By.CSS_SELECTOR, "[style='cursor: pointer;']")
    AD_IMAGE_URL = (By.CSS_SELECTOR, "img[alt='product image']")
    AD_NAME = (By.CSS_SELECTOR, "header h2")
    AD_PRICE = (By.CSS_SELECTOR, "h2+p")
    AD_DESCRIPTION = (By.CSS_SELECTOR, "header+div p")
    """ Селекторы элементов в режиме редактирования объявления """
    AD_EDIT_IMAGE_URL_FIELD = (By.CSS_SELECTOR, "input[name='imageUrl']")
    AD_EDIT_NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    AD_EDIT_PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price']")
    AD_EDIT_DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea[name='description']")
    AD_SAVE_EDIT_BUTTON = (By.CSS_SELECTOR, "div svg[style='cursor: pointer;']")


    """ Методы для получения данных из полей: URL изображения, Название товара, Цена, Описание """
    
    def get_ad_image_url(self):
        return self.find_element(self.AD_IMAGE_URL).get_attribute("src")
    
    def get_ad_name(self):
        return self.find_element(self.AD_NAME).text
        
    def get_ad_price(self):
        price = self.find_element(self.AD_PRICE).text
        return int(price.replace(" ", "").replace("₽", ""))
    
    def get_ad_description(self):
        return self.find_element(self.AD_DESCRIPTION).text
    
    def get_ad_image_url_in_edit_field(self):
        return self.find_element(self.AD_EDIT_IMAGE_URL_FIELD).get_attribute("value")
    
    def get_ad_name_in_edit_field(self):
        return self.find_element(self.AD_EDIT_NAME_FIELD).get_attribute("value")
        
    def get_ad_price_in_edit_field(self):
        price = self.find_element(self.AD_EDIT_PRICE_FIELD).get_attribute("value")
        return int(price)
        
    def get_ad_description_in_edit_field(self):
        return self.find_element(self.AD_EDIT_DESCRIPTION_FIELD).text
    
    
    """ Методы редактирования полей объявления """

    def click_start_edit_button(self):
        self.click(self.AD_EDIT_BUTTON)
    
    def edit_image_url_field(self, new_text):
        self.input_text(self.AD_EDIT_IMAGE_URL_FIELD, new_text)
        
    def edit_name_field(self, new_text):
        self.input_text(self.AD_EDIT_NAME_FIELD, new_text)
        
    def edit_price_field(self, new_text):
        self.input_text(self.AD_EDIT_PRICE_FIELD, new_text)
        
    def edit_description_field(self, new_text):
        self.input_text(self.AD_EDIT_DESCRIPTION_FIELD, new_text)
    
    def click_save_edit_button(self):
        self.click(self.AD_SAVE_EDIT_BUTTON)


    """ Методы проверки присутствия полей на странице редактирования объявления """
    
    def is_name_edit_field_visible(self):
        try: 
            self.is_element_visible(self.AD_EDIT_NAME_FIELD)
            return True
        except NoSuchElementException:
            return False
        
    def is_price_edit_field_visible(self):
        try: 
            self.is_element_visible(self.AD_EDIT_PRICE_FIELD)
            return True
        except NoSuchElementException:
            return False
        
    def is_description_edit_field_visible(self):
        try: 
            self.is_element_visible(self.AD_EDIT_DESCRIPTION_FIELD)
            return True
        except NoSuchElementException:
            return False
        
    def is_image_url_edit_field_visible(self):
        try: 
            self.is_element_visible(self.AD_EDIT_IMAGE_URL_FIELD)
            return True
        except NoSuchElementException:
            return False
