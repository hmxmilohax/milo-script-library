## this is a great module

def doit (x) :
    return x * 2

def crash () :
    return crash2 ()

def crash2 () :
    return 5 / 0

if (__name__ == "__main__"):
    print "3 * 2 =", doit (3)
    
