import sys
pdbname=sys.argv[1]
f=open(pdbname)
words2 = list()
words4 = list()
words5 = list()
sum = float()
sum1 = float()
sum2 = float()
sum3 = float()
summ = float()
m = float()
str1=""
lines=f.readlines()
xcoordinate = float()
ycoordinate = float()
zcoordinate = float()

#Typecasting each element 
for line in lines:
    words = line.split()
    words[1]=int(words[1])
    words[5]=int(words[5])
    words[6]=float(words[6])
    words[7]=float(words[7])
    words[8]=float(words[8])
    words[9]=float(words[9])
    words[10]=float(words[10])
    
    words2.append(words)    
#print (words2)    
n = input(" Enter choice: 1 for geometric centre and 2 for centre of mass: ")
if n == '1':
    print("geometric")
    
else:
    
    for line in lines:
        words = line.split()
        
        words[6]=float(words[6])
        words[7]=float(words[7])
        words[8]=float(words[8])
        
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
          

        
            sum2= sum2 + (m*words[7])
          

            
            sum3 = sum3 + (m*words[8])
            

        sumx = sum1/summ;
        sumy = sum2/summ;
        sumz = sum3/summ;
        
        #sum = sum1+sum2+sum3;
        #summ = summ+m;
        #sumf= sum/summ;
print (sumx,sumy,sumz)