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







## for login page needs to be that specific page 
############################################################################################################################

#driver = webdriver.Chrome(executable_path='chromedriver')
#driver.maximize_window()

fp = webdriver.FirefoxProfile('C:/Users/User/AppData/Roaming/Mozilla/Firefox/Profiles/119mkegb.default')
driver = webdriver.Firefox(executable_path='geckodriver.exe',firefox_profile=fp)
driver.maximize_window()


#driver.get('https://web.whatsapp.com/')




driver.get('https://dalilk4ielts.agilecrm.com/login#tasks')
#driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard.html')
time.sleep(5)


username = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div[1]/input')
time.sleep(1)
username.click()
time.sleep(1)
username.clear()
time.sleep(1)
username.send_keys('sjkbfbwsfbfjbjfb')
time.sleep(2)


password = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div[2]/input')
time.sleep(1)
password.click()
time.sleep(1)
password.clear()
time.sleep(1)
password.send_keys('wjf fvbwjvf bjkwf')
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

whatsapp_page = driver.window_handles[1]
time.sleep(1)

driver.switch_to.window(whatsapp_page)

time.sleep(2)

driver.get('https://web.whatsapp.com/')

time.sleep(60)






############################################################################################################################

count = 0

while True:
    ## Task access 
    ############################################################################################################################

    time.sleep(1)

    #crm_dashboard = driver.window_handles[0]

    #time.sleep(1)

    driver.switch_to.window(crm_dashboard)

    #tasks = driver.find_elements_by_id('task-model-list')    ## complete list of tasks selected
    #print('task 0 here',tasks[0].text)
    #print('task 1 here',tasks[1].text)



    time.sleep(1)



    #first_task_link= driver.find_element_by_xpath('//div[@class="task-related-to task-related-contacts"]/a')
    first_task_link = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="list-tasks-OVERDUE"]//div[@class="task-related-to task-related-contacts"]/a')))
    first_task_link.click()
    



    time.sleep(1)

    #contact_page = driver.window_handles[0]
    #time.sleep(2)

    #notes_contact = driver.find_element_by_xpath('//*[@id="contactDetailsTab"]/li[2]/a') ## selecting "Notes" when task is clicked
    notes_contact = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contactDetailsTab"]/li[2]/a')))
    notes_contact.click()



    ############################################################################################################################



    ## Data scrapping
    ############################################################################################################################



    #driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard-contact.html')

    time.sleep(4)

    tag_text= driver.find_element_by_xpath('//div[@class="contact-tags"]')
    tag_text= tag_text.text

    if 'No WhatsApp' in tag_text:

            #task_page= driver.find_element_by_xpath('//*[@id="tasksmenu"]/a')
            task_page = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tasksmenu"]/a')))
            task_page.click()

            time.sleep(1)

            #task_done= driver.find_element_by_xpath('//div/label[@class="i-checks pull-left i-checks-sm"]')
            task_done = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, '//div[@id="list-tasks-OVERDUE"]//div/label[@class="i-checks pull-left i-checks-sm"]')))
            task_done.click()

            time.sleep(5)

            #calender= WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendarmenu"]/a')))
            #calender.click()

            driver.refresh()

            time.sleep(1)


            task_page = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tasksmenu"]/a')))
            task_page.click()


            #driver.refresh()
            time.sleep(1)
            count = count + 1
            print('Number of tasks completed are = ',count)



            ############################################################################################################################

    else:
            #phone_num= driver.find_element_by_xpath('//*[@id="contact-details-block"]/div/div/div/div/div/div[1]/div/div/div[11]/div[1]/div[3]/div/a')    ## phone number
            phone_num= driver.find_element_by_xpath('//div[@class="contact-make-call-div"]/a')

            num_send = phone_num.text


            contact_complete= driver.find_element_by_xpath('//div[@class="contact-phone"]')
            contact_split=contact_complete.text

            if '+' in num_send:
                if len(contact_split) >= 35:
                    contact_name= driver.find_element_by_xpath('//*[@id="contactName"]')
                    contact_name=contact_name.text
                    num_send=contact_name
                    #print('contact_name',num_send)

                else:
                    num_send= num_send.split()
                    num_send=num_send[0]
                    #print('phone_num',num_send)
            else:    
                contact_name= driver.find_element_by_xpath('//*[@id="contactName"]')
                contact_name=contact_name.text
                num_send=contact_name
                #print('contact_name',num_send)




            #task_complete = driver.find_element_by_xpath('//*[@id="notes-model-list"]/li[1]/div/div[2]/div[4]/div/pre')
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

            	#print(task_send)
            	task_send= task_send.split("\n\n")

            elif dash2 in task_text:
            	for character in dash2:
            		task_send= task_text.replace(character,"")

            	#print(task_send)
            	task_send= task_send.split("\n\n")

            else:
                task_send = [task_text]
                #print('task_send',task_send)


            time.sleep(1)

            #task_page= driver.find_element_by_xpath('//*[@id="tasksmenu"]/a')
            task_page = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tasksmenu"]/a')))
            task_page.click()

            time.sleep(1)




            ############################################################################################################################


            ##Whatsapp automation
            ############################################################################################################################


            time.sleep(1)

            driver.switch_to.window(whatsapp_page)

            #num_send = ""
            #task_send= []
            #task_send= "1"

            time.sleep(1)


            search_whatsapp=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

            time.sleep(1)
            search_whatsapp.click()
            time.sleep(1)
            search_whatsapp.clear()
            time.sleep(1)
            search_whatsapp.send_keys(num_send)

            #select_sender = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div')
            time.sleep(2)

            number_click= driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[2]')
            number_click.click()


            message_box= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            #/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]
            time.sleep(1)
            message_box.click()
            time.sleep(1)
            message_box.clear()
            time.sleep(1)


            for message in range(len(task_send)):
                if task_send[message] == "":
                    message+=1
                    
                else:
                    message_box.click()
                    time.sleep(1)
                    message_box.clear()
                    time.sleep(1)
                    message_box.send_keys(task_send[message])
                    time.sleep(1)
                    send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    time.sleep(2)
                    send_button.click()



            ############################################################################################################################


            ## Click task done
            ############################################################################################################################
            time.sleep(1)
            driver.switch_to.window(crm_dashboard)

            #task_done= driver.find_element_by_xpath('//div/label[@class="i-checks pull-left i-checks-sm"]')
            task_done = WebDriverWait(driver, 300,ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, '//div[@id="list-tasks-OVERDUE"]//div/label[@class="i-checks pull-left i-checks-sm"]')))
            task_done.click()

            time.sleep(7)

            driver.refresh()
            #calender= WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="calendarmenu"]/a')))
            #calender.click()

            time.sleep(1)

            task_page = WebDriverWait(driver, 300,poll_frequency=1,ignored_exceptions=StaleElementReferenceException).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tasksmenu"]/a')))
            task_page.click()

            time.sleep(1)


            count = count + 1
            print('Number of tasks completed are = ',count)

            ############################################################################################################################



print('Program either ended because tasks are finished or there is an error somehwhere and you might need to restart the whole program \
	   BUT FIRST PLEASE DO THE TASK IT WAS STUCK ON YOURSELF which is the first one in the overdue task list ')