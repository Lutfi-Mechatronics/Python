from FileIO import FileIO as io




def main():
    #word1=input("input First Tab word : ")
    #word2=input("input Second Tab word : ")
    #io.append(word1,word2)
    #print(io.readmod())

    filepath = 'myfile.txt'  
    with open(filepath) as fp:  
       line = fp.readline()
       cnt = 1
       while line:
           if cnt == 8:
               print(line.strip())
               print("Line {}: {}".format(cnt, line.strip()))
               break
           #print("Line {}: {}".format(cnt, line.strip()))
           line = fp.readline()
           cnt += 1
        




main()
