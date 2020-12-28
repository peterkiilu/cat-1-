def csc_217_attendance():
        with open("CSC_217_attendance_ week1_30.txt","r")as file1:
                with open("CSC_217_attendance_ week1_end.txt","r")as file2:
                        compmembers=file1.read()
                        itmembers=file2.read()
                        members={compmembers}.union({itmembers})
                file2.close()
        file1.close()
        with open("CSC_217_attendance_week1_with_dublicate.txt","w")as file3:
               for i in members:
                       file3.write(i)
        file3.close()
        memberfinal=set()
        with open("CSC_217_attendance_week1.txt","w")as file1:
                for i in open("CSC_217_attendance_week1_with_dublicate.txt","r"):
                         if i not in memberfinal:
                                 file1.write(i)
                                 memberfinal.add(i)
        file1.close()
        with open("CSC_217_attendance_week1.txt","r")as file1:
                c=file1.read()
csc_217_attendance()
def csc_217_separated():
        with open("CSC_217_attendance_week1.txt","r") as file1:
                separation=[i for i in file1]
                with open("CSC_217_Computer.txt","w") as file3:        
                        for j in separation:
                                if "B135" in j:
                                        file3.write(j)
                file3.close()
                with open("CSC_217_IT.txt","w") as file2:
                        for j in separation:
                                if "B141" in j:
                                        file2.write(j)
                file2.close()
        file1.close()
csc_217_separated ()   
def spacingcomp():
        file=open("CSC_217_Computer.txt","r")
        spaces=[file.read()]
        for i in spaces:
                space=i.replace("-"," ")
        file=open("CSC_217_Computer.txt","w")
        for i in space:
                file.write(i)
spacingcomp()
def CSC_217_Computer():
	with open("CSC_217_Computer.txt","r") as file:
		with open("sample.txt","w") as file1:
			b=[i for i in file]
			for i in b:
				c=i.split()
				for j in c:
					if "B135" in j:
						index=c.index(j)
						c=[c[index]]+c[:index]+c[index+1:]
				student=(" ".join(c))
				file1.write(student+"\n")
		file1.close()
	file.close()
	with open("sample.txt","r") as file:
		b=file.read()
		with open("CSC_217_Computer.txt","w") as file1:
			file1.write(b)
		file1.close()
	file.close()
CSC_217_Computer()
def CSC_217_IT():
	with open("CSC_217_IT.txt","r") as file:
		 with open("sample.txt","w") as file1:
			b=[i for i in file]
			for i in b: 
				c=i.split()
				for j in c:
					if "B141" in j:
						index=c.index(j)
    						c=[c[index]]+c[:index]+c[index+1:]
				student=(" ".join(c))
				file1.write(student+"\n")
			file1.close()
	file.close()
        with open("sample.txt","r") as file:
                b=file.read() 
                with open("CSC_217_IT.txt","w") as file1:
                        file1.write(b)
                file1.close()
        file.close()

CSC_217_IT()

def underscoreit():
     	with open("CSC_217_IT.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("2019","2019 ")
     	with open("CSC_217_IT.txt","w") as file:
     		for i in under:
          		file.write(i)
	with open("CSC_217_IT.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace(" ","_")
	with open("CSC_217_IT.txt","w") as file:
     		for i in under:
          		file.write(i)
	with open("CSC_217_IT.txt","r") as file:
		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("__","_")
	with open("CSC_217_IT.txt","w") as file:
     		for i in under:
        		file.write(i)
	with open("CSC_217_IT.txt","r") as file:
		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("-","")
     	with open("CSC_217_IT.txt","w") as file:
     		for i in under:
          		file.write(i)
     	with open("CSC_217_IT.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("__","_")
     	with open("CSC_217_IT.txt","w") as file:
     		for i in under:
          		file.write(i)
underscoreit()

def underscorecomp():
     	with open("CSC_217_Computer.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("2019","2019 ")
     	with open("CSC_217_Computer.txt","w") as file:
     		for i in under:
          		file.write(i)
     	with open("CSC_217_Computer.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace(" ","_")
     	with open("CSC_217_Computer.txt","w") as file:
     		for i in under:
          		file.write(i)
     	with open("CSC_217_Computer.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace(".","")
     	with open("CSC_217_Computer.txt","w") as file:
     		for i in under:
          		file.write(i)
     	with open("CSC_217_Computer.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("-","")
    	with open("CSC_217_Computer.txt","w") as file:
     		for i in under:
          		file.write(i)
    	with open("CSC_217_Computer.txt","r") as file:
     		underscore=[file.read()]
     		for i in underscore:
          		under=i.replace("__","_")
    	with open("CSC_217_Computer.txt","w") as file:
     		for i in under:
          		file.write(i)
underscorecomp()

def CSC_217_formated():
        with open("CSC_217_Computer.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("2019_","2019, ")
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("2018_","2018, ")
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("2016_","2016, ")
        file.close()
	with open("CSC_217_Computer_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("_"," ")
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("17838/2019, ","17838/2019, Computer 2019")
        file.close()
        with open("CSC_217_Computer_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
        with open("CSC_217_IT.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("2019_","2019, ")
        file.close()
        with open("CSC_217_IT_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
        with open("CSC_217_IT_Week1_final.txt","r") as file:
        	underscore=[file.read()]
        	for i in underscore:
                	under=i.replace("_"," ")
        file.close()
        with open("CSC_217_IT_Week1_final.txt","w") as file:
        	for i in under:
                	file.write(i)
        file.close()
CSC_217_formated()
