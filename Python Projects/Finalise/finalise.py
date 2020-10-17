#Read in and write out a pdb file
#Krittika's pdb file short assignment
import sys
pdbname=sys.argv[1]
f=open(pdbname)
words2=[]
words3=list()
str1=""
lines=f.readlines()

#Typecasting each element 
for line in lines:
    words = line.split()
    words[1]=int(words[1]);words[5]=int(words[5])
    words[6]=float(words[6]);words[7]=float(words[7]);words[8]=float(words[8]);words[9]=float(words[9]);words[10]=float(words[10])
    words2.append(words)    
print (words2)
#Using formatted strings to write the new pdb file
f1=open("sample.pdb","w")
c=0
for line in lines:
    
    words3 = line.split()
    words3[6]=str(words3[6]);words3[7]=str(words3[7]);words3[8]=str(words3[8])
    
    str1 = ' '.join(map(str, words3))

    f1.write(str1)
    f1.write('\n')
     
print ("Done")
