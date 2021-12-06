import string    
import sys
import code
def restoreio () :
    "If anyone screwed up sys.std*, this will restore them back to normal"
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

#****************************************************************************
#
#  Harmonix Music Systems
#  Copyright (c) 1995-2000 Harmonix Music Systems Inc., All Rights Reserved.
#
#****************************************************************************

class MyConsole (code.InteractiveInterpreter):
    
    def __init__ (self, locals):
        "Constructor "
        code.InteractiveInterpreter.__init__ (self, locals)
        self.mBuffer    = ""
        self.mOldStdOut = None

    def grabOut (self):
        if (self.mOldStdOut == None):
            self.mOldStdOut = sys.stdout
            sys.stdout = self;
        
    def releaseOut (self):
        if (self.mOldStdOut != None):
            sys.stdout = self.mOldStdOut;
            self.mOldStdOut = None
    
    def getOut (self):
        tmp = self.mBuffer
        self.mBuffer = ""
        return tmp

    def write (self, data):
        data = string.replace (data, r'\012', '\n') # print actual newlines
        self.mBuffer = self.mBuffer + data

    def run (self, source):
        self.grabOut ()
        retval = self.runsource (source)
        self.releaseOut ()
        return retval
