from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Common.configure import baseConfigure

class linuxindexPage(baseConfigure):


    def __init__(self,driver):
        baseConfigure.__init__(self,driver)
        driver.get('http://dkcphweb15/')
        testadress=driver.find_element_by_link_text('Start Page').get_attribute("href")
        driver.get(testadress+'/thin-client')


    def clickNextButton(self):
        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def chooseDevice(self):
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        device=(By.XPATH,"//label[contains(text(),'" + lastingDevicename+ "')]")
        self.click(*device)
        self.driver.find_element(By.ID,'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//input[@value='NEXT >']").click()

class windowsPage(baseConfigure):

    def __init__(self,driver):
        baseConfigure.__init__(self,driver)
        driver.get('http://dkcphweb15/')
        testadress='https://jabraxpress.jabra.com/'
        # testadress=driver.find_element_by_link_text('Start Page').get_attribute("href")
        driver.get(testadress+'/windows-desktop')

    def clickNextButton(self):

        button = (By.CLASS_NAME, 'button-container')
        self.click(*button)

    def chooseDevice(self):
        fo = open("device.txt", "rt")
        lastingDevicename = fo.read()
        device=(By.XPATH,"//label[contains(text(),'" + lastingDevicename+ "')]")
        self.click(*device)
        self.driver.find_element(By.ID,'btnAdd').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,"//input[@value='NEXT >']").click()