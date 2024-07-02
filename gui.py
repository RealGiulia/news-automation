from selenium import webdriver
from logger import Logger
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

class Searcher:

    def __init__(self) -> None:
        self.driver = Chrome()
        self.log = Logger()


    def open_website(self):
        try:
            self.driver.get('https://www.latimes.com/')
        except Exception as error:
            self.log.register_exception("Exception ocurred when opening page: %s" % error)

    
    def search_news(self):
        try:
            expand_search_script = "document.getElementsByClassName('flex justify-center items-center h-10 py-0 px-2.5 bg-transparent border-0 text-header-text-color cursor-pointer transition-colors hover:opacity-80 xs-5:px-5 md:w-10 md:p-0 md:ml-2.5 md:border md:border-solid md:border-header-border-color md:rounded-sm lg:ml-3.75')[0].click()"
            self.driver.execute_script(expand_search_script)
        except Exception as error:
            self.log.register_exception("Exception ocurred when clicking on search button: %s" % error)



#driver = Shadow(driver)
# driver.execute_script("document.getElementsByClassName('text__text__1FZLe text__graphite__1DktY text__medium__1kbOh text__extra_small__1Mw6v body__base__22dCE body__extra_small_body__3QTYe link')[0].click()")
# print('teste')