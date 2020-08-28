from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://playtictactoe.org/')
link_to_catalog = browser.find_element(By.CLASS_NAME, 'neave')
if not link_to_catalog:
    print('Empty link in "neave" element!')
    browser.quit()

link_URL = link_to_catalog.get_attribute('href')
link_to_catalog.click()

opened_URL = browser.current_url
try:
    assert opened_URL == link_URL
except AssertionError as error:
    print('Click on {} link, but get {} URL!'.format(link_URL, opened_URL))

opened_page_title = browser.title
try:
    assert opened_page_title == 'Neave Interactive'
except AssertionError as error:
    print('Click on {} link, but get wrong title:{}!'.format(link_URL, opened_page_title))

browser.back()
opened_URL = browser.current_url
try:
    assert opened_URL == 'https://playtictactoe.org/'
except AssertionError as error:
    print('Click back on the catalog page, but {} opened!'.format(opened_URL))

browser.quit()