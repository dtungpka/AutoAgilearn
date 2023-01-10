import trio
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import logging
logging.basicConfig(level=logging.DEBUG)
import itertools
#import pychrome

PLAYER_CLICKS = [100,2]

# fetch a site that does xhr requests
URL = "https://phenikaa.agilearn.app"
options = {
    'verify_ssl': False,
    'connection_timeout': None,
    'connection_keep_alive': False  

}
driver = webdriver.Chrome()
driver.get(URL)


def end_vid():
    try:
        iframe = driver.find_element(By.CSS_SELECTOR,"#vertical-tabpanel-0 > div > div:nth-child(1) > div > div > div > iframe")
    except:
        sleep(20)
        return False
    driver.switch_to.frame(iframe)
    video = driver.find_element(By.ID,"player")
    video.click()
    player = driver.find_element(By.TAG_NAME,"video")
    #press the right arrow button 20 times
    for i in range(PLAYER_CLICKS[0]):
        player.send_keys(Keys.ARROW_RIGHT)
        sleep(0.01)
    for i in range(PLAYER_CLICKS[1]):
        player.send_keys(Keys.ARROW_LEFT)
        sleep(0.1)
    driver.switch_to.default_content()
    while "M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z" not in driver.page_source:
        sleep(0.5)
    return True
def interceptor(request, response):  # A response interceptor takes two args
    if  'callable-getReviewQuestionResult' in request.url :
        print(response.body)

#driver.response_interceptor = interceptor
def rand_ans():
    sleep(2)
    box = driver.find_element(By.CLASS_NAME,"MuiFormGroup-root")
    try:
        
        #check element role 
        role = box.get_attribute("role")
    except:
        role = "checkbox"
    if role == "radiogroup":
        #get all radio buttons inside box
        radios = box.find_elements(By.CSS_SELECTOR,"input[type='radio']")
        #get the number of radio buttons
        num = len(radios)
        for i in range(num):
            #select a random radio button
            rand = radios[i]
            rand.click()
            sleep(0.1)
            driver.find_element(By.XPATH,"//*[@id=\"vertical-tabpanel-1\"]/div/div[2]/button").click()
            sleep(1)
            while True:
                if "Chúc mừng bạn đã trả lời đúng!" in driver.page_source:
                    break
                else:
                    try:
                        driver.find_element(By.CSS_SELECTOR,"#vertical-tabpanel-1 > div > button").click()
                        break
                    except:
                        sleep(0.5)
            if "Chúc mừng bạn đã trả lời đúng!" in driver.page_source:
                    break
    else:
        box_choose = driver.find_element(By.XPATH,"//*[@id=\"questionundefined\"]/div/div[2]/div/fieldset/div")
        checkb = box_choose.find_elements(By.CSS_SELECTOR,'input[type=\'checkbox\']')
        num = len(checkb)
        combinations = list(itertools.product('01', repeat=num))
        s = ["".join(i) for i in combinations if i.count('1') > 1]
        print(combinations)
        for i in s:
            if i == '0'*num:
                continue
            for j in range(len(i)):
                if i[j] == '1':
                    checkb[j].click()
               
            sleep(0.1)
            driver.find_element(By.XPATH,"//*[@id=\"vertical-tabpanel-1\"]/div/div[2]/button").click()
            sleep(1)
            while True:
                if "Chúc mừng bạn đã trả lời đúng!" in driver.page_source:
                    break
                else:
                    try:
                        driver.find_element(By.CSS_SELECTOR,"#vertical-tabpanel-1 > div > button").click()
                        break
                    except:
                        sleep(0.5)
            if "Chúc mừng bạn đã trả lời đúng!" in driver.page_source:
                    break
input("Press Enter to continue...")
svgs = driver.find_elements(By.CSS_SELECTOR, "svg.MuiSvgIcon-root.MuiSvgIcon-colorAction.MuiSvgIcon-fontSizeSmall")
print("Found", len(svgs), "svgs")
for svg in svgs:
    sleep(.2)
    svg.click()
    a = 0
    while True:
        try:
            a = driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/main/div/div[1]/div/div[3]/button")
            a.click()
            sleep(3)
            break
        except:
            a+= 1
            if a == 10:
                print("break")
                break
            sleep(0.5)
    if not end_vid():
        continue
    sleep(0.5)
    
    btt = driver.find_element(By.ID,"vertical-tab-1")
    btt.click()
    sleep(0.5)
    rand_ans()
    #tab.Page.navigate(url=URL, _timeout=5)