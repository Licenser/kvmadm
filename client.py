#!/usr/bin/env python
"""
   Example for PyQemu.
   
   Controlling a virtual machine.
"""

import PyQemu
import time


if __name__ == "__main__" :

  # Get a proxy to the server, find out which virtual machines are available
  s = PyQemu.GetProxy("qserver")
  machines = s.Enumerate()
  # List of virtual machine names, as defined in the xml config.
  print machines

  # Get a proxy to the first virtual machine
  m = PyQemu.GetProxy(machines[0])
  
  # Start the virtual machine
  m.Start()
  
  # Wait for it to boot
  time.sleep(15.0)
  
  # Take a large screenshot (always PNG format)
  data = m.ScreenShot()
  if data :
    # Write the PNG data to disk
    file("screen.png","wb").write(data)
  
  # Take a thumbnail (always PNG format)
  data = m.Thumbnail()
  if data :
    file("screen_t.png","wb").write(data)
 
  # Stop the machine 
  m.Stop()
  
  # Discard any changes made
  m.DiscardChanges()

