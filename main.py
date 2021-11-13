from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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

def pageFour():
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    time.sleep(9)
    print("Trying the move")
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div").click()
    # time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[2]/div").click()
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Mute (m)"]'))).click()
    time.sleep(3)
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "//*[@id='aVideoSubmit']").click()
    
def pageFive():#in progress
    time.sleep(20)
    
    

def move_Left():
    time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_back']").click()

def move_Right():
    time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_forward']").click()

def move_Up():
    time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_upward']").click()

def move_Down():
    time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_downward']").click()

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

pageFive()

close_driver()
print("Execution Completed.")
