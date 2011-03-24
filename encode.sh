#! /bin/bash

ffmpeg -f image2 -r 25 -i "$1/screenshot-%d.png" $1/game-jam.mov
