import picamera
from time import sleep

astroCamMode = "setup"
fps = 0
recTime = 0 # Length of recording in seconds

while(True)

  if astroCamMode == "setup":
    fps = raw_input('How many FPS? ') 
    recTime = raw_input('Length of recording (s)? ')
    
    astroCamMode = "viewFinder"
    
  elif astroCamMode == "viewFinder":
      print 'View finder mode'
      # View finder code
      # use mouse to select point on screen
    
      astroCamMode = "takeImages"
    
  elif astroCamMode == "takeImages":
      print 'Take image mode' 
    # Take Pictures
      with picamera.PiCamera() as camera:
      camera.resolution = (1296, 972)
      
      # speed to 1/33s and ISO to 100
      camera.framerate = fps
      camera.shutter_speed = 30303
      camera.exposure_mode = 'off'
      camera.iso = 100
      # Give the camera a good long time to measure AWB
      # (you may wish to use fixed AWB instead)
      sleep(10)
      # Finally, capture an video
      print 'Start recording'
      camera.start_recording('my_video.h264')
      camera.wait_recording(recTime)
      camera.stop_recording()
      print 'End recording'
      
      astroCamMode = "finished"
  
  elif astroCamMode == "finished":
      print 'Finished'
      break
