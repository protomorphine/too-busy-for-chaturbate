import os
import time
import selenium
import requests
from seleniumwire import webdriver

# TODO: don't use selenium cause requests faster
class Model(object):
    def __init__(self, nickname):
        super(Model, self).__init__()
        self.nickname = nickname
        self.chaturbate_link = "https://chaturbate.eu/" + self.nickname
        self.json_data = {}
        self.online = False
        self.driver = 0
        self.m3u8_link = ""

    # +------------------------------------------------------------------------+
    # |    Инициализая подключения к chaturbate.eu + подтверждение возраста    |
    # +------------------------------------------------------------------------+
    def connect_to_chaturbate(self):
        print("Trying to connect " + self.chaturbate_link + " ...")
        self.json_data = requests.get(
            "https://chaturbate.eu/api/chatvideocontext/{}".format(model.nickname)
        ).json()
        return self.json_data

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
        if json_data["room_status"] not "offline":
            print("Room is currently offline")

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
