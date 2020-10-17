#Link to GitHub repository:https://github.com/KR031994/bch5884
#Krittika's 1st programmingproject
import sys
pdbname=sys.argv[1]
f=open(pdbname)
words2=list()
words3=list()
str1=""
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
    #file.write("%-6s%5s %-4s%5s %s%-4s" % (line[0], line[1], line[2], line[3], line[4], line[5]))
print (words2)  
n = input(" Enter choice: 1 for geometric centre and 2 for centre of mass: ")
if n == '1':
                                                        
    for i in range(0,len(words2)):

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
        
        for i in range(0,len(words2)):
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
f1=open("programmingproject.pdb","w")
c=0
for line in lines:
    
    words3 = line.split()

    words3[6]=float(words3[6]);words3[7]=float(words3[7]);words3[8]=float(words3[8])
    
    words3[6]= ("%.3f" %(words3[6]-sumx))
    words3[7]= ("%.3f" %(words3[7]-sumx))
    words3[8]= ("%.3f" %(words3[8]-sumx))
    
    words3[6]=str(words3[6]);words3[7]=str(words3[7]);words3[8]=str(words3[8])
    
    str1 = ' '.join(map(str, words3))

    f1.write(str1)
    f1.write('\n')
     
print ("Done!")

