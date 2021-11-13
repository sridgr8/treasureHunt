from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

def startExecution():
    time.sleep(2)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://54.80.137.197:5000/")

def pageOne():
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/a[2]/img").click()

def pageTwo():
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='start']").click()

def pageThree():
    time.sleep(2)
    for btn in driver.find_elements(By.XPATH, "//*[contains(@id,'c1submitbutton')]"):
        try:
            btn.click()
        except:
            print("Correct btn was clicked.")

def pageFour():#in progress
    time.sleep(2)
    driver.execute_script('document.getElementsByTagName("video")[0].play()')
    time.sleep(2)

def close_driver():
    time.sleep(2)
    # Close ChromeDriver
    print("Closing ChromeDriver")
    driver.quit()

print("Execution Started")
driver = webdriver.Chrome(executable_path="./webDrivers/chromedriver")

startExecution()
pageOne()

pageTwo()

pageThree()

pageFour()

close_driver()
print("Execution Completed.")
