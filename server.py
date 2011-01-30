#!/usr/bin/env python
"""
   Simple example of running the QDaemon
   
   bifferos@yahoo.co.uk
"""

import PyQemu

if __name__ == "__main__" :

  qs = PyQemu.QServer()
  qs.Initialise("./qserver.xml")
  qd = PyQemu.QDaemon(qs)
  qd.Loop()  
