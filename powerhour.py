import csv
from pydub import AudioSegment

in_file_name = input("Enter the path or filename of the csv for generating the power hour: \n")
song_dir = input("Enter the folder the songs are in: \n")
out_file_name = input("Enter the name for the power hour output file (don't include the extension): \n")
out_file_name += ".wav"

songs = []
with open(in_file_name) as csvfile:
    file = csv.reader(csvfile)
    for line in file:
        songs.append(line)

power_hour = AudioSegment.empty()

transition_file = songs.pop(0)
transition = AudioSegment.from_wav(transition_file)

for item in songs:
    filename, start_time = 'songs/' + song_dir + '/' + item[0], item[1]
    song = AudioSegment.from_file(filename, format='.wav')
    start_time *= 1000
    song = song[start_time:start_time + 60000]
    power_hour += song + transition

power_hour.export(out_file_name, format=".wav")
