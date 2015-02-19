import picamera
from time import sleep

astroCamMode = "setup"
fps = 0
recTime = 0 

while(True):

    if astroCamMode == "setup":
        fps = raw_input('How many FPS? ') 
        shots = raw_input('Number of shots? ')
        
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
            camera.iso = 100
      
            while camera.analog_gain <= 1:
                time.sleep(0.1)
        
            camera.exposure_mode = 'off'
            g = camera.awb_gains
            camera.awb_mode = 'off'
            camera.awb_gains = g
          
            # Finally, capture an video
            print 'Start recording'
          
            camera.capture_sequence(['image%02d.jpg' % i for i in range(int(shots))])
          
            print 'End recording'
      
        astroCamMode = "finished"
  
    elif astroCamMode == "finished":
        print 'Finished'
        break
