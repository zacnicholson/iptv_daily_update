from genericpath import isfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
import csv
import threading
import os
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("--disable-gpu")
prefs = {'download.default_directory' : 'iptv_daily'}
chrome_options.add_experimental_option('prefs', prefs)

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

    # job = ["Ceo", "COO", "Head of Security", "Business Manager", "Security Officer", "CFO", "Admin", "HR Manager", "IT Manager", "Director of IT", "Director of Security", "Information Security Analyst", "Network Security Administrator", "Cyber Crime Investigator", "Network Security Engineer", "Security Manager"]
    # job = random.choice(job)
    # print(job)

    street_address_number = str(random.randint(1,2000))
    street_address = street_address_number + " " + company
    # ios = random.randint(10, 2000)

class free_iptv_auto:
 
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


    def free_trial(self):
        ## Open tempmail
            self.driver.get("https://www.disposablemail.com/")
            sleep(5)
            get_email = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div[5]/span')
            get_email = get_email.text
            print(get_email)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
            sleep(5)


            ## Order free IPTV
            self.driver.get("https://free.viewsible.com/trial")
            sleep(5)
            select_m3u = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div[2]/form/div/div[1]/div[4]/div[1]/select/option[2]')
            select_m3u.click()
            yes_usa = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div[2]/form/div/div[1]/div[4]/div[6]/select/option[2]')
            yes_usa.click()
            continue_button = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div[2]/form/div/div[2]/div/div[2]/button')
            continue_button.click()
            sleep(2)
            checkout = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[5]/a[1]')
            checkout.click()






            email_field = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div/form/div[2]/div[3]/div[3]/div/input')
            email_field.send_keys(get_email)
            first_field = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div/form/div[2]/div[3]/div[1]/div/input')
            first_field.send_keys(first)
            last_field = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div/form/div[2]/div[3]/div[2]/div/input')
            last_field.send_keys(last)
            generate_password = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div/form/div[3]/div[2]/div[2]/div/input')
            generate_password.send_keys('pass!diek83')
            generate_password_confirm = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div/form/div[3]/div[2]/div[3]/div/input')
            generate_password_confirm.send_keys('pass!diek83')
            submit = self.driver.find_element_by_xpath('/html/body/section[3]/div/div/div[1]/div/div/div/form/div[13]/button')
            submit.click()
            sleep(15)

            ### Open Tab to email confirmation
            self.driver.get("https://www.disposablemail.com/")

            sleep(360)
            self.driver.get('https://www.disposablemail.com/window/id/3')
            try:
                username = self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/table[1]/tbody/tr/td/div[4]/blockquote/p[6]').text
                print(username)
                print('firstone')
            except:
                username = self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr/td/table[1]/tbody/tr/td/div[4]/blockquote/p[6]').text()
                print(username)
                print('secondone')
            


            

            ###Downloading the m3u
            self.driver.get('https://best-usa-hosting.com/clientarea.php?action=services')
            sleep(3)
            my_iptv = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/div[1]/table/tbody/tr[1]')
            my_iptv.click()
            sleep(2)
            iptv_details = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/div/div[5]/div[1]/form/button')
            iptv_details.click()
            iptv_link = self.driver.find_element_by_xpath('/html/body/center/font/b/center/center/center/center/center/center/section[3]/div/div/div[3]/div/div[1]/center/a')
            save_link = iptv_link.get_attribute('href')
            self.driver.get(save_link)
            print(f'downloaded started. file name is {save_link}')
            sleep(120)
            if os.path.isfile("busa.one*"):
                os.remove("iptv_daily/iptv_daily_update.m3u")
                print('file removed')
                folder = r'iptv_daily/'
                count = 1
                # count increase by 1 in each iteration
                # iterate all files from a directory
                for file_name in os.listdir(folder):
                    # Construct old file name
                    source = folder + file_name

                    # Adding the count to the new file name and extension
                    destination = folder + "iptv_daily_update.m3u"

                    # Renaming the file
                    os.rename(source, destination)
                    count += 1

                print('New Names are')
                # verify the result
                res = os.listdir(folder)
                print(res)
                print("finished")

            else:
                print('no change')
                pass
            
            






def do_requests():
        who()
        bot = free_iptv_auto()
        bot.free_trial()

do_requests()

