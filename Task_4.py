try:
    file = open("data.txt", "r")
except:
    raise Exception("Cannot open file\n")


def Read_int(filename):
    f=0
    z=0
    x='0'
    while (x!=' ') and (x!=''):
        x=filename.read(1)
        if (x==' ' or x=='') and (f!=0):
            return z
        if (x=='') and (f==0):
            return 'end'        
        elif (x!=' '):
            try:
                x=int(x)
                z=z*10+x
                if (f==0):
                    f+=1            
            except:
                if (x!=' ') and (x!=''):
                    raise Exception("Wrong data\n")
                
            
e1=None
while (e1==None):        
    e1=Read_int(file)
    if (e1=='end'):
        raise Exception("Empty file\n")

e2=None
while (e2==None):        
    e2=Read_int(file)
    if (e2=='end'):
        raise Exception("There is only one element\n")

if (e1==e2):
    raise Exception("Elements are equal\n")


one=0
two=0
c=None
while(c!='end'):
    while (c==None):        
        c=Read_int(file)
        if (c==e1):
            one+=1
        if (c==e2):
            two+=1
        if (c!='end'):
            c=None


if (one>two):
    print("More elements equal to the first\n")
elif (two>one):
    print("More elements equal to the second\n")
else:
    print("The values are equal\n")

file.close()



