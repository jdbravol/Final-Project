#!/usr/bin/env python
# -*- coding: utf-8 -*-
from langdetect import detect

file_name = "young_thug"


def process():
    with open("../raw/"+file_name, "r") as input:
        with open("../processed/" + file_name, "wb") as output:
            lines = input.readlines()
            for line in lines:
                if "\n" == line:
                    output.write(line)
                elif "[" in line:
                    continue
                elif "@" in line:
                    continue
                elif ":" in line:
                    continue
                elif "(" in line:
                    continue
                elif "Tracklist" in line or "Album Art" in line or "Deluxe Edition" in line:
                    continue
                elif "Album Mastered by" in line or "Cover Art" in line or "Music Video Poster" in line:
                    continue
                elif "Lyrics for this song have yet to be released" in line:
                    continue
                elif "RCA Records" in line or "Keyboards by" in line or "Programming by" in line:
                    continue
                elif "Assisted at" in line or "Management by" in line :
                    continue
                elif "Produced by" in line or "Arrangement by" in line or "Production by" in line:
                    continue
                elif "Guitar by" in line or "Additional Vocals" in line or "Guitars by" in line or "Vocals by" in line:
                    continue
                elif "Assisted by" in line or "Mixed, Edited & Arranged by" in line or "Editing by" in line:
                    continue
                elif "Recorded by" in line or "Recorded and Mixed" in line or "Recorded & Mixed" in line or "Mixed by" in line:
                    continue
                elif "Trumpet by" in line or "Bass by" in line:
                    continue
                elif "appears courtesy" in line or "Contains a sample" in line:
                    continue
                elif "DISC" in line:
                    continue
                elif "Contains samples" in line:
                    continue
                elif "All Rights Reserved" in line:
                    continue
                elif "Credits" in line:
                    continue
                elif "THANK YOU's" in line:
                    continue
                elif "Producer –" in line or "Written-By" in line or "Featuring –" in line or "Vocals –" in line:
                    continue
                elif "Guitar –" in line:
                    continue
                elif ".com" in line or ".net" in line:
                    continue
                elif "intro" == line or "Intro" == line:
                    continue
                elif "1." in line or "2." in line or "3." in line or "4." in line or "5." in line:
                    continue
                elif "6." in line or "7." in line or "8." in line or "9." in line or "0." in line:
                    continue
                elif len(line) < 5:
                    continue
                elif len(line) > 150:
                    continue
                #elif not detect(line) == 'en':
                    #continue
                else:
                    output.write(line)
        output.close()
    input.close()

process()