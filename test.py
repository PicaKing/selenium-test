import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/abin_store")

#  // Login va Save
# a = input("prompt")
#
# if a == "1":
#     pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#

cookies = pickle.load(open("cookies.pkl", "rb"))  # load login
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

# def update():
#     i = 0
#     while i < 10:
#         main = driver.find_element_by_tag_name('main')
#         main.send_keys(Keys.END)
#         time.sleep(3)

following_cand = driver.find_elements_by_class_name("-nal3 ")
for cand in following_cand:
    if "following" in cand.text:
        cand.click()
        time.sleep(2)
        break

main = driver.find_element_by_class_name('isgrP')
driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', main)
time.sleep(1)
driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', main)
time.sleep(2)
driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', main)
time.sleep(2)
driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', main)
time.sleep(2)


def start_un_follow():
    elems = driver.find_elements_by_tag_name("button")
    for cand in elems:
        if "Following" in cand.text:
            cand.click()
            time.sleep(2)
            unfollow = driver.find_elements_by_xpath("//*[contains(text(), 'Unfollow')]")
            try:
                unfollow[1].click()
            except:
                unfollow[0].click()

            time.sleep(1)


i = 0
while (i != 5):
    try:
        main = driver.find_element_by_class_name('isgrP')
        driver.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight)', main)
        time.sleep(1)
        start_un_follow()
    except:
        i += 1
        continue

input("test")
# assert "Python" in driver.title


# if a == "2":
#
#
# elems = driver.find_elements_by_class_name("button")
# elems.pop().click()
