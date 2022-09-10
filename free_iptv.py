from genericpath import isfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import csv
import threading
import os
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("--disable-gpu")
prefs = {'download.default_directory' : 'iptv_daily'}
chrome_options.add_experimental_option('prefs', prefs)



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

            ##Open New tab for free iptv
            self.driver.get('https://iptv-best.net/free-2-day-trial/')
            input_email = self.driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div[1]/div/div/div/div[2]/div/div/form/div[2]/div[2]/input')
            input_email.send_keys(get_email)
            submit = self.driver.find_element_by_xpath('/html/body/div[1]/div/main/section/div/div/div[1]/div/div/div/div[2]/div/div/form/div[3]/button')
            submit.click()

            ### Open Tab to email confirmation
            sleep(10)
            self.driver.get('https://www.disposablemail.com/window/id/2')
            sleep(5)



            ###Downloading the m3u
            self.driver.get(f'http://tv4k.me/get.php?username={get_email}&password=500100&type=m3u_plus&output=ts')
            sleep(3)
            print(f'downloaded started. file name is http://tv4k.me/get.php?username={get_email}&password=500100&type=m3u_plus&output=ts')
            sleep(120)
            if os.path.isfile("iptv_daily/iptv_daily_update.m3u"):
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
        bot = free_iptv_auto()
        bot.free_trial()

do_requests()

