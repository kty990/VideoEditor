import subprocess

class Time:
    def __init__(self,hour,minute,second,milisecond):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.milisecond = milisecond

    def NumberToFormatString(self, value: int = 0, places: int = 1):
        x = str(value)
        while len(x) < places:
            x = f"0{x}"
        return x

    def __str__(self):
        hour = self.NumberToFormatString(self.hour, 2)
        min = self.NumberToFormatString(self.minute, 2)
        sec = self.NumberToFormatString(self.second, 2)
        mil = self.NumberToFormatString(self.milisecond, 3)
        return f"{hour}:{min}:{sec}.{mil}"

class Audio:
    def __init__(self, input: str = None, start: Time = Time(0,0,0,0), length: Time = Time(0,0,0,0), output: str = "output.wav"):
        self.input_file = input
        self.start_time = start
        self.duration = length
        self.output_file = output

    def GetNextClip(self):
        command = ["ffmpeg", "-i", self.input_file, "-vn", "-ss", self.start_time, "-t", self.duration,
                "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", self.output_file]

        try:
            subprocess.run(command, check=True)
            with open(self.output_file, "r") as file:
                return file
        except:
            return False