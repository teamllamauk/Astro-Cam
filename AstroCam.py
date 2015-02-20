import picamera
from time import sleep

astroCamMode = "setup"
fps = 0
recTime = 0 

def viewFinder()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            
            drawTargetRectSize = (mouseX - 10, mouseY - 10, 20, 20)
            drawTargetRect = 1
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN or event.key == pygame.K_ENTER:
                if mouseX > 0 and mouseY > 0:
                    #Exit function
    
    stream = io.BytesIO() # Capture into in-memory stream
    camera.capture(stream, use_video_port=True, format='raw')
    stream.seek(0)
    stream.readinto(yuv)  # stream -> YUV buffer
    stream.close()
    
    yuv2rgb.convert(yuv, rgb, viewFinder[0], viewFinder[1])
    
    img = pygame.image.frombuffer(rgb[0:(viewFinder[0] * viewFinder[1] * 3)], (viewFinder[0], viewFinder[1]), 'RGB')
    
    screen.blit(img, ((viewFinder[0] - img.get_width() ) / 2, (viewFinder[1] - img.get_height()) / 2))
    
    if drawTargetRect == 1:
        pygame.draw.rect(screen, (255,0,0), drawTargetRectSize, 1)
    
    pygame.display.update() 
    
    
    
    
    
def takePictures()
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
        camera.capture_sequence(['/media/usb0/image%02d.jpg' % i for i in range(int(shots))])
        print 'End recording'


while(True):

    if astroCamMode == "setup":
        fps = raw_input('How many FPS? ') 
        shots = raw_input('Number of shots? ')
        
        astroCamMode = "viewFinder"
    
    elif astroCamMode == "viewFinder":
        print 'View finder mode'
        # View finder code
        # use mouse to select point on screen
        viewFinder()
    
        astroCamMode = "takeImages"
    
    elif astroCamMode == "takeImages":
        
        takePictures()
      
        astroCamMode = "finished"
  
    elif astroCamMode == "finished":
        print 'Finished'
        break
