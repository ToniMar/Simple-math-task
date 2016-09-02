##Koodauskoe.py




import sys

##Aliohjelmat
def Fileparser(fileName):
	thelist=[]
	fh=open(fileName,"r")
	lines=fh.read()
	thelist=lines.splitlines()
	try:
		thelist=map(int, thelist)
	except ValueError:
		print "Tiedosto ei ole kelvollinen"
		exit()
	fh.close()
	return thelist
	
def CountSum(numberlist):
	return sum(numberlist)

	
def CountAverage(numberlist):
	average=sum(numberlist)/float (len(numberlist))
	return average
		
def CountMedian(numberlist):
	sortedlist=sorted(numberlist)
	if len(sortedlist)%2!=0:
		half=len(sortedlist)//2
		return sortedlist[half]
	else:
		half=len(sortedlist)//2
		medians=[sortedlist[half],sortedlist[half-1]]
		return medians
	return sortedlist[0]
	
	

def gtcomp(thenumber, Optionalnumber):
	if type(thenumber) is list:
		if Optionalnumber > thenumber[0]:
			print Optionalnumber,"on suurempi kuin", thenumber[0]			
		else:
			print Optionalnumber,"ei ole suurempi kuin", thenumber[0]
		if Optionalnumber > thenumber[1]:
			print Optionalnumber,"on suurempi kuin", thenumber[1]
		else:
			print Optionalnumber,"ei ole suurempi kuin", thenumber[1]
		
		
	else:
		if (Optionalnumber > thenumber):
			print Optionalnumber,"on suurempi kuin", thenumber
			
		else:
			print Optionalnumber,"ei ole suurempi kuin", thenumber


def lgcomp(thenumber, Optionalnumber):
	if type(thenumber) is list:
		if Optionalnumber < thenumber[0]:
			print Optionalnumber,"on pienempi kuin", thenumber[0]			
		else:
			print Optionalnumber,"ei ole pienempi kuin", thenumber[0]
		if Optionalnumber < thenumber[1]:
			print Optionalnumber,"on pienempi kuin", thenumber[1]
		else:
			print Optionalnumber,"ei ole pienempi kuin", thenumber[1]
		
		
	else:
		if (Optionalnumber < thenumber):
			print Optionalnumber,"on pienempi kuin", thenumber
			
		else:
			print Optionalnumber,"ei ole pienempi kuin", thenumber

def eqcomp(thenumber, Optionalnumber):
	if type(thenumber) is list:
		if Optionalnumber == thenumber[0]:
			print Optionalnumber,"on yhta kuin", thenumber[0]			
		else:
			print Optionalnumber,"ei ole yhta kuin", thenumber[0]
		if Optionalnumber == thenumber[1]:
			print Optionalnumber,"on yhta kuin", thenumber[1]
		else:
			print Optionalnumber,"ei ole yhta kuin", thenumber[1]
	else:
		if (Optionalnumber == thenumber):
			print Optionalnumber,"on yhta kuin", thenumber
			
		else:
			print Optionalnumber,"ei ole yhta kuin", thenumber
	
	
	
		

##MAIN##

if __name__ == '__main__':
	AmountofArgs= len(sys.argv)-1
	Argumentlist= (sys.argv[1:])
	if len(Argumentlist)<2:
		print "Poistutaan...."
		exit()
	
	numberlist=Fileparser(Argumentlist[0])

	##Summa
	if Argumentlist[1]=="sum":
		thenumber=CountSum(numberlist)
		print "Summa on ",thenumber
		
	##Keskiarvo
	elif Argumentlist[1]=="avg":
		thenumber=CountAverage(numberlist)
		print "Keskiarvo on ",thenumber

	##Mediaani
	elif Argumentlist[1]=="median":
		thenumber=CountMedian(numberlist)
		if type(thenumber) is list:
			print "Mediaanit ovat ",thenumber[0], thenumber[1] 
		else:
			print "Mediaani on ",thenumber
	else:
		print "Virheellinen input...poistutaan"
		exit()
	
	##Vaihtoehtoiset komennot
	
	if len(Argumentlist)>3:
		Optionalcommand=Argumentlist[2]
		try:
			Optionalnumber=int(Argumentlist[3])
		except ValueError:
			print "Viimeinen valinnainen argumentti ei ole kelvollinen"
			exit()
		
		if Optionalcommand=="gt":
			gtcomp(thenumber, Optionalnumber)
		elif Optionalcommand=="lg":
			lgcomp(thenumber, Optionalnumber)
		elif Optionalcommand=="eq":
			eqcomp(thenumber, Optionalnumber)
		else:
			print "Virheellinen input...poistutaan"
			exit()
	
