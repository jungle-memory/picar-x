
# Terminal Commands For Video

After recording a video with the PiCar-X, you might want to transfer the video from the car to a different computer. You also may want to convert the file format from .h264 to mp4.

Raspberry Pi and Python make it very easy to export and convert files.

Read below.

### Move video from Raspberry Pi to Computer

From a terminal session on the destination computer your, enter the following command.

```
scp pi@[YOUR-CAR-IPADDRESS]:picar-x/example/ [DESTINATION FILEPATH]
```

Example: 

```
scp pi@111.111.1.11:picar-x/example/my_video.h264 ./Desktop
```


### Convert File from h264 to mp4

On the computer where you want to convert the file, install `ffmpeg`.

```
pip3 install ffmpeg-python
```

Convert the video by entering in the terminal the following command.

```
ffmpeg -r 30 -i [ORIGINAL_VIDEO_PATH].h264 [NEW_VIDEO_PATH].mp4
```

Example:

```
ffmpeg -r 30 -i my_video.h264 my_video.mp4
```
