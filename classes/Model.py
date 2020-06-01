import requests


class Model(object):
    def __init__(self, nickname):
        super(Model, self).__init__()
        self.nickname = nickname
        self.chaturbate_link = f"https://chaturbate.eu/{self.nickname}"
        self.json_data = self.connect_to_chaturbate()
        self.online = False
        self.m3u8_link = self.get_m3u8_link()

    def connect_to_chaturbate(self):
        print(f"Trying to connect {self.chaturbate_link} ... ", end="")
        try:
            json_data = requests.get(
                f"https://chaturbate.eu/api/chatvideocontext/{self.nickname}"
            ).json()
            print("success")
        except ValueError:
            print("failed")
            print(f"HTTP 404 - Model {self.nickname} not found!")
            raise SystemExit(-1)
        return json_data

    def is_online(self):
        if self.json_data["room_status"] not in ["offline", "private"]:
            self.online = True
        print(f"Room status is {self.json_data['room_status']}")
        if self.json_data["room_status"] == "private":
            print(
                f"You can spy {self.nickname} show for {self.json_data['spy_private_show_price']} tkn per minute on {self.chaturbate_link}"
            )
        return self.online

    def get_m3u8_link(self):
        if self.is_online():
            self.m3u8_link = self.json_data["hls_source"].split("?")[0]
            return self.m3u8_link
        raise SystemExit(-1)
