#Calculating RMSD between two pdb files
#Link to repository:https://github.com/KR031994/bch5884.git
import sys 
import math

def	readpdb(pdbfilename1):
	"""Parse pdb and return first as a list of atoms"""
	pdbfile1=open(pdbfilename1,'r')
	lines1=pdbfile1.readlines()
	pdbfile1.close()
	
	#parse the 2FA9noend pdb
	first=[]
	for line in lines1:
		if line[:4]=="ATOM":
			v={}
			v['x']=float(line[30:38])
			v['y']=float(line[38:46])
			v['z']=float(line[46:54])
			first.append(v)
	return first
	
def readpdb(pdbfilename2):
	"""Parse pdb and return second as a list of atoms"""
	pdbfile2=open(pdbfilename2,'r')
	lines2=pdbfile2.readlines()
	pdbfile2.close()
	
	#parse the 2FA9noend2mov pdb
	second=[]
	for line in lines2:
		if line[:4]=="ATOM":
			w={}
			w['x']=float(line[30:38])
			w['y']=float(line[38:46])
			w['z']=float(line[46:54])
			second.append(w)
	return second
    
def rmsd(atomlist1,atomlist2):
    
    corrected = []
    for atomlist1, atomlist2 in zip(atomlist1, atomlist2):
        corrected.append({m: n - atomlist2.get(m, 0) for m, n in atomlist1.items()})
    sumx=sumy=sumz=c=0
    final=float()
    for atom in corrected:
        atom['x']=atom['x']**2
        atom['y']=atom['y']**2
        atom['z']=atom['z']**2
        
        sumx=sumx+atom['x']
        sumy=sumy+atom['y']
        sumz=sumz+atom['z']
        c=c+1
    final=math.sqrt((sumx+sumy+sumz)/c)
    print("Total sum:" , sumx+sumy+sumz)
    print("Total count:", c)
    print("RMSD value :" , final)
    
if __name__=="__main__":
	if len(sys.argv)	!=	3:
		print	("Not Applicable")
		sys.exit()
		
	filename1=sys.argv[1]
	filename2=sys.argv[2]
	
	atomlist1=readpdb(filename1)
	atomlist2=readpdb(filename2)
	rmsd(atomlist1,atomlist2)