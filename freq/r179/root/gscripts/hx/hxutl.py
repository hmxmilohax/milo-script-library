#****************************************************************************
#
#  Harmonix Music Systems
#  Copyright (c) 1995-2000 Harmonix Music Systems Inc., All Rights Reserved.
#
#****************************************************************************
#
#  $Header: j:\\cvs/Freq/run/gscripts/hx/hxutl.py,v 1.1 2001/09/20 22:03:50 rex Exp $
#
#  $Log: hxutl.py,v $
#  Revision 1.1  2001/09/20 22:03:50  rex
#  *** empty log message ***
#
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

def traceback_str (tb, topstr) :
    "Format a traceback object into a string representation."

    tb_list = traceback.format_tb (tb);
    if (string.find (tb_list[0], "<string>")):
        tb_list[0] = topstr + "\n"
    return string.join (tb_list)

