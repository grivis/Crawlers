import os
inp = "/home/grigory/MyStem/input_texts"
lst = os.listdir(inp)
#print(lst)
for fl in lst:
    os.system(r"/home/grigory/MyStem/mystem " + inp + os.sep + fl + " /home/grigory/MyStem/output_texts" + os.sep + fl)
