from PIL.Image import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver import ActionChains
import time
import urllib
import numpy
# import pytesseract as tess
# import PIL from Image
from time import sleep

maze_List1 = [6,2,2,2,6,2,8,1,6,3,2,2,4,1,2,1,4,3,2,1,4,1,2,2,6,6,8,2,6,1,8,1,6,2]
maze_List2 = [6,2,2,1,6,2,8,3,4,2,8,2,6,1,8,2,6,2,2,3,6,2,2,4,6,1,2,1,6,3]
maze_List = []

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
            pass

def pageFour():
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://www.youtube.com/embed")]'))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Play"]'))).click()
    time.sleep(9)
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
    time.sleep(1)
    get_Matrix()

def make_List(l1):
    l1_copy =[]
    for item in l1: l1_copy.append(item)
    return l1_copy

def get_Matrix():
    time.sleep(1)
    if("green" in str((driver.find_element(By.XPATH, "//*[@id='maze']/tr[7]/td[12]").get_attribute("class")))):
        maze_List=make_List(maze_List1)
    else:
        maze_List=make_List(maze_List2)

    i = 0
    while i < (len(maze_List) - 1):
        # print(maze_List2[i])
        if(maze_List[i]==2):
            for _ in range(maze_List[i+1]):move_Down()
        elif(maze_List[i]==4):
            for _ in range(maze_List[i+1]):move_Left()
        elif(maze_List[i]==6):
            for _ in range(maze_List[i+1]):move_Right()
        elif(maze_List[i]==8):
            for _ in range(maze_List[i+1]):move_Up()
        i += 2
    driver.find_element(By.XPATH, "//*[@id='crystalMazeFormSubmit']").click()
    time.sleep(5)


def move_Left():
    # time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_back']").click()

def move_Right():
    # time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_forward']").click()

def move_Up():
    # time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_upward']").click()

def move_Down():
    # time.sleep(1)
    driver.find_element(By.XPATH, "//div/a/i[text()='arrow_downward']").click()

def pageSix():
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='OpenLayers_Layer_WMS_4']/img[2]").click()
    time.sleep(8)
    # driver.execute_script("document.getElementById('OpenLayers_Layer_WMS_4').value='i'")
    actions = ActionChains(driver)
    actions.send_keys('i')
    actions.perform()
    time.sleep(3)
    for _ in range(37):move_pointer_right()
    for _ in range(10):move_pointer_up()
    driver.find_element(By.XPATH, "//*[@id='mapsChallengeSubmit']").click()
    time.sleep(10)

def move_pointer_right():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()

def move_pointer_up():
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()

def pageSeven():
    time.sleep(1)
    #open file in write and binary mode
    with open('Logo.png', 'wb') as file:
        #identify image to be captured
        l = driver.find_element_by_xpath("//*[@id='notABotCaptchaImg']")
        #write file
        file.write(l.screenshot_as_png)
    
    # img = driver.find_element_by_xpath("//*[@id='notABotCaptchaImg']")
    # src = img.get_attribute('src')
    # # download the image
    # urllib.urlretrieve(src, "captcha.png")
    # time.sleep(5)

def pageSevenTwo():
    time.sleep(1)
    # q = 'captcha();'
    # print(str(driver.execute_script(q)))
    val1=""
    for entry in driver.get_log('browser'):
        # print (entry)
        val1=""
        val1=entry
    print("Final Value is:")
    # val2=val1.split("\"")
    val2=val1["message"].split("\"")[1]
    # print(val2)
    driver.find_element(By.XPATH, "//*[@id='notABotCaptchaResponse']").send_keys(val2)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='notABotCaptchaSubmit']").click()
    time.sleep(5)
    

def close_driver():
    time.sleep(2)
    # Close ChromeDriver
    print("Closing ChromeDriver")
    driver.quit()

print("Execution Started")
capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = { 'browser':'INFO' }
driver = webdriver.Chrome(executable_path="./webDrivers/chromedriver", desired_capabilities=capabilities)

startExecution()

pageOne()

pageTwo()

pageThree()

pageFour()

pageFive()

pageSix()

# pageSeven()

pageSevenTwo()

close_driver()
print("Execution Completed.")
