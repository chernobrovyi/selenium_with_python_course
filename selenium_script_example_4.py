from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link_1 = "http://suninjuly.github.io/find_link_text";
# link_2 = "http://suninjuly.github.io/simple_form_find_task.html";

try:
    browser = webdriver.Chrome();
    browser.get(link_1);

    link = browser.find_element(By.LINK_TEXT, "224592");
    link.click();

    # browser.get(link_2);

    input1 = browser.find_element(By.NAME, 'first_name');
    input1.send_keys("Valeriy");
    input2 = browser.find_element(By.NAME, 'last_name');
    input2.send_keys("Chernobrovyi");
    input3 = browser.find_element(By.CLASS_NAME, 'city');
    input3.send_keys("Taganrog");
    input4 = browser.find_element(By.ID, "country");
    input4.send_keys("Russia");
    button = browser.find_element(By.CSS_SELECTOR, "button.btn");
    button.click();

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(60);
    # закрываем браузер после всех манипуляций
    browser.quit();

# не забываем оставить пустую строку в конце файла