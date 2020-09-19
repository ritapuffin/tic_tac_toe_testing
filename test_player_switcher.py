# Pull request

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def is_child_exists(names, session, child_name):
    for name in names:
        element = session.find_element(By.CSS_SELECTOR,
                                       "div[class='" + name + "']")  # ищем элемент с очередным именем класса
        if element.find_elements(By.CSS_SELECTOR,
                                 "div[class='" + child_name + "']"):  # проверяем, что список элементов-детей с заданным именем не пуст
            return True  # так как мы нашли элемент, можем сразу вернуть True и дальше не проверять
    return False  # если мы дошли до конца списка names, а нужный элемент-ребёнок так и не нашёлся, придётся вернуть False


def assert_true(statement, text):
    if not statement:
        print(text)
        return False
    return True


squares = (
'square top left', 'square top', 'square top right', 'square left', 'square', 'square right', 'square bottom left',
'square bottom', 'square bottom right')

# Тестовый случай №1: проверка начального состояния
browser = webdriver.Chrome()
browser.get('https://playtictactoe.org/')  # открыть страницу https://playtictactoe.org/
# проверить, что на странице есть элемент с классом  ‘scores p1’
assert_true(browser.find_element(By.CSS_SELECTOR, "div[class='scores p1']"), "TestCase #1: No element 'scores p1'!")
# проверить, что на странице нет элемента с классом  ‘scores p2’ (т.е. список элементов с классом  ‘scores p2’ пуст)
assert_true(not browser.find_elements(By.CSS_SELECTOR, "div[class='scores p2']"),
            "TestCase #1: There is element 'scores p2' on the page!")
# проверить, что на странице элементов из множества squares нет элементов-детей с классом “о”
assert_true(not is_child_exists(squares, browser, 'o'), "TestCase #1: There is O element!")
# проверить, что на странице элементов из множества squares нет элементов-детей с классом “х”
assert_true(not is_child_exists(squares, browser, 'x'), "TestCase #1: There is X element!")

# Тестовый случай №2: переключение
# нажать на элемент с именем класса swap
browser.find_element(By.CLASS_NAME, 'swap').click()
# проверить, что исчез элемент с классом  ‘scores p1’
assert_true(not browser.find_elements(By.CSS_SELECTOR, "div[class='scores p1']"),
            "TestCase #2: There is element 'scores p1' on the page!")
# проверить, что появился элемент с классом  ‘scores p2’
assert_true(browser.find_element(By.CSS_SELECTOR, "div[class='scores p2']"), "TestCase #2: No element 'scores p2'!")
# проверить, что на странице элементов из множества squares нет элементов-детей с классом “о”
assert_true(not is_child_exists(squares, browser, 'o'), "TestCase #2: There is O element!")
# проверить, что на странице элементов из множества squares нет элементов-детей с классом “х”
assert_true(not is_child_exists(squares, browser, 'x'), "TestCase #2: There is X element!")

# Тестовый случай №3: обратное переключение
# нажать на элемент с именем класса swap
browser.find_element(By.CLASS_NAME, 'swap').click()
# проверить, что исчез элемент с классом  ‘scores p2’
assert_true(not browser.find_elements(By.CSS_SELECTOR, "div[class='scores p2']"),
            "TestCase #3: There is element 'scores p2' on the page!")
# проверить, что появился элемент с классом  ‘scores p1’
assert_true(browser.find_element(By.CSS_SELECTOR, "div[class='scores p1']"), "TestCase #3: No element 'scores p1'!")
# проверить, что в одном из элементов множества squares есть элемент-ребёнок с именем класса ‘o’
time.sleep(2)
assert_true(is_child_exists(squares, browser, 'o'), "TestCase #3: There is no O element!")
# проверить, что ни в одном из элементов множества squares нет элемента-ребёнка с именем класса ‘x’
assert_true(not is_child_exists(squares, browser, 'x'), "TestCase #3: There is X element!")

browser.quit()
