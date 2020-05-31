import os
import time
import subprocess


class Vidak(object):
    def __init__(self, ffmpeg_path, vids_folder, model):
        super(Vidak, self).__init__()
        self.fmmpeg_path = ffmpeg_path
        self.model = model
        self.workind_dir = vids_folder + model.nickname
        self.log_file = "{}\\ffmpeg.log".format(self.workind_dir)

    def output_name(self):
        time_now = time.strftime("%d-%b-%H-%M-%S-")
        return "{time}{nickname}-chaturbate.mkv".format(
            time=time_now, nickname=self.model.nickname
        )

    def record_m3u8_stream(self):
        if self.model.online:
            approve_record = input("Start recording broadcast? (y/n) ").lower()
            if approve_record in ["y", "yes", ""]:
                if not os.path.exists(self.workind_dir):
                    os.mkdir(self.workind_dir)
                out_file = self.output_name()
                full_path = self.workind_dir + "\\" + out_file
                print(
                    "Recording broadcast in {}".format(full_path)
                    + "\nPlease don't close this window\n"
                    + "To stop  recording press CTRL + C"
                )
                try:
                    with open(self.log_file, "w") as ffmpeg_log:
                        subprocess.call(
                            [
                                self.fmmpeg_path,
                                "-i",
                                self.model.m3u8_link,
                                "-c",
                                "copy",
                                "-vcodec",
                                "copy",
                                "-bsf:a",
                                "aac_adtstoasc",
                                full_path,
                            ],
                            stdout=ffmpeg_log,
                            stderr=subprocess.STDOUT,
                        )
                except KeyboardInterrupt:
                    print(
                        "Recording was stopped by user.\n"
                        + "Recorded broadcast in {}".format(full_path)
                    )
                return "Recorded in " + full_path
            raise SystemExit(-1)
