from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import csv
import threading
import pyperclip


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("--disable-gpu")

def who():
    global company, email, zipcode, first, last, job, phone, street_address, macos, state, ios
    company = open('company.csv').read().splitlines()
    company =random.choice(company)
    print(company)
    if " " in company:
        company = company.split(" ")
        company = company[0]
        print(company)
    else:
        pass
    print(company)

    zipcode = open('zipcode.csv').read().splitlines()
    zipcode =random.choice(zipcode)
    zipcode = zipcode.split(",")
    state = zipcode[1]
    zipcode = zipcode[0]
    print(zipcode)
    print(state)

    first = open('firstnames.txt').read().splitlines()
    first =random.choice(first)
    print(first)

    last = open('last.csv').read().splitlines()
    last =random.choice(last)
    print(last)
    url = [".com", ".org", ".net", ".co", ".ai", ".io"]
    url = random.choice(url)

    email = [f'{first}{last}@{company}{url}', f'{first[0]}{last}@{company}{url}', f"{first[0]}{last[0]}@{company}{url}", f"{last[0]}{first}@{company}{url}", f"{first}@{company}{url}" ]
    email = random.choice(email)
    print(email)

    phone = random.randint(1111111111,9999999999)
    print(phone)

    job = ["Ceo", "COO", "Head of Security", "Business Manager", "Security Officer", "CFO", "Admin", "HR Manager", "IT Manager", "Director of IT", "Director of Security", "Information Security Analyst", "Network Security Administrator", "Cyber Crime Investigator", "Network Security Engineer", "Security Manager"]
    job = random.choice(job)
    print(job)

    street_address_number = str(random.randint(1,2000))
    street_address = street_address_number + " " + company
    ios = random.randint(10, 2000)

class kandji_spam:
 
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/zacnicholson/Documents/GitHub/kandji spam/chromedriver', options=chrome_options) #, options=chrome_options

    def free_trial(self):
            ### Order free IPTV
            self.driver.get("https://best-usa-hosting.com/index.php?rp=/store/free-24hr-trials-hosting")
            sleep(5)
            order_now = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div/div/div/div[2]/div[3]/div/div/div/strong/footer/a')
            order_now.click()
            sleep(5)
            check_out = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/div[3]/div[2]/div/div[2]/div[5]/a[1]')
            check_out.click()



            ### Fill out into 
            first_field = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[3]/div[1]/div/input')
            first_field.send_keys(first)
            last_field = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[3]/div[2]/div/input')
            last_field.send_keys(last)
            email_field = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[3]/div[3]/div/input')
            email_field.send_keys(email)
            phone_number = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[3]/div[4]/div/div/input')
            phone_number.send_keys(phone)
            street_name = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[5]/div[2]/div/input')
            street_name.send_keys(street_address)
            city = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[5]/div[4]/div/input')
            city.send_keys('Austin')
            zip_code = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[5]/div[6]/div/input')
            zip_code.send_keys(zipcode)
            state2 = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[2]/div[5]/div[5]/div/select')
            state2.send_keys(state)
            password = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[3]/div[2]/div[2]/div/input')
            password.send_keys('mypa!&ssword')
            password_confirm = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[3]/div[2]/div[3]/div/input')
            password_confirm.send_keys('mypa!&ssword')
            approve_terms = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[13]/p/label/div/ins').click()
            complete_order = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[1]/div/div/div[2]/form/div[13]/button').click()

            self.driver.get('https://best-usa-hosting.com/clientarea.php?action=services')
            sleep(3)
            my_iptv = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/div[1]/table/tbody/tr[1]')
            my_iptv.click()
            sleep(2)
            iptv_details = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/div/div[5]/div[1]/form/button')
            iptv_details.click()
            # iptv_link = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/div[3]/div[2]/div[2]/button')
            # iptv_link.click()
            iptv_link = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/center/a')
            save_link = iptv_link.get_attribute('href')
            with open('iptv_daily_update', "w") as o:
                o.write(save_link)



            print("finished")
            sleep(6)

            






def do_requests():
        who()
        bot = kandji_spam()
        bot.free_trial()

do_requests()

