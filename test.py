from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import random
import time


'''
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
#driver.get('https://web.whatsapp.com')
'''


fp = webdriver.FirefoxProfile('C:/Users/User/AppData/Roaming/Mozilla/Firefox/Profiles/119mkegb.default')

driver = webdriver.Firefox(executable_path='geckodriver.exe',firefox_profile=fp)
driver2 = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()
driver2.maximize_window()
#driver.get("https://web.whatsapp.com/")







driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard.html')

first_task_link = WebDriverWait(driver, 300,ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, '//div[@id="list-tasks-OVERDUE"]//div/label[@class="i-checks pull-left i-checks-sm"]')))
first_task_link.click()
    


#driver.implicitly_wait(3)
#crm_dashboard = driver.window_handles[0]

"""

first_task_link = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div/form/input[4]')))
#first_task_link= driver.find_element_by_xpath('//div[@class="task-related-to task-related-contacts"]/a')
first_task_link.click()
"""
"""
driver.get('https://dalilk4ielts.agilecrm.com/login#tasks')
#driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard.html')
time.sleep(5)


username = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div[1]/input')
time.sleep(1)
username.click()
time.sleep(1)
username.clear()
time.sleep(1)
username.send_keys('jabfjabjkdfbjdwbvf')
time.sleep(2)


password = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div[2]/input')
time.sleep(1)
password.click()
time.sleep(1)
password.clear()
time.sleep(1)
password.send_keys('sjfvbusvbfusfvb')
time.sleep(2)

login = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/input[4]')
login.click()

time.sleep(15)


task_page1= driver.find_element_by_xpath('//*[@id="tasksmenu"]/a')
task_page1.click()

time.sleep(5)

crm_dashboard = driver.window_handles[0]

time.sleep(1)

driver.execute_script("window.open()")

time.sleep(2)

driver.get('https://web.whatsapp.com/')

time.sleep(1)

whatsapp_page = driver.window_handles[1]

time.sleep(30)


"""


#driver.switch_to.window(whatsapp_page)




#my_str = '—asasas—'
#my_str.replace(b'\xe2\x80\x94'.decode('utf-8'), '-')

"""

driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard.html')

task_complete = driver.find_element_by_xpath('//div[@class="notes-pre"]/pre')

task_text = []
task_text = task_complete.text
task_text = task_text.replace(b'\xe2\x80\x94'.decode('utf-8'), '---')  
dash = "-"
dash2 = "."  




task_send = []
 
if dash in task_text:
    for character in dash:
        task_send= task_text.replace(character,"")

    print(task_send)
    task_send= task_send.split("\n\n")

elif dash2 in task_text:
    for character in dash2:
        task_send= task_text.replace(character,"")

    print(task_send)
    task_send= task_send.split("\n\n")



else:
    task_send= [task_text]
    #task_send= task_send.insert(0,"\n\n\n")
    #task_send = task_send.split("\n\n\n")
    #task_send = task_send[1]
    #task_send =  task_send[0]
    print('task_send',task_send)


driver.execute_script("window.open()")
time.sleep(3)

whatsapp_page = driver.window_handles[1]
driver.switch_to.window(whatsapp_page)
driver.get('https://www.google.com/')

message_box=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

time.sleep(random.randint(1, 2))
message_box.click()
time.sleep(random.randint(1, 2))
message_box.clear()
time.sleep(random.randint(1, 2))

print('first',task_send[0],task_send[0].isspace())
print('second',task_send[1],task_send[1].isspace())

counter =0
for message in range(len(task_send)):
    if task_send[message] == "":
        message+=1
    else:
        message_box.click()
        time.sleep(random.randint(1, 2))
        message_box.clear()
        time.sleep(random.randint(1, 2))
        message_box.send_keys(task_send[message])
        print(task_send[message])
        counter += 1
        print('count',counter)


"""

'''
phone_num= driver.find_element_by_xpath('//div[@class="contact-make-call-div"]/a')

num_send = phone_num.text

contact_complete= driver.find_element_by_xpath('//div[@class="contact-phone"]')
contact_split=contact_complete.text



if '+' in num_send:
    if len(contact_split) >= 35:
        contact_name= driver.find_element_by_xpath('//*[@id="contactName"]')
        contact_name=contact_name.text
        num_send=contact_name
        print('contact_name',num_send)

    else:
        num_send= num_send.split()
        num_send=num_send[0]
        print('phone_num',num_send)
else:    
    contact_name= driver.find_element_by_xpath('//*[@id="contactName"]')
    contact_name=contact_name.text
    num_send=contact_name
    print('contact_name',num_send)

driver.execute_script("window.open()")

whatsapp = driver.window_handles[1]
driver.switch_to.window(whatsapp)
driver.get('https://web.whatsapp.com')



time.sleep(5)


search_whatsapp=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

time.sleep(random.randint(1, 2))
search_whatsapp.click()
time.sleep(random.randint(1, 2))
search_whatsapp.clear()
time.sleep(random.randint(1, 2))
search_whatsapp.send_keys(num_send)

#select_sender = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div')
time.sleep(random.randint(3,4))

'''

#time.sleep(10)







print('end of code')