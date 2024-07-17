import requests
from datetime import date
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Searcher:

    def __init__(self, img_path:str, log: object) -> None:
        self.driver = Chrome()
        self.log = log
        self.img_folder = img_path + date.today().strftime("%m-%d-%y")

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
            sleep(3)
            sort_by_element = self.driver.find_element(By.CLASS_NAME,"select-input")
            sort_by_element.click()
            select = Select(sort_by_element)
            if period == 'Newest':
                select.select_by_value('1')
            else:
                select.select_by_value('2')
            self.log.register_info("Search was done!")
            sleep(2)
        except Exception as error:
            self.log.register_exception("Exception ocurred when selecting period of time: %s" % error)


    def select_topic(self, topic: str):
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
            sleep(3)
            self.log.register_info("Option selected")
        except Exception as error:
            if "Cannot read properties of undefined" in str(error):
                self.log.register_exception("Invalid topic. Please, select an available topic on the website!")


    def get_news_info(self, news_storage: list):
        try:
            self.driver.implicitly_wait(5)
            news_table = self.driver.find_element(By.CLASS_NAME, "search-results-module-results-menu")
            news_item =  news_table.find_elements(By.TAG_NAME, 'li')
            counter = 0

            for element in news_item:
                try:
                    counter += 1
                    content_dict = {}
                    news_title = element.find_element(By.TAG_NAME, 'h3')
                    content_dict["Title"] = self.driver.execute_script("return arguments[0].textContent", news_title)
                except NoSuchElementException:
                    self.log.register_exception("Item has no title.")
                    content_dict["Title"] = "empty"

                try:
                    image = element.find_element(By.TAG_NAME,'img')
                    content_dict["IMG_URL"] = image.get_attribute("src")
                    content_dict["IMG_NAME"] = self.img_folder + "/img-" + str(counter) + ".jpg"

                except NoSuchElementException:
                    self.log.register_exception("Could not get News URL")
                    content_dict["IMG_URL"] = "empty"
                    content_dict["IMG_NAME"] = "empty"
                    
                try:
                    news_desc = element.find_element(By.CLASS_NAME, "promo-description")
                    content_dict["Description"] = self.driver.execute_script("return arguments[0].textContent", news_desc)
                except NoSuchElementException:
                    self.log.register_exception("Item dont have description")
                    content_dict["Description"] = "empty"

                try:
                    news_date = element.find_element(By.CLASS_NAME,"promo-timestamp")
                    content_dict["Date"] = self.driver.execute_script("return arguments[0].textContent", news_date)
                except NoSuchElementException:
                    self.log.register_exception("Item has no date.")
                    content_dict["Date"] = "N/A"

                news_storage.append(content_dict)

        except Exception as error:
            self.log.register_exception("Could not get news content. Error %s" %error)

        finally:
            return news_storage


    def go_next_page(self):
        try:
            next_page_element = self.driver.find_element(By.CLASS_NAME, "search-results-module-next-page")
            next_page_element.click()
            sleep(4)
        except Exception as error:
            self.log.register_exception("Could not get news content. Error: %s" %error)


    def get_image_info(self, news: list):

        try:
            from datetime import date
            import os
            if not os.path.exists(self.img_folder):
                os.mkdir(self.img_folder)

            for item in news:
                if item["IMG_URL"] != "empty":
                    sleep(2)
                    img = requests.get(item["IMG_URL"])
                    if img.status_code == 200:
                        with open(item["IMG_NAME"], 'wb') as f:
                            f.write(img.content)
                    sleep(3)
        except Exception as error:
            self.log.register_exception("Could not get image information. Error: %s" %error)


 