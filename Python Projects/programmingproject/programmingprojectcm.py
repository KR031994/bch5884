#Link to GitHub repository:https://github.com/KR031994/bch5884
#Krittika's 1st programmingproject
import sys
pdbname=sys.argv[1]
f=open(pdbname)
words2=[]
words3=[]
sum1 = float()
sum2 = float()
sum3 = float()
summ = float()
sumx = float()
sumy = float()
sumz = float()
m = float()
lines=f.readlines()

#Typecasting each element 
for line in lines:
    words = line.split()
    words[1]=int(words[1]);words[5]=int(words[5])
    words[6]=float(words[6]);words[7]=float(words[7]);words[8]=float(words[8]);words[9]=float(words[9]);words[10]=float(words[10])
    words2.append(words)    
print (words2) 

#User's choice of geometric center/center of mass 
n = input(" Enter choice: 1 for geometric centre and 2 for centre of mass: ")
if n == '1':
                                                        
    for i in range(len(words2)):

        words[6]=float(words[6]);words[7]=float(words[7]);words[8]=float(words[8])
        
        sum1 = sum1 + words[6]
        sum2 = sum2 + words[7]
        sum3 = sum3 + words[8]

    sumx = sum1/1337;
    sumy = sum2/1337;
    sumz = sum3/1337;
    print ("%.3f" "%.3f" "%.3f" % (sumx, sumy, sumz))
    
else:                                                  
        
    for line in lines:
        words = line.split()
        
        words[6]=float(words[6]);words[7]=float(words[7]);words[8]=float(words[8])
        
        words2.append(words)
        
        for i in range(len(words2)):
            if words[11]== 'N':
                m = 14;
            elif words[11]== 'C':
                m = 12;
            elif words[11]== 'S':
                m = 32;
            else:
                m = 16;
                
            summ = summ+m;
            
            sum1 = sum1 + (m*words[6])
            sum2 = sum2 + (m*words[7])
            sum3 = sum3 + (m*words[8])
            
        sumx = sum1/summ;
        sumy = sum2/summ;
        sumz = sum3/summ;
        
    print ("%.3f" "%.3f" "%.3f" % (sumx ,sumy ,sumz))

words3=words2.copy()
if n == '1':
    for i in range(len(words2)):
       words3[i][6]= float(words2[i][6]-sumx)
       words3[i][7]= float(words2[i][7]-sumy)
       words3[i][8]= float(words3[i][8]-sumz)
else:
    for i in range(len(words2)):
       words3[i][6]= float(words2[i][6]-sumx)
       words3[i][7]= float(words2[i][7]-sumy)
       words3[i][8]= float(words3[i][8]-sumz)

#Using formatted strings to write the new pdb file for center of mass  
f=open("centeredwithcenterofmass.pdb","w")
for line in words2:
    f.write("%-6s%5d %-4s%3s %-1s%4d %8.3f%8.3f%8.3f%6.2f%6.2f %-2s \n" %(line[0],int(line[1]),line[2],line[3],line[4],int(line[5]),(line[6]),(line[7]),(line[8]),(line[9]),(line[10]),line[11]))    
f.close()     
print ("Done!")

