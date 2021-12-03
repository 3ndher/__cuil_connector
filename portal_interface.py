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
                return browser