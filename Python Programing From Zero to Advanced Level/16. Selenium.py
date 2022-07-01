import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

# url="https://www.youtube.com/"
# driver.get(url)
# time.sleep(2)
# driver.maximize_window()
# # driver.save_screenshoot("youtubehomepage.png")
# time.sleep(5)
# print(driver.title)
# url="https://www.sabah.com.tr/"
# driver.get(url)
# if "Sabah" in (driver.title).split():
#     driver.save_screenshot("sabah.png")
# time.sleep(4)
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(2)
# print(driver.title)
# time.sleep(2)
# driver.close()

url="http://github.com"
driver.get(url)
searchinput=driver.find_element_by_name("q")
#or with xpath
#searchinput=driver.find_element_by_xpath("/html/body/div[1]/header/div[3]/div/div/form/label/input[1]")

time.sleep(1)
searchinput.send_keys("python")
time.sleep(1)
searchinput.send_keys(Keys.ENTER)
time.sleep(1)
repolist=driver.find_elements_by_css_selector(".repo-list-item a")

for element in repolist:
    print(element.text)

#sayfa kaynağına ulaşmak için
result=driver.page_source
print(result)

driver.close()


action=webdriver.ActionChains(driver)
action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform() #to scroll down

#Changing of browser language
browserProfile=webdriver.ChromeOptions()
browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
driver=webdriver.Chrome("chromedriver.exe",chrome_options=browserProfile)


