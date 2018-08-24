import csv
from pydub import AudioSegment

in_file_name = "mycsv.csv"
out_file_name = "mypowerhour.wav"

songs = []
with open(in_file_name) as csvfile:
    file = csv.reader(csvfile)
    for line in file:
        songs.append(line)

power_hour = AudioSegment.empty()

transition = songs.pop(0)
for item in songs:
    filename, start_time = item[0], 'songs/' + item[1]
    song = AudioSegment.from_file(filename, format='.wav')
    start_time *= 1000
    song = song[start_time:start_time + 60]
    power_hour += song + transition

power_hour.export(out_file_name, format=".wav")

