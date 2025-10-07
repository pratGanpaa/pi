from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
picam2.start()
frame = picam2.capture_array()
print(frame.shape)  # Should print frame resolution, e.g. (480, 640, 3)
picam2.stop()
