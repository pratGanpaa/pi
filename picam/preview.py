from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()

# Configure for a default preview
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

# Start the preview and camera
picam2.start_preview(Preview.QTGL)
picam2.start()

# Keep the preview running for a specified duration
time.sleep(100)

# Stop the preview and close the camera
picam2.stop_preview()
picam2.close()
