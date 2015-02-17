
astroCamMode = "setup"
numberShots = 0

while(True)

  if astroCamMode == "setup":
    numberShots = raw_input('How many images? ') 
    
    astroCamMode = "viewFinder"
    
  elif astroCamMode == "viewFinder":
    
    // View finder code
    // use mouse to select point on screen
    
    astroCamMode = "takeImages"
    
  elif astroCamMode == "takeImages":
    
    // Take Pictures
  
