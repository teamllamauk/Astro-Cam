import picamera
from time import sleep

astroCamMode = "setup"
fps = 0
recTime = 0 

while(True):

    if astroCamMode == "setup":
        

        print 'Take image mode' 
        # Take Pictures
        with picamera.PiCamera() as camera:
        
            camera.resolution = (1296, 972)
            camera.framerate = 30
            camera.iso = 100
            
            while camera.analog_gain <= 1:
                time.sleep(0.1)
            
            camera.shutter_speed = camera.exposure_speed
            camera.exposure_mode = 'off'
            g = camera.awb_gains
            camera.awb_mode = 'off'
            camera.awb_gains = g
            
            # speed to 1/33s
            camera.shutter_speed = 30303
            
            # capture images
            print 'Start recording'
            
            camera.exposure_compensation(0)
            camera.capture('image0.png')
            
            camera.exposure_compensation(1)
            camera.capture('image1.png')
            
            camera.exposure_compensation(2)
            camera.capture('image2.png')
            
            camera.exposure_compensation(3)
            camera.capture('image3.png')
            
            camera.exposure_compensation(4)
            camera.capture('image4.png')
            
            camera.exposure_compensation(5)
            camera.capture('image5.png')
            
            camera.exposure_compensation(6)
            camera.capture('image6.png')
            
            camera.exposure_compensation(7)
            camera.capture('image7.png')
            
            camera.exposure_compensation(8)
            camera.capture('image8.png')
            
            camera.exposure_compensation(9)
            camera.capture('image9.png')
            
            camera.exposure_compensation(9)
            camera.capture('image9.png')
            
            camera.exposure_compensation(10)
            camera.capture('image10.png')
            
            camera.exposure_compensation(11)
            camera.capture('image11.png')
            
            camera.exposure_compensation(12)
            camera.capture('image12.png')
            
            camera.exposure_compensation(13)
            camera.capture('image13.png')
            
            camera.exposure_compensation(14)
            camera.capture('image14.png')
            
            camera.exposure_compensation(15)
            camera.capture('image15.png')
            
            camera.exposure_compensation(16)
            camera.capture('image16.png')
            
            camera.exposure_compensation(17)
            camera.capture('image17.png')
            
            camera.exposure_compensation(18)
            camera.capture('image18.png')
            
            camera.exposure_compensation(19)
            camera.capture('image19.png')
            
            camera.exposure_compensation(20)
            camera.capture('image20.png')
            
            camera.exposure_compensation(21)
            camera.capture('image21.png')
            
            camera.exposure_compensation(22)
            camera.capture('image22.png')
            
            camera.exposure_compensation(23)
            camera.capture('image23.png')
            
            camera.exposure_compensation(24)
            camera.capture('image24.png')
            
            camera.exposure_compensation(25)
            camera.capture('image25.png')
          


        print 'Finished'
        break
