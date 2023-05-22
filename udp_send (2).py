'''
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2

# Open live webcam video stream on first index(i.e. 0) device
stream = CamGear(source=0, logging=True).start()

# define required FFmpeg optimizing parameters for your writer
# "-vcodec": "mpegts"
#"-vcodec": "libx264"
#"-vcodec": "libx265"
output_params = {
    "-vcodec": "libx264",
    "-tune": "zerolatency",
    "-b:v": "900k",
    "-f": "mpegts"
}

# Define writer with defined parameters and
writer = WriteGear(
    output_filename="udp://172.16.1.35:1234", logging=True, **output_params
)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()
'''

from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2

# Open live webcam video stream on first index(i.e. 0) device
stream = CamGear(source=0, logging=True).start()

# define required FFmpeg optimizing parameters for your writer
# "-vcodec": "mpegts"
#"-vcodec": "libx264"
#"-vcodec": "libx265"
output_params = {
    "-pix_fmt"         : "yuv420p",
    "-c:v"             : "libx264",
    "-preset"          : "ultrafast",
    "-x265-params"     : "crf=23",
    "-strict"          : "experimental",
    "-f"               : "rtp"
}

# Define writer with defined parameters and
writer = WriteGear(
    output_filename="udp://127.0.0.1:5600", logging=True, **output_params
)

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()

# ffmpeg -f v4l2 -i /dev/video0 -pix_fmt yuv420p -c:v libx265 -preset ultrafast -x265-params crf=23 -strict experimental -f rtp udp://172.16.1.35:5600
