#Read in and write out a pdb file
#Krittika's pdb file short assignment
import sys
pdbname=sys.argv[1]
f=open(pdbname)
words2=[]
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
for line in words2:
    f1.write("%-6s%5d %-4s%3s %-1s%4d %8.3f%8.3f%8.3f%6.2f%6.2f %-2s \n" %(line[0],int(line[1]),line[2],line[3],line[4],int(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[9]),float(line[10]),line[11]))
f1.close()
print ("Done!")
