import os
import time
import subprocess


class Vidak(object):
    def __init__(self, ffmpeg_path, vids_folder, model):
        super(Vidak, self).__init__()
        self.fmmpeg_path = ffmpeg_path
        self.model = model
        self.workind_dir = vids_folder + model.nickname
        self.log_file = self.workind_dir + "\\ffmpeg.log"
        if not os.path.exists(self.workind_dir):
            os.mkdir(self.workind_dir)

    # +------------------------------------------------------------------------+
    # |         формирование названия файла число-месяц-время-ник-сайт         |
    # +------------------------------------------------------------------------+
    def output_name(self):
        time_now = time.strftime("%d-%b-%H-%M-%S-")
        return time_now + self.model.nickname + "-chaturbate.mp4"

    # +------------------------------------------------------------------------+
    # |                      Запись трансляции в файл                          |
    # +------------------------------------------------------------------------+
    def record_m3u8_stream(self):
        if self.model.online:
            approve_record = input("Start recording broadcast? (y/n) ").lower()
            if approve_record in ["y", "yes", ""]:
                out_file = self.output_name()
                full_path = self.workind_dir + "\\" + out_file
                print(
                    "Recording broadcast in "
                    + full_path
                    + "\nPlease don't close this window\n"
                    + "To stop  recording press CTRL + C"
                )
                with open(self.log_file, "w") as ffmpeg_log:
                    subprocess.call(
                        [
                            self.fmmpeg_path,
                            "-i",
                            self.model.m3u8_link,
                            "-c",
                            "copy",
                            full_path,
                        ],
                        stdout=ffmpeg_log,
                        stderr=subprocess.STDOUT,
                    )
                return "Recorded in " + full_path
            else:
                return -1
