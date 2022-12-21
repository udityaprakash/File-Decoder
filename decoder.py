import time
i=0
list=[]
p=[]
print("..................Welcome To Uditya's Decoder.....................")
print('\n\n')
opk=input('Enter the name of file to decode(.txt):')
lmk=open(opk+".txt","r")
kl=lmk.readlines()
ozp=input('Enter the name of file to save the decoded file: ')
filem=open(ozp+".txt","w")
for mn in kl:
    z=len(mn)
    i=0
    while i<z:
        p=mn[i]
        if p.isalnum():
          if p=='1':
            k=mn[i+1]
            if k=='1':
                j='a'
                list.append(j)
                i=i+2
            elif k=='a':
                j='b'
                list.append(j)
                i=i+2
            elif k=='3':
                j='c'
                list.append(j)
                i=i+2
            elif k=='4':
                j='d'
                list.append(j)
                i=i+2
            elif k=='d':
                j='e'
                list.append(j)
                i=i+2    
            elif k=='6':
                j='f'
                list.append(j)
                i=i+2
            elif k=='7':
                j='g'
                list.append(j)
                i=i+2
            elif k=='g':
                j='h'
                list.append(j) 
                i=i+2   
            elif k=='9':
                j='i'
                list.append(j)
                i=i+2
          elif p=='2':
            k=mn[i+1]
            if k=='0':
                j='j'
                list.append(j)
                i=i+2
            elif k=='j':
                j='k'
                list.append(j)
                i=i+2
            elif k=='2':
                j='l'
                list.append(j)
                i=i+2
            elif k=='3':
                j='m'
                list.append(j)
                i=i+2
            elif k=='m':
                j='n'
                list.append(j)
                i=i+2    
            elif k=='5':
                j='o'
                list.append(j)
                i=i+2
            elif k=='6':
                j='p'
                list.append(j)
                i=i+2
            elif k=='p':
                j='q'
                list.append(j) 
                i=i+2   
            elif k=='8':
                j='r'
                list.append(j)
                i=i+2
            elif k=='9':
                j='s'
                list.append(j)
                i=i+2
          elif p=='3':
            k=mn[i+1]
            if k=='s':
                j='t'
                list.append(j)
                i=i+2
            elif k=='1':
                j='u'
                list.append(j)
                i=i+2
            elif k=='2':
                j='v'
                list.append(j)
                i=i+2
            elif k=='v':
                j='w'
                list.append(j)
                i=i+2
            elif k=='4':
                j='x'
                list.append(j)
                i=i+2
            elif k=='5':
                j='y'
                list.append(j)
                i=i+2
            elif k=='y':
                j='z'
                list.append(j)    
                i=i+2
            elif k=='6':
                j='.'
                list.append(j)
                i=i+2
            elif k=='7':
                j=','
                list.append(j)
                i=i+2    
          elif p=='6':
            k=mn[i+1]
            if k=='5':
                j='A'
                list.append(j)
                i=i+2
            elif k=='A':
                j='B'
                list.append(j)
                i=i+2
            elif k=='7':
                j='C'
                list.append(j) 
                i=i+2   
            elif k=='8':
                j='D'
                list.append(j)
                i=i+2
            elif k=='D':
                j='E'
                list.append(j)
                i=i+2
          elif p=='7':
            k=mn[i+1]
            if k=='0':
                j='F'
                list.append(j)
                i=i+2
            elif k=='1':
                j='G'
                list.append(j)
                i=i+2
            elif k=='G':
                j='H'
                list.append(j)
                i=i+2
            elif k=='3':
                j='I'
                list.append(j)
                i=i+2
            elif k=='4':
                j='J'
                list.append(j)
                i=i+2     
            elif k=='J':
                j='K'
                list.append(j)
                i=i+2
            elif k=='6':
                j='L'
                list.append(j) 
                i=i+2    
            elif k=='7':
                j='M'
                list.append(j)
                i=i+2
            elif k=='M':
                j='N'
                list.append(j)
                i=i+2
            elif k=='9':
                j='O'
                list.append(j)
                i=i+2
          elif p=='8':
            k=mn[i+1]
            if k=='0':
                j='P'
                list.append(j)
                i=i+2
            elif k=='P':
                j='Q'
                list.append(j)
                i=i+2
            elif k=='2':
                j='R'
                list.append(j)
                i=i+2
            elif k=='3':
                j='S'
                list.append(j)
                i=i+2
            elif k=='S':
                j='T'
                list.append(j)
                i=i+2
            elif k=='5':
                j='U'
                list.append(j)
                i=i+2
            elif k=='6':
                j='V'
                list.append(j)
                i=i+2
            elif k=='V':
                j='W'
                list.append(j)
                i=i+2
            elif k=='8':
                j='X'
                list.append(j)
                i=i+2
            elif k=='9':
                j='Y'
                list.append(j)
                i=i+2
          elif p=='9':
            k=mn[i+1]
            if k=='Y':
                j='Z'
                list.append(j)
                i=i+2
          elif p=='3':
            k=mn[i+1]
            if k=='6':
                j='.'
                list.append(j)
                i=i+2
            elif k=='7':
                j=','
                list.append(j)
                i=i+2
          elif p=='5':
            k=mn[i+1]
            if k=='1':
                j='0'
                list.append(j)
                i=i+2
            elif k=='2':
                j='1'
                list.append(j)
                i=i+2
            elif k=='c':
                j='2'
                list.append(j)
                i=i+2
            elif k=='3':
                j='3'
                list.append(j)
                i=i+2
            elif k=='4':
                j='4'
                list.append(j)
                i=i+2    
            elif k=='d':
                j='5'
                list.append(j)
                i=i+2
            elif k=='6':
                j='6'
                list.append(j)
                i=i+2
            elif k=='7':
                j='7'
                list.append(j)
                i=i+2
            elif k=='e':
                j='8'
                list.append(j)
                i=i+2
            elif k=='9':
                j='9'
                list.append(j)
                i=i+2           
        else:
            list.append(p)
            i=i+1
filem.writelines(list)
filem.close()
lmk.close()
print('kindly go to desktop file named "'+ozp+'"')
print('')       
time.sleep(10)
            
            
            
