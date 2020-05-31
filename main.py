import subprocess
from classes.Model import Model
from classes.Vidak import Vidak


def main():
    try:
        FFMPEG_PATH = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
        VIDS_PATHH = "D:\\vids_chaturbate\\"

        welcome_logo = open("text\\wellcome.txt", "r").read()
        subprocess.call("cls", shell=True)
        print(welcome_logo)

        model = Model(input("Please, enter model nickname:\n> "))
        if model.connect_to_chaturbate():
            model.get_m3u8_link()
            vidak = Vidak(FFMPEG_PATH, VIDS_PATHH, model)
            vidak.record_m3u8_stream()
        else:
            print(
                "Model with nickname "
                + model.nickname
                + " doesn't exist.\n"
                + "Please check nickname and try again."
            )
    except KeyboardInterrupt:
        print("Script was stopped by user. Exiting.")


if __name__ == "__main__":
    main()
