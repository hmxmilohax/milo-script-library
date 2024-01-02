import glob
import os.path
import re
import string
import sys

class Range:
    def __init__ (self, name, lo, hi, filename=None):
        self.lo = int(lo)
        self.hi = int(hi)
        self.name = name
        self.filename = filename

    def __str__ (self):
        if self.filename != None:
            return "[%20s] %10s %d--%d" % (self.filename, self.name, self.lo, self.hi)
        else:
            return "%10s %d--%d" % (self.name, self.lo, self.hi)

    def __cmp__ (self, other):
        return cmp (self.lo, other.lo)

class Msg:
    def __init__ (self, name, num, filename=None):
        self.num = int(num)
        self.name = name
        self.filename = filename

    def __str__ (self):
        if self.filename != None:
            return "[%20s] %10s %d" % (self.filename, self.name, self.num)
        else:
            return "%10s %d" % (self.name, self.num)

    def __cmp__ (self, other):
        return cmp (self.num, other.num)

range_re = re.compile (r"DISPATCH_RANGE\s*\((\w+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)")
declare_re = re.compile (r"HX_DECLARE_MSG\s*\(\s*(\w+)\s*,\s*(\d+)\s*\)")

dirs = sys.argv[1:]
files = []
ranges = []
msgs = []

def visit (f):
    filename = os.path.basename(f)
    for line in open(f).readlines():
        if line[0] == '#':
            match = range_re.search(line)
            if match:
                name, lo, hi = match.groups()
                ranges.append (Range (name, lo, hi, filename))
        elif string.find(line, "HX_DECLARE_MSG") != -1:
            match = declare_re.search(line)
            if match:
                name, num = match.groups()
                msgs.append (Msg (name, num, filename))

def lookit (arg, dirname, names):
    for name in names:
        if name[-4:] == ".cpp" or name[-2:] == ".h":
            visit (os.path.join (dirname, name))
        
for dir in dirs:
    os.path.walk (dir, lookit, None)

errormsg = ""

ranges.sort()
lastrange = Range("Happy", -2, -1)
for range in ranges:
    if lastrange.hi > range.lo:
        errormsg = errormsg + ("  Overlapping ranges!\n    %s\n    %s\n" % (lastrange, range))
    lastrange = range
    print range
print

msgs.sort()
lastmsg = Msg("Happy", -1)
for msg in msgs:
    if lastmsg == msg:
        errormsg = errormsg + ("  Duplicate messages!\n    %s\n    %s\n" % (lastmsg, msg))
    lastmsg = msg
    print msg

if len(errormsg):
    print "\nErrors found:"
    sys.exit (errormsg)
