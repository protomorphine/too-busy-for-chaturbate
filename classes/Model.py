import os
import selenium
from seleniumwire import webdriver


class Model(object):
    def __init__(self, nickname):
        super(Model, self).__init__()
        self.nickname = nickname
        self.chaturbate_link = "https://chaturbate.eu/" + self.nickname
        self.online = False
        self.driver = 0
        self.m3u8_link = ""

    # +------------------------------------------------------------------------+
    # |    Инициализая подключения к chaturbate.eu + подтверждение возраста    |
    # +------------------------------------------------------------------------+
    def connect_to_chaturbate(self):
        # запускаем Хром с параметром headless
        # чтобы не создавать окно браузера
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=chrome_options)

        print("Trying to connect " + self.chaturbate_link + " ...")
        self.driver.get(self.chaturbate_link)

        try:
            entrance_btn = self.driver.find_element_by_id("close_entrance_terms")
        except selenium.common.exceptions.NoSuchElementException:
            return False

        # self.exists = True
        entrance_btn.click()
        print("Sucсessfuly connected!")
        return self.driver

    def close_connection(self):
        time.sleep(10)
        self.driver.close()

    # +------------------------------------------------------------------------+
    # |         Возвращает состояние трансляции модели (Online/Offline)        |
    # +------------------------------------------------------------------------+
    def is_online(self):
        driver = self.driver
        if not self.driver:
            return -1
        # на chaturbate.eu чтобы узнать онлайн модель или нет необходимо
        # найти на странице тэг <video> и узнать параметр src
        # если src есть - трансляция запущена
        video_player = driver.find_element_by_tag_name("video")
        video_src = video_player.get_attribute("src")

        if not video_src:
            return False
        else:
            self.online = True
            print(self.nickname + " is online now")
            return True

    # +------------------------------------------------------------------------+
    # |                 Вытягивает ссылку на потокое видео                     |
    # +------------------------------------------------------------------------+
    def get_m3u8_link(self):
        self.is_online()
        if self.online:
            driver = self.driver
            for request in driver.requests:
                if request.response and request.path.find(".m3u8"):
                    self.m3u8_link = request.path
                    return self.m3u8_link
        else:
            print("Coudn't get stream link. Model is offline.")
            return -1
