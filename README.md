Readme for Free IPTV Auto

This Python script automates the process of obtaining a free trial of IPTV service and downloading the m3u file. It uses the Selenium library to automate web interactions and ChromeDriver to run the Chrome browser.
Prerequisites

This script requires the following libraries to be installed:

    selenium
    webdriver_manager
    csv

The Chrome browser and ChromeDriver must also be installed on the system.
How to use

    Clone or download the script to your local machine.
    Install the required libraries using pip.
    Ensure ChromeDriver is installed and the path is set correctly.
    Run the script using a Python interpreter.

What the script does

The script performs the following steps:

    Opens the website disposablemail.com to generate a temporary email address.
    Opens the IPTV free trial website and enters the generated email address to sign up for the trial.
    Opens the disposable email address website to confirm the email address.
    Downloads the m3u file using the generated email address.
    Renames the downloaded file to "iptv_daily_update.m3u".

The m3u file is downloaded to the "iptv_daily" directory in the current working directory. If a file with the name "iptv_daily_update.m3u" already exists in the directory, it is deleted and replaced with the new file.

Please note that this script is for educational purposes only and should not be used to engage in any illegal or unethical activities.
