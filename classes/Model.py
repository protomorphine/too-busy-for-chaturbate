import os
import time
import requests


class Model(object):
    def __init__(self, nickname):
        super(Model, self).__init__()
        self.nickname = nickname
        self.chaturbate_link = "https://chaturbate.eu/" + self.nickname
        self.chat_video_context = {}
        self.online = False
        self.m3u8_link = ""

    def connect_to_chaturbate(self):
        print("Trying to connect " + self.chaturbate_link + " ...")
        try:
            self.chat_video_context = requests.get(
                "https://chaturbate.eu/api/chatvideocontext/{}".format(self.nickname)
            ).json()
        except ValueError:
            print("HTTP 404 - Model {} not found!".format(self.nickname))
            raise SystemExit(-1)
        return self.chat_video_context

    def is_online(self):
        if self.chat_video_context["room_status"] not in ["offline", "private"]:
            self.online = True
        print("Room status is {}".format(self.chat_video_context["room_status"]))
        return self.online

    def get_m3u8_link(self):
        if self.is_online():
            self.m3u8_link = self.chat_video_context["hls_source"].split("?")[0]
            return self.m3u8_link
        raise SystemExit(-1)
