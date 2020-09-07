import os

for f in os.listdir('.'):
       if '.txt' in f:
               lines = open(f).readlines()
               open(f, 'w').writelines(lines[2:])