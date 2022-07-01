import os
import time

from pandas import isnull
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
un=os.getenv('username')
pw=os.getenv('password')

url="https://github.com/login"
driver.get(url)
# time.sleep(1)
driver.maximize_window()
# time.sleep(1)
uninput=driver.find_element_by_name("login")
uninput.send_keys(un)
# time.sleep(1)
pwinput=driver.find_element_by_name("password")
pwinput.send_keys(pw)
# time.sleep(1)
singinbutton=driver.find_element_by_name("commit")
singinbutton.click()
time.sleep(15)
avatarbutton=driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/span[2]")
avatarbutton.click()
time.sleep(1)
yourprofile=driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[1]")
yourprofile.click()
# time.sleep(1)
following=driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[2]')
following.click()
# time.sleep(1)
sadikturan=driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a/span[1]')
sadikturan.click()
# time.sleep(1)
stfollowing=driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]/span')
stfollowing.click()
time.sleep(3)
items=driver.find_elements_by_css_selector('.d-table.table-fixed')
print(items)
lst=[]
# # print(lst)
for i in items:
    lst.append(i.find_element_by_css_selector('.f4.Link--primary').text)
    time.sleep(1)
j=0
while j<=2:
    buttons=driver.find_element_by_class_name("pagination").find("a").find_elements_by_tag_name("a")
    print(buttons.text)
    if len(buttons) is 1: 
        if buttons[0].text is "Next":
           buttons[0].click()
           time.sleep(2)
           for i in items:
            lst.append(i.find_element_by_css_selector('.f4.Link--primary').text)
            time.sleep(1)
        else:
            break
    else:
        for button in buttons:
            if button.text is "Next":
                button.click()
                time.sleep(2)
                for i in items:
                    lst.append(i.find_element_by_css_selector('.f4.Link--primary').text)
                    time.sleep(1)
            else:
                continue
    j+=1    

for i in lst:
    if i== "" or i== '':
        lst.remove(i)

print(lst)
