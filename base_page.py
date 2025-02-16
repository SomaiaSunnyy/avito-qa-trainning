from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import time

class BasePage:
    """
    Класс базовой страницы
    ------
    Описаны основные методы для работы на наследуемых классах сраниц
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def open(self, url):
        self.driver.get(url)
        
    def find_element(self, selector):
        return self.driver.find_element(*selector)
    
    def is_element_visible(self, selector):
        return self.wait.until(expected_conditions.visibility_of_element_located((selector)))
        
    def is_element_interactable(self, selector):
        return self.wait.until(expected_conditions.element_to_be_clickable((selector)))


    def click(self, selector):
        """
        Нажатие на кнопку
        """
        try:
            element = self.is_element_interactable(selector)
            element.click()
            time.sleep(1) #Потом переделать
        except (ElementNotInteractableException, NoSuchElementException) as e:
            print(f"ОШИБКА: Кнопка с селектором --> {selector} <-- недоступна для взаимодействия или не найдена")
            raise e
        
    def input_text(self, selector, text):
        """ 
        Ввод текста в форму
        """
        try:
            element = self.is_element_interactable(selector)
            element.clear()
            element.send_keys(text)
        except (ElementNotInteractableException, NoSuchElementException) as e:
            print(f"ОШИБКА: поле для ввода с селектором --> {selector} <-- недоступно для взаимодействия или не найдено")
            raise e
    
