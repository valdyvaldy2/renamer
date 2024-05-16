import os

subtitles = os.listdir()
subtitles.sort()

for index, sub in enumerate(subtitles):
    if sub.endswith("srt"):
        to_rename = f"(Drakorasia.show) AOUAD Eps - {str(index + 1).zfill(2)} 720p.srt"
        os.system(f"mv \"{sub}\" \"{to_rename}\"")
