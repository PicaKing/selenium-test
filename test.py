import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.instagram.com")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

input("test")


# def update():
#     i = 0
#     while i < 10:
#         main = driver.find_element_by_tag_name('main')
#         main.send_keys(Keys.END)
#         time.sleep(3)


elems = driver.find_elements_by_class_name("FFVAD")

for elem in elems:
    print(elem.get_attribute("src"))
# assert "Python" in driver.title

# a = input("prompt")

# if a == "1":
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
# if a == "2":


# elems = driver.find_elements_by_class_name("button")
# elems.pop().click()
