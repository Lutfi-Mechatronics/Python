import csv

class FileIO:

    def append(word1=0,word2=0):
        f=open("myfile.txt", "a")
        f.write("\n"+ word1 + "\t" +word2)
        f.close()

    def read():
        print("\nReading File")
        f=open("myfile.txt", "r")
        for line in f:
            print(line.strip("\n\r"))
        f.close()   # Close opened file

    def write(word1=0,word2=0):
        f=open("myfile.txt", "w")
        f.write("\n"+ word1 + "\t\t" +word2)
        f.close()

    def readmod():
        print("\nReading File")
        data = []
        target = []
        with open('myfile.txt') as fobj:
            for line in fobj:
                row = line.split()
                data.append(row[:-1])
                val = target.append(row[1])
                
        return target



