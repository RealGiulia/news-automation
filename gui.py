from selenium import webdriver
from logger import Logger
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
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
            self.log.register_info('Page opened successfully!')
        except Exception as error:
            self.log.register_exception("Exception ocurred when opening page: %s" % error)

    
    def search_news(self, search_term):
        try:
            expand_search_script = "document.getElementsByClassName('flex justify-center items-center h-10 py-0 px-2.5 bg-transparent border-0 text-header-text-color cursor-pointer transition-colors hover:opacity-80 xs-5:px-5 md:w-10 md:p-0 md:ml-2.5 md:border md:border-solid md:border-header-border-color md:rounded-sm lg:ml-3.75')[0].click()"
            self.driver.execute_script(expand_search_script)

            input_search = self.driver.find_element(By.XPATH, "/html/body/ps-header/header/div[2]/div[2]/form/label/input")
            input_search.send_keys(search_term)
            input_search.send_keys(Keys.ENTER)
            sleep(2)
            self.log.register_info("Search was done!")
        except Exception as error:
            self.log.register_exception("Exception ocurred when clicking on search button: %s" % error)


    def select_period(self, period: str):
        try:
            sort_by_element = self.driver.find_element(By.XPATH,
                "/html/body/div[2]/ps-search-results-module/form/div[2]/ps-search-filters/div/main/div[1]/div[2]/div/label/select")
            sort_by_element.click()
            select = Select(sort_by_element)
            if period == 'Newest':
                select.select_by_value('1')
            else:
                select.select_by_value('2')
            self.log.register_info("Search was done!")
        except Exception as error:
            self.log.register_exception("Exception ocurred when selecting period of time: %s" % error)


    def select_topics(self, topic: str):
        try:
            script = ("""
                        var table = document.getElementsByClassName('search-filter-menu')[0]
                        var lines = table.getElementsByTagName('li')
                        for (var i = 0;i<lines.length;i++){
                            var topic = lines[i].getElementsByTagName('span')[0].innerText
                            if (topic == '%s'){
                                lines[i].getElementsByClassName('checkbox-input-element')[0].click();
                                break;
                            }
                        }
                    """ % topic)
            self.driver.execute_script(script)
            self.log.register_info("Option selected")
        except Exception as error:
            self.log.register_exception("Could not select topic due to error: %s" % error)
                   




#driver = Shadow(driver)
# driver.execute_script("document.getElementsByClassName('text__text__1FZLe text__graphite__1DktY text__medium__1kbOh text__extra_small__1Mw6v body__base__22dCE body__extra_small_body__3QTYe link')[0].click()")
# print('teste')