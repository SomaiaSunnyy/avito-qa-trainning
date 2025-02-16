from base_page import BasePage
from ad_page import AdPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class CatalogPage(BasePage):
    """
    Класс страницы каталога
    ------
    Описаны селекторы элементов каталога и основные методы:
    - поиск объявления
    - переход в карточку
    - работа с модальным окном создания объявления
    """
    
    """ Селекторы главной страницы (каталога) """
    CTLG_CREATE_BUTTON = (By.CSS_SELECTOR, ".chakra-stack button:nth-child(4)")
    CTLG_SEARCH_FIELD = (By.CSS_SELECTOR, "input[value][placeholder]")
    CTLG_SEARCH_BUTTON = (By.CSS_SELECTOR, "input[value]+button")
    CTLG_AD = (By.CSS_SELECTOR, "p.chakra-text + div a")
    CTLG_AD_NAME = (By.CSS_SELECTOR, "a h4")
    """ Селекторы модального окна """
    MODAL_WINDOW = (By.CSS_SELECTOR, ".chakra-modal__content")
    MODAL_NAME_FIELD = (By.CSS_SELECTOR, "input[name='name'][value]")
    MODAL_PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price'][value]")
    MODAL_DESCRIPTION_FIELD = (By.CSS_SELECTOR, "input[name='description'][value]")
    MODAL_IMAGE_URL_FIELD = (By.CSS_SELECTOR, "input[name='imageUrl'][value]")
    MODAL_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    MODAL_VALIDATION_NAME_FIELD = (By.CSS_SELECTOR, "input[name='name'][value]+.chakra-form__error-message")
    MODAL_VALIDATION_PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price'][value]+.chakra-form__error-message")
    MODAL_VALIDATION_DESCRIPTION_FIELD = (By.CSS_SELECTOR, "input[name='description'][value]+.chakra-form__error-message")
    MODAL_VALIDATION_IMAGE_URL_FIELD = (By.CSS_SELECTOR, "input[name='imageUrl'][value]+.chakra-form__error-message")

    
    def search_ad(self, search_text):
        """ 
        Поиск объявления в каталоге по названию
        """
        self.input_text(self.CTLG_SEARCH_FIELD, search_text)
        self.click(self.CTLG_SEARCH_BUTTON)
    
    def get_ad_name(self):
        """
        Получение названия объявления из каталога
        """
        card_name_element = self.find_element(self.CTLG_AD_NAME)
        return card_name_element.text
        
    def open_ad_page(self, ad_name):
        """
        Открытие карточки объявления
        """
        ad_link = (By.XPATH, f"//a//h4[contains(text(), '{ad_name}')]")
        self.click(ad_link)
        return AdPage(self.driver) 
        
        
    """ Методы для работы с модальным окном создания объявления """
    
    def open_widget_for_create_new_ad(self):
        self.click(self.CTLG_CREATE_BUTTON)
    
    def enter_name(self, name):
        self.input_text(self.MODAL_NAME_FIELD, name)
        
    def enter_price(self, price):
        self.input_text(self.MODAL_PRICE_FIELD, price)
        
    def enter_description(self, description):
        self.input_text(self.MODAL_DESCRIPTION_FIELD, description)
        
    def enter_image_url(self, image_url):
        self.input_text(self.MODAL_IMAGE_URL_FIELD, image_url)
        
    def click_submit_button(self):
        self.click(self.MODAL_SUBMIT_BUTTON)
        
    def is_modal_displayed(self):
        """
        Проверка отображения модального окна
        """
        try: 
            self.find_element(self.MODAL_WINDOW)
            return True
        except NoSuchElementException:
            return False
    
    
    """ Методы проверки валидации полей модального окна создания объявления """
    
    def is_validation_name_field(self):
        try:
            self.find_element(self.MODAL_VALIDATION_NAME_FIELD)
            return True
        except NoSuchElementException:
            return False

    def is_validation_price_field(self):
        try:
            self.find_element(self.MODAL_VALIDATION_PRICE_FIELD)
            return True
        except NoSuchElementException:
            return False

    def is_validation_description_field(self):
        try:
            self.find_element(self.MODAL_VALIDATION_DESCRIPTION_FIELD)
            return True
        except NoSuchElementException:
            return False

    def is_validation_image_url_field(self):
        try:
            self.find_element(self.MODAL_VALIDATION_IMAGE_URL_FIELD)
            return True
        except NoSuchElementException:
            return False
