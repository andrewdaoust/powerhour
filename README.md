# Powerhour.py

### About this project
This project uses `pydub` and `ffmpeg` to create a wav file to use as a power hour.

### csv formatting
A csv is required with the required format:
- Line 1: transition sound, should follow the format: link(YouTube, Soundcloud, or whatever else youtube-dl supports), start time (minutes:seconds), end time (minute:seconds)
- Line 2 to 61: The sources for the minute chunks in the power hour and should follow the format: link(YouTube, Soundcloud, or whatever else youtube-dl supports), start time (minutes:seconds)

### Setting up the project
In the directory that contains the power hour script create another directory called `csvs`.  Put any csvs you want to use in the `csvs` directory.  When the code is run, it will ask for input from the user about the name of the csv, the name of the file to be output and its extention type, and the path for where to save the file.

### What is a power hour
From Urban Dictionary:

Take one shot of beer every minute for an hour. This can be more or less potent depending on what kind of beer you drink. From strongest to weakest, your choices are malt liquor, ice beer, regular beer, and light beer. To make a power hour even better, burn a 60 minute CD with 60 1 minute tracks. Play a different song for every shot you take!

This repo helps create the "CD" for the power hour!


P.S. Thanks Ian, love you ;*
