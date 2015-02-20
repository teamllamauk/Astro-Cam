import picamera
from time import sleep

astroCamMode = "setup"
fps = 0
recTime = 0 

def viewFinder():
    
    

def takePictures():
    


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
