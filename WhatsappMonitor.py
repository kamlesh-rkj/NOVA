from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  
from playsound import playsound
import time
import sys

name = sys.argv[1]
print(name)
def MonitorPerson():
    # Replace with the path to your ChromeDriver executable
    webdriver_service = Service('C://Users//rkjrk//Downloads//chromedriver_win32//chromedriver-win64//chromedriver.exe')

    # Replace with the path to your Chrome profile
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C://Users//rkjrk//AppData//Local//Google//Chrome//User Data//Default")
    chrome_options.add_argument("--disable-gpu")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Replace with the name of the person you want to monitor
    target_person = f"{name}".strip()

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # # Wait for the user to scan the QR code and log in
    # input("Press Enter after scanning the QR code and logging in...")
    for i in range(0,60):
        print(i)
        time.sleep(1)
    # Find the chat of the target person
    chat_xpath = f"//span[@title='{target_person}']"
    chat_element = driver.find_element(By.XPATH, chat_xpath)
    # Click on the chat element
    print(chat_element)
    chat_element.click()
    # Check the online status of the target person
    body_xpath=f"//span[@title='online']"
    # body_element = driver.find_element(By.XPATH,body_xpath)
    while True:
        # online_status = chat_element.get_attribute("aria-label")
        # if online_status == "online":
        #     print(f"{target_person} is online!")
        #     playsound("C://Users//rkjrk//Downloads//videoplayback.mp3")  # Replace with the path to your alert alarm sound file
        #     break
        try:
            body_element = driver.find_element(By.XPATH,body_xpath)
            print(f"{target_person} is online!")
            # Replace with the path to your alert alarm sound file
            break
        except:
            print(f"{target_person} is offline!")
            time.sleep(1)

    # Close the browser
    driver.quit()