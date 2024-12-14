#!/usr/bin/env python3
import re

def rearange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if(result is None):
        return name
    return "{} {}".format(result[2],result[1])


#print(rearange_name("Jaroenchokwittaya, Nutthawut"))
#print(rearange_name(""))
print(rearange_name("Jordan, Michael B."))