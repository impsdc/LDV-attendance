from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#Ici mettre ses identifiants LDV
emailDevinci = '##########'
mdp = '#######'

#Lancement du navigateur
def init():
    options = Options()
    options.headless = False
    return webdriver.Firefox(options=options) 

#Connection au portail LDV
def connect(driver):
    driver.get('https://www.leonard-de-vinci.net/') # loaded when `onload` even has fired
    time.sleep(1)
    driver.find_element_by_id("login").send_keys(emailDevinci)
    driver.find_element_by_css_selector(".pull-right").click()
    time.sleep(1)
    driver.find_element_by_id('passwordInput').send_keys(mdp)
    driver.find_element_by_css_selector("#submitButton").click()

def checking(driver):
    time.sleep(1)
    driver.get('https://www.leonard-de-vinci.net')
    time.sleep(2)
    #check if LDV is responding
    if driver.find_element_by_xpath("//*[text()[contains(., 'Relevé de présence')]]"):
        driver.find_element_by_xpath("//*[text()[contains(., 'Relevé de présence')]]").click()
        time.sleep(1)
    elif driver.find_element_by_xpath("//*[text()[contains(., 'Relevé de présence')]]"):
        time.sleep(5)
        btn = driver.find_element_by_xpath("//*[text()[contains(., 'Relevé de présence')]]")
        btn.click()
        time.sleep(1)
    else:
        return print('unable to get the ldv portail, system is having maintenance')
def getNumberOfLesson(driver):
    #Check if got lessons today
    if driver.find_elements_by_css_selector('tbody tr'): 
        cours = len(driver.find_elements_by_css_selector('tbody tr'))
        return cours
    else:
        return print("Pas de cours aujourd'hui, go dodo ;)")
    
def getToPresencePage(cours, driver):
    driver.get('https://www.leonard-de-vinci.net/student/presences/')
    time.sleep(1)
    ex = driver.find_elements_by_css_selector("tbody tr")
    ex[cours].find_element_by_css_selector('a').click()    

def main():
    driver = init()
    connect(driver)
    while True:
        checking(driver)
        nbLessons = getNumberOfLesson(driver)
        #Check which lessons the attendance can be taken
        for cours in range(nbLessons):
            getToPresencePage(cours, driver)
            if len(driver.find_elements_by_css_selector("#set-presence")) > 0:
                driver.find_element_by_id("set-presence").click()
                return print("Je t'es mis présent pour ton cours ;) ")
            else: 
                print(driver.find_elements_by_css_selector('#body_presence div')[0].get_attribute("innerHTML"))
    driver.quit()

if __name__ == '__main__':
    main()
