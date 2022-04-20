# Taking Videos

Take videos with the PiCar-X. 

Save them to your car, export them to your computer, stream them, process them. The options seem endless..

Starting with the code examples in the [Ezblock](https://docs.sunfounder.com/projects/picar-x/en/latest/ezblock/play_with_ezblock.html) and [Python](https://docs.sunfounder.com/projects/picar-x/en/latest/python/play_with_python.html), you can use their code that makes the car drive to understand how you can program the car to drive.


## Starting With Examples

Starting with the examples is a great way to learn how to program the PiCar-X to work with videos.

Start with the [`computer vision`](https://docs.sunfounder.com/projects/picar-x/en/latest/python/python_view_pic.html), [`color detection`](https://docs.sunfounder.com/projects/picar-x/en/latest/python/python_color_detection.html), and [`face detection`](https://docs.sunfounder.com/projects/picar-x/en/latest/python/python_face_detection.html) examples.

To help you get started and to inspire you to create, this project folder contains additional code examples for programming the PiCar-X to work with video.

You may encounter challenges with the FFC connections and servo angles. Consider what limitations the camera has. For instance, how does it perform in different lighting, how can you work with video while it is still on the car, and anything else. 

Feel free to use and modify the code below.

Post videos on Instagram and YouTube and tag us or hashtag #junglememory!

## Forward Video

```python

from picarx import Picarx
import time
import picamera

if __name__ == "__main__":
    try:
        px = Picarx()
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording('forward.h264')
        
        counter = 0
        threshold = 4
        px.set_dir_servo_angle(0)
        px.forward(20)
        time.sleep(4)

        camera.stop_recording()

    finally:
        px.set_dir_servo_angle(0)
        px.forward(0)

```

## Oval Video

```python

from picarx import Picarx
import time
import picamera

if __name__ == "__main__":
    try:
        px = Picarx()
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.start_recording('my_video.h264')
        
        counter = 0
        threshold = 4
        px.set_dir_servo_angle(0)
        px.forward(20)
        time.sleep(2)

        while counter < threshold:
            px.forward(23)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            for angle in range(0,38):
                px.set_dir_servo_angle(angle)
                time.sleep(0.0275)

            px.set_dir_servo_angle(0)
            px.forward(20)
            time.sleep(2)
            counter = counter + 1

        camera.stop_recording()

    finally:
        px.set_dir_servo_angle(0)
        px.forward(0)
```

## Transfer Video From Pi

After recording video with your car, you may want to move the video from your car to another computer. 

Here is how to move a video file from the Raspberry Pi to another computer.

On the destination computer, run the following terminal command.

```python
scp pi@[YOUR_PI_IPADDRESS]:[YOUR_VIDEO_PATH].h264 [VIDEO_DESTINATION_DIR_PATH]
```

Example:

```python
scp pi@111.111.1.11:picar-x/example/my_video.h264 ./Desktop
```

Find the IP address for your Raspberry Pi by running the following command in your terminal on the destination computer.

```python
ping raspberrypi.local
```

The Raspberry Pi and destination computer need to be on the same WiFi network for this to work.

## Convert h264 To mp4

After recording video with your car, you may want to convert the video from `.h264` to `.mp4`. 


On the computer where you want to convert the file, install `ffmpeg`.

```python
pip3 install ffmpeg-python
```

Run the following terminal command.

```python
ffmpeg -r 30 -i [YOUR_VIDEO_PATH] [NEW_VIDEO_PATH]
```

Example:

```python
ffmpeg -r 30 -i my_video.h264 foo.mp4
```


