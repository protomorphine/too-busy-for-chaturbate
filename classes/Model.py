import requests


class Model(object):
    def __init__(self, nickname):
        super(Model, self).__init__()
        self.nickname = nickname
        self.chaturbate_link = "https://chaturbate.eu/" + self.nickname
        self.json_data = self.connect_to_chaturbate()
        self.online = False
        self.m3u8_link = self.get_m3u8_link()

    def connect_to_chaturbate(self):
        print("Trying to connect " + self.chaturbate_link + " ... ", end="")
        try:
            json_data = requests.get(
                "https://chaturbate.eu/api/chatvideocontext/{}".format(self.nickname)
            ).json()
            # time.sleep(10)
            print("success")
        except ValueError:
            print("failed")
            print("HTTP 404 - Model {} not found!".format(self.nickname))
            raise SystemExit(-1)
        return json_data

    def is_online(self):
        if self.json_data["room_status"] not in ["offline", "private"]:
            self.online = True
        print("Room status is {}".format(self.json_data["room_status"]))
        if self.json_data["room_status"] == "private":
            print(
                "You can spy {nickname} show for {price} tkn per minute on {link}".format(
                    nickname=self.nickname,
                    price=self.json_data["spy_private_show_price"],
                    link=self.chaturbate_link,
                )
            )
        return self.online

    def get_m3u8_link(self):
        if self.is_online():
            self.m3u8_link = self.json_data["hls_source"].split("?")[0]
            return self.m3u8_link
        raise SystemExit(-1)
