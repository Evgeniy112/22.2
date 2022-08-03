import pytest
from selenium import webdriver
from settings import valid_email, valid_password
import time

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys(valid_email)
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

   pytest.driver.find_element_by_link_text('Мои питомцы').clic()
   pets = pytest.find_element_by_teg_name('tr')
   my_pets_data = pytest.driver.find_element_by_class_name('\.col-sm-4.left')
   pets_string = my_pets_data.text.split(" ")
   pets_counter = pets_string[1]
   time.sleep(3)

         #Список функций, которые используются для множественного поиска
         # find_elements_by_name
         # find_elements_by_xpath
         # find_elements_by_link_text
         # find_elements_by_partial_link_text
         # find_elements_by_tag_name
         # find_elements_by_class_name
         # find_elements_by_css_selector
