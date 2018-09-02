import csv
from pydub import AudioSegment

in_file_name = input("Enter the filename of the csv: \n")
in_file_name = 'csvs/' + in_file_name
song_dir = input("Enter the directory the songs are in: \n")
out_file_name = input("Enter the name for the power hour output file (don't include the extension): \n")
out_file_name = "out_files/" + out_file_name + ".wav"

songs = []
with open(in_file_name) as csvfile:
    file = csv.reader(csvfile)
    for line in file:
        songs.append(line)

power_hour = AudioSegment.empty()

transition_file = songs.pop(0)
transition_file = 'songs/' + song_dir + '/' + transition_file[0]
transition = AudioSegment.from_wav(transition_file)
power_hour += transition

for item in songs:
    filename, start_time = 'songs/' + song_dir + '/' + item[0], int(item[1])
    print('Adding:', filename)
    song = AudioSegment.from_wav(filename)
    start_time *= 1000
    song = song[start_time:start_time + 60000]
    power_hour += song + transition

print("Writing output file...")
power_hour.export(out_file_name, format="wav")
print("Finished.")
