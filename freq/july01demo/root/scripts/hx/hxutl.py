#****************************************************************************
#
#  Harmonix Music Systems
#  Copyright (c) 1995-2000 Harmonix Music Systems Inc., All Rights Reserved.
#
#****************************************************************************
#
#  $Header: j:\\cvs/Freq/run/scripts/hx/hxutl.py,v 1.2 2000/11/27 20:15:34 emalafeew Exp $
#
#  $Log: hxutl.py,v $
#  Revision 1.2  2000/11/27 20:15:34  emalafeew
#  merged SOURCESAFE_BRANCH
#
#  Revision 1.1.2.1  2000/11/27 20:13:56  emalafeew
#  from Sourcesafe
#
#      
#      4     9/08/00 11:52a Eran
#      improved console string printing
#      
#      3     7/25/00 2:59p Eran
#      stuff
#  
#      2     7/25/00 2:57p Eran
#      added MyConsole that help implement an embedded gui console
#            
#****************************************************************************

import string
import traceback
import re

def traceback_str (tb, topstr) :
    "Format a traceback object into a string representation."

    tb_list = traceback.format_tb (tb);
    if (string.find (tb_list[0], "<string>")):
        tb_list[0] = topstr + "\n"
    return string.join (tb_list)
    
import sys
import code
def restoreio () :
    "If anyone screwed up sys.std*, this will restore them back to normal"
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__



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
