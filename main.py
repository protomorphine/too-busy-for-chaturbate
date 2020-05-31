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
        vidak = Vidak(FFMPEG_PATH, VIDS_PATHH, model)
        vidak.record_m3u8_stream()
    except KeyboardInterrupt:
        print("Script was stopped by user. Exiting.")


if __name__ == "__main__":
    main()
