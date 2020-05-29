from seleniumwire import webdriver
import time

class Chaturbate(object):
    def __init__(self, url):
        super(Chaturbate, self).__init__()
        self.url = url
        self.driver = 0

    def connect(self):
        # запускаем Хром с параметром headless
        # чтобы не создавать окно браузера
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options = chrome_options)

        # Подтвержаем что наш возраст 18+
        self.driver.get(self.url)
        entrance_btn = self.driver.find_element_by_id("close_entrance_terms")
        entrance_btn.click()

        return self.driver

    def close_connection(self):
        time.sleep(20)
        self.driver.quit()
