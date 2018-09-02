# Powerhour.py

### About this project
This project uses `pydub` and `ffmpeg` to create a wav file to use as a power hour.

### csv formatting
A csv is required with the required format:
- Line 1: transition noise (Just the filename, the whole file will be played as the transition)
- Line 2 to 61: The files for the minute chunks in the power hour (The filename and the start time of the desired minute in seconds separated by a comma)

### Setting up the project
In the folder that contains the power hour script create directories called `csvs`, `songs`, and `out_files`.  Put any csvs you want to use in the `csvs` directory.  In the `songs` directory create a subdirectory containing all the songs you'd like to use.  The script will write the output file into the `out_files` directory.

### What is a power hour
From Urban Dictionary:

Take one shot of beer every minute for an hour. This can be more or less potent depending on what kind of beer you drink. From strongest to weakest, your choices are malt liquor, ice beer, regular beer, and light beer. To make a power hour even better, burn a 60 minute CD with 60 1 minute tracks. Play a different song for every shot you take!

This repo helps create the "CD" for the power hour!


P.S. Thanks Ian, love you ;*
