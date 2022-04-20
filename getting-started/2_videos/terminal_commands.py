
# Videos

### move file from pi to computer
scp pi@192.168.1.35:picar-x/example/my_video.h264 ./Desktop

### convert file from h264 to mp4
ffmpeg -r 30 -i my_video.h264 foo.mp4
