import os.path
import os
import glob
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from datetime import date
from datetime import datetime
import random 
import sys
sys.path.append('../')
from private.credentials import discord_credentials






def doWhenReady(browser, By, function, input):

    repeat = True

    element = None

    exception = (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException,ElementNotInteractableException)

    while repeat:

        try:

            repeat = False

            if(By == 'id'):

                if(function == "find"):

                    element = browser.find_element_by_id(input)

            if(By == 'xpath'):

                if(function == "find"):

                    element = browser.find_element_by_xpath(input)

            if(By == 'action'):

                if(function == 'click'):

                    browser.click()

            if(By == 'partial_link_text'):

                if(function == 'find'):

                    element = browser.find_element_by_partial_link_text(input)

            # if(function == "select"):

            #     droplist = Select(browser.find_element_by_id(input))

            #     droplist.select_by_visible_text(chassis)      

        except exception:

            repeat = True

            pass

    return element

def openBrowser():

                browser = webdriver.Chrome()

                browser.get("https://discord.com/channels/900583560434561135/900777613704982608")
                time.sleep(5) 
                password = discord_credentials.password
                userName = discord_credentials.username

                element = browser.find_element_by_xpath("//*[@id=\"app-mount\"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
                element.send_keys(userName) 
                element = browser.find_element_by_xpath("//*[@id=\"app-mount\"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")
                element.send_keys(password)
                time.sleep(1)
                element.send_keys(Keys.ENTER)
                time.sleep(3)
                browser.refresh()

                element = doWhenReady(browser, 'xpath', 'find', "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div")
                
                count = 4
                timeInc = 30
                totalCount = 0
                while True:
                    
                    # if count <= 4: IS ANYTHING 
                    
                    element = doWhenReady(browser, 'xpath', 'find', "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div")
                    element.send_keys("\\w")
                    element.send_keys("o")
                    time.sleep(.7)
                    element.send_keys("r")
                    time.sleep(.7)
                    element.send_keys("k")
                    time.sleep(.7)
                    element.send_keys(Keys.ENTER)
                    time.sleep(1)
                    if count >= 4:
                        element = doWhenReady(browser, 'xpath', 'find', "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div")
                        element.send_keys("\\s")
                        element.send_keys("l")
                        time.sleep(.7)
                        element.send_keys("u")
                        time.sleep(.7)
                        element.send_keys("t")
                        time.sleep(.7)
                        element.send_keys(Keys.ENTER)
                        time.sleep(1)
                        
                        element = doWhenReady(browser, 'xpath', 'find', "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div")
                        element.send_keys("\\c")
                        time.sleep(.7)
                        element.send_keys("r")
                        time.sleep(.7)
                        element.send_keys("i")
                        time.sleep(.7)
                        element.send_keys("me")
                        time.sleep(.7)
                        element.send_keys(Keys.ENTER)
                        count = 0

                    randNum = random.randint(30,120)
                    print(randNum)
                    increase = count + randNum/30
                    count = count + int(increase)  
                    totalCount = totalCount + count  
                    print("count " + str(count))
                    print("totalCount = =" + str(totalCount))
                    time.sleep(randNum)

                    if totalCount > 60:
                        browser.close()

def openTab(browser):
    browser.get("https://discord.com/channels/900583560434561135/900583560879165522")
    time.sleep(5) 
    password = discord_credentials.password
    userName = discord_credentials.username

    element = browser.find_element_by_xpath("//*[@id=\"app-mount\"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
    element.send_keys(userName) 
    element = browser.find_element_by_xpath("//*[@id=\"app-mount\"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input")
    element.send_keys(password)
    time.sleep(1)
    element.send_keys(Keys.ENTER)
    time.sleep(3)
    browser.refresh()

    element = doWhenReady(browser, 'xpath', 'find', "//*[@id=\"app-mount\"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div")

  
    element.sendKeys(Keys.CONTROL+ "t")
    return