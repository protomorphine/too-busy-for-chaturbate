import os
import time
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
        # запускаем firefox с параметром headless
        # чтобы не создавать окно браузера
        options = selenium.webdriver.firefox.options.Options()
        options.headless = True
        # настройки proxy
        ip, port = "192.168.1.1", "443"
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 1)
        firefox_profile.set_preference("network.proxy.socks", ip)
        firefox_profile.set_preference("network.proxy.socks_port", int(port))

        self.driver = webdriver.Firefox(firefox_profile, options=options)

        print("Trying to connect " + self.chaturbate_link + " ...")
        self.driver.get(self.chaturbate_link)

        try:
            entrance_btn = self.driver.find_element_by_id("close_entrance_terms")
        except selenium.common.exceptions.NoSuchElementException:
            return False

        entrance_btn.click()
        return self.driver

    def close_connection(self):
        try:
            self.driver.quit()
        except ConnectionAbortedError:
            raise ConnectionAbortedError
            print("ABORTED")

    # +------------------------------------------------------------------------+
    # |         Возвращает состояние трансляции модели (Online/Offline)        |
    # +------------------------------------------------------------------------+
    def is_online(self):
        if not self.driver:
            return -1
        # на chaturbate.eu чтобы узнать онлайн модель или нет необходимо
        # найти на странице тэг <video> и узнать параметр src
        # если src есть - трансляция запущена
        video_player = self.driver.find_element_by_tag_name("video")
        video_src = video_player.get_attribute("src")

        if not video_src:
            return False
        self.online = True
        print(self.nickname + " is online now")
        return True

    # +------------------------------------------------------------------------+
    # |                 Вытягивает ссылку на потокое видео                     |
    # +------------------------------------------------------------------------+
    def get_m3u8_link(self):
        self.is_online()
        if self.online:
            for request in self.driver.requests:
                if request.response and request.path.find(".m3u8") != -1:
                    self.m3u8_link = request.path
                    self.close_connection()
                    return self.m3u8_link
        print("Coudn't get broadcast link. Model is offline.")
        return -1
