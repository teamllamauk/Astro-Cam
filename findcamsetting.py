import time
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
            
            # speed to 1/33s
            camera.shutter_speed = 30303
            
            while camera.analog_gain <= 1:
                time.sleep(0.1)
            
            #camera.shutter_speed = camera.exposure_speed
            camera.exposure_mode = 'off'
            g = camera.awb_gains
            camera.awb_mode = 'off'
            camera.awb_gains = g
            
            # capture images
            print 'Start recording'
            
            camera.exposure_compensation = int(0)
            camera.capture('/media/usb0/image0.png')
            
            camera.exposure_compensation = int(1)
            camera.capture('/media/usb0/image1.png')
            
            camera.exposure_compensation = int(2)
            camera.capture('/media/usb0/image2.png')
            
            camera.exposure_compensation = int(3)
            camera.capture('/media/usb0/image3.png')
            
            camera.exposure_compensation = int(4)
            camera.capture('/media/usb0/image4.png')
            
            camera.exposure_compensation = int(5)
            camera.capture('/media/usb0/image5.png')
            
            camera.exposure_compensation = int(6)
            camera.capture('/media/usb0/image6.png')
            
            camera.exposure_compensation = int(7)
            camera.capture('/media/usb0/image7.png')
            
            camera.exposure_compensation = int(8)
            camera.capture('/media/usb0/image8.png')
            
            camera.exposure_compensation = int(9)
            camera.capture('/media/usb0/image9.png')
            
            camera.exposure_compensation = int(10)
            camera.capture('/media/usb0/image10.png')
            
            camera.exposure_compensation = int(11)
            camera.capture('/media/usb0/image11.png')
            
            camera.exposure_compensation = int(12)
            camera.capture('/media/usb0/image12.png')
            
            camera.exposure_compensation = int(13)
            camera.capture('/media/usb0/image13.png')
            
            camera.exposure_compensation = int(14)
            camera.capture('/media/usb0/image14.png')
            
            camera.exposure_compensation = int(15)
            camera.capture('/media/usb0/image15.png')
            
            camera.exposure_compensation = int(16)
            camera.capture('/media/usb0/image16.png')
            
            camera.exposure_compensation = int(17)
            camera.capture('/media/usb0/image17.png')
            
            camera.exposure_compensation = int(18)
            camera.capture('/media/usb0/image18.png')
            
            camera.exposure_compensation = int(19)
            camera.capture('/media/usb0/image19.png')
            
            camera.exposure_compensation = int(20)
            camera.capture('/media/usb0/image20.png')
            
            camera.exposure_compensation = int(21)
            camera.capture('/media/usb0/image21.png')
            
            camera.exposure_compensation = int(22)
            camera.capture('/media/usb0/image22.png')
            
            camera.exposure_compensation = int(23)
            camera.capture('/media/usb0/image23.png')
            
            camera.exposure_compensation = int(24)
            camera.capture('/media/usb0/image24.png')
            
            camera.exposure_compensation = int(25)
            camera.capture('/media/usb0/image25.png')
          


        print 'Finished'
        break
