import os

for f in os.listdir('.'):
    if '.txt' in f:
        file_test = open(f,mode='r')
        new_file = open('./extracted/'+f+'.txt',mode='a')
        for line in file_test:  
            x = line.split(";")
            new_file.write(x[0])
            new_file.write("\t")
            new_file.write(x[55])
            new_file.write("\n")
        new_file.close()
        file_test.close() 

