string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


import math

32442343

def distance_from_zero(num):
    if isinstance(num,int) or isinstance(num,float):
        return math.fabs(num)
    else:
        return "Not an integer or float!"

print distance_from_zero(23)