#! /bin/bash

ffmpeg -f image2 -r 25 -i "images/gamejam-%d.png" ./game-jam.mov
