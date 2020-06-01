import os
import time
import subprocess


class Vidak(object):
    def __init__(self, ffmpeg_path, vids_folder, model):
        super(Vidak, self).__init__()
        self.fmmpeg_path = ffmpeg_path
        self.model = model
        self.workind_dir = vids_folder + model.nickname
        self.log_file = f"{self.workind_dir}\\ffmpeg.log"

    def output_name(self):
        time_now = time.strftime("%d-%b-%H-%M-%S-")
        return f"{time_now}{self.model.nickname}-chaturbate.mkv"

    def record_m3u8_stream(self):
        if self.model.online:
            background_rec = input(
                "Do u want to record broadcast in background? (y/n) "
            ).lower()
            approve_record = input("Start recording broadcast? (y/n) ").lower()
            if approve_record in ["y", "yes", ""]:
                if not os.path.exists(self.workind_dir):
                    os.mkdir(self.workind_dir)
                out_file = self.output_name()
                full_path = f"{self.workind_dir}\\{out_file}"
                ffmpeg_exec = [
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
                ]
                print(
                    f"Recording broadcast in {full_path}"
                    + "\nPlease don't close this window\n"
                    + "To stop  recording press CTRL + C"
                )
                try:
                    with open(self.log_file, "w") as ffmpeg_log:
                        if background_rec in ["y", "yes", ""]:
                            subprocess.Popen(
                                ffmpeg_exec,
                                stdout=ffmpeg_log,
                                stderr=subprocess.STDOUT,
                            )
                        else:
                            subprocess.call(
                                ffmpeg_exec,
                                stdout=ffmpeg_log,
                                stderr=subprocess.STDOUT,
                            )
                except KeyboardInterrupt:
                    print(
                        "Recording was stopped by user.\n"
                        + f"Recorded broadcast in {full_path}"
                    )
                return f"Recorded in {full_path}"
            raise SystemExit(-1)
