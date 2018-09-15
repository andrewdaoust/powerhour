from __future__ import unicode_literals
from pydub import AudioSegment
import os
import glob
import shutil
import youtube_dl
import csv


def make_song_dir(base_dir):
    os.chdir(base_dir)
    os.mkdir('songs')


def download_song(base_dir, filename, source_link):
    os.chdir(base_dir)
    ydl_opts = {'outtmpl': filename,
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio',
                     'preferredcodec': 'wav'
                     # 'preferredquality': '192'
                     }
                ]
                }

    os.chdir(base_dir + "/songs")
    print("Downloading file to:", os.getcwd())

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([source_link])


def find_file(filename, base_dir):
    os.chdir(base_dir + '/songs')
    filename += '.*'
    file_and_ext = glob.glob(filename)
    os.chdir(base_dir)
    return file_and_ext


def get_ext(file_str):
    path, ext = os.path.splitext(file_str)
    return ext


def transition_setup(csv_line, base_dir):
    link = csv_line[0]
    start = timestamp_to_sec(csv_line[1]) * 1000
    end = timestamp_to_sec(csv_line[2]) * 1000
    tran = 'transition'

    download_song(working_dir, tran, link)
    file = find_file(tran, base_dir)
    file = file[0]
    ext = get_ext(file)

    os.chdir(base_dir + '/songs')
    tran_seg = AudioSegment.from_file(file, ext)
    tran_seg = tran_seg[start:end]
    os.chdir(base_dir)
    return tran_seg


def timestamp_to_sec(timestamp):
    min, sec = timestamp.split(':')
    start_in_sec = int(min) * 60 + int(sec)
    return start_in_sec


def start_end_ms(start_time):
    start_time = timestamp_to_sec(start_time)
    start = start_time * 1000
    end = start + 60000
    return start, end


def make_segment(filename, start_time, tran_sound):
    filename = 'songs/' + filename
    start, end = start_end_ms(start_time)
    ext = get_ext(filename)
    seg = AudioSegment.from_file(filename, ext)
    seg = seg[start:end] + tran_sound
    return seg


def clean_up(base_dir, delete=True):
    if delete:
        print("Removing downloaded files...")
        shutil.rmtree(base_dir + "/songs")
        print('Files removed.')
    else:
        print("Downloaded files were kept.")


def save(save_dir, ph, filename, file_type):
    os.chdir(save_dir)
    print("Saving file to", os.getcwd())
    ph.export(filename, format=file_type)
    print("File saved as " + file_type)


working_dir = os.getcwd()
make_song_dir(working_dir)

# Take info from user
input_csv = input('Enter name of csv file (make sure it is in the csvs directory:\n')
input_csv = 'csvs/' + input_csv
output_name = input("Enter name of the file that will be output (don't include the extention):\n")
save_ext = input('Enter extention you want to save file as (e.g. wav or mp3):\n')
output_name += '.' + save_ext
save_loc = input('Enter the path for the location to save the output file:\n')

songs = []
with open(input_csv) as csv_file:
    file = csv.reader(csv_file)
    for line in file:
        songs.append(line)

# setup transition AudioSegment
t = songs.pop(0)
transition = transition_setup(t, working_dir)

power_hour = transition

for i in range(len(songs)):
    print('-----------------------------------------'*2)
    print('Song #' + str(i + 1))
    params = songs[i]
    print(params)
    link = params[0]
    start = params[1]
    fname = 'file' + str(i + 1)
    print(fname)

    # download song
    download_song(working_dir, fname, link)

    # make audio segment and add to overall audio segment
    song_file = find_file(fname, working_dir)
    print(song_file)
    new_min_seg = make_segment(song_file[0], start, transition)
    power_hour += new_min_seg

# export completed file
save(save_loc, power_hour, output_name, save_ext)

# cleanup after finished
clean_up(working_dir)
