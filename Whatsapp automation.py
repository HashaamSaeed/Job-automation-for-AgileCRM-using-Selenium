from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import random
import time







## for login page needs to be that specific page 
############################################################################################################################

#driver = webdriver.Chrome(executable_path='chromedriver')
#driver.maximize_window()

options = webdriver.FirefoxOptions()
options.add_argument(r"user-data-dir=./driver/data")
driver = webdriver.Firefox(executable_path='geckodriver', options=options)
driver.maximize_window()
#driver.get('https://web.whatsapp.com/')




driver.get('https://dalilk4ielts.agilecrm.com/login#tasks')
#driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard.html')
time.sleep(10)


username = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div[1]/input')
time.sleep(2)
username.click()
time.sleep(2)
username.clear()
time.sleep(2)
username.send_keys('jbfbbfubeebfwb')
time.sleep(2)


password = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/div[1]/div[2]/input')
time.sleep(2)
password.click()
time.sleep(2)
password.clear()
time.sleep(2)
password.send_keys('eklfnefgnwelgwegb')
time.sleep(2)

login = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/input[4]')
login.click()

time.sleep(20)


crm_dashboard = driver.window_handles[0]

time.sleep(3)

driver.execute_script("window.open()")
time.sleep(3)

whatsapp_page = driver.window_handles[1]
time.sleep(3)

driver.switch_to.window(whatsapp_page)

time.sleep(5)

driver.get('https://web.whatsapp.com/')

time.sleep(30)






############################################################################################################################

count = 0

while True:
    ## Task access 
    ############################################################################################################################

    time.sleep(3)

    crm_dashboard = driver.window_handles[0]

    time.sleep(3)

    driver.switch_to.window(crm_dashboard)

    #tasks = driver.find_elements_by_id('task-model-list')    ## complete list of tasks selected
    #print('task 0 here',tasks[0].text)
    #print('task 1 here',tasks[1].text)



    time.sleep(random.randint(3,10))


    first_task_link= driver.find_element_by_xpath('//div[@class="task-related-to task-related-contacts"]/a')
    first_task_link.click()


    time.sleep(15)

    contact_page = driver.window_handles[0]
    time.sleep(3)

    notes_contact = driver.find_element_by_xpath('//*[@id="contactDetailsTab"]/li[2]/a') ## selecting "Notes" when task is clicked
    notes_contact.click()


    ############################################################################################################################



    ## Data scrapping
    ############################################################################################################################



    #driver.get('file:///C:/Users/User/Desktop/Agile CRM Dashboard-contact.html')

    time.sleep(10)

    tag_text= driver.find_element_by_xpath('//div[@class="contact-tags"]')
    tag_text= tag_text.text

    if 'No WhatsApp' in tag_text:

            task_page= driver.find_element_by_xpath('//*[@id="tasksmenu"]/a')
            task_page.click()

            time.sleep(20)

            task_done= driver.find_element_by_xpath('//div/label[@class="i-checks pull-left i-checks-sm"]')
            task_done.click()

            time.sleep(5)

            driver.refresh()
            time.sleep(20)
            count = count + 1
            print('Number of tasks completed are = ',count)



            ############################################################################################################################

    else:
            #phone_num= driver.find_element_by_xpath('//*[@id="contact-details-block"]/div/div/div/div/div/div[1]/div/div/div[11]/div[1]/div[3]/div/a')    ## phone number
            phone_num= driver.find_element_by_xpath('//div[@class="contact-make-call-div"]/a')

            num_send = phone_num.text
            num_send= num_send.split()
            print('phone_num',num_send[0])




            #task_complete = driver.find_element_by_xpath('//*[@id="notes-model-list"]/li[1]/div/div[2]/div[4]/div/pre')
            task_complete = driver.find_element_by_xpath('//div[@class="notes-pre"]/pre')

            task_text = []
            task_text = task_complete.text
            dash = "--------"
            dash2 = ".........."
            dash3 = "..........."
            if dash in task_text:
                #task_send = task_text.replace("--------", "")
                task_send = task_text.split('--------') 
                print('task_send',task_send)
            elif dash2 in task_text:
            	task_send = task_text.split('..........') 
            	print('task_send',task_send)
            elif dash3 in task_text:
            	task_send = task_text.split('...........') 
            	print('task_send',task_send)
            else:
                task_send = task_text
                print('task_send',task_send)



            ############################################################################################################################


            ##Whatsapp automation
            ############################################################################################################################


            time.sleep(3)

            driver.switch_to.window(whatsapp_page)

            #num_send = "+923002885997"
            #task_send= []
            #task_send= "1"

            time.sleep(random.randint(3,7))


            search_whatsapp=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

            time.sleep(random.randint(1, 2))
            search_whatsapp.click()
            time.sleep(random.randint(1, 2))
            search_whatsapp.clear()
            time.sleep(random.randint(1, 2))
            search_whatsapp.send_keys(num_send[0],Keys.ENTER)

            #select_sender = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div')
            time.sleep(random.randint(2,5))


            message_box= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            #/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]
            time.sleep(random.randint(1, 2))
            message_box.click()
            time.sleep(random.randint(1, 2))
            message_box.clear()
            time.sleep(random.randint(1, 2))


            for message in range(len(task_send)):
                message_box.click()
                time.sleep(random.randint(1, 2))
                message_box.clear()
                time.sleep(random.randint(1, 2))
                message_box.send_keys(task_send[message])
                time.sleep(random.randint(2, 5))
                send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                time.sleep(random.randint(1, 2))
                send_button.click()



            ############################################################################################################################


            ## Click task done
            ############################################################################################################################
            time.sleep(3)
            driver.switch_to.window(contact_page)
            time.sleep(3)

            task_page= driver.find_element_by_xpath('//*[@id="tasksmenu"]/a')
            task_page.click()

            time.sleep(20)

            task_done= driver.find_element_by_xpath('//div/label[@class="i-checks pull-left i-checks-sm"]')
            task_done.click()

            time.sleep(5)

            driver.refresh()
            time.sleep(20)
            count = count + 1
            print('Number of tasks completed are = ',count)



            ############################################################################################################################



print('Program either ended because tasks are finished or there is an error somehwhere and you might need to restart the whole program \
	   BUT FIRST PLEASE DO THE TASK IT WAS STUCK ON YOURSELF which is the first one in the overdue task list ')


    



'''
for task in driver.find_elements_by_xpath('//*[@id="task-model-list"]'):
    print('task is here',task.text)
    for t in task.find_elements_by_xpath('//*[@id="task-model-list"]/div[2]'):
        print('t is here ',t.text)
        url = t.find_elements_by_xpath('/html/body/div[8]/div[1]/div[5]/div/div/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]')
        for u in url:
            print('url is here',u.text)
            link = u.find_element_by_partial_link_text('#con').click()
            print('link is here',link.text)
            #print(link.text)

'''