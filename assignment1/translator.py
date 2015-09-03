import re
print "Source file name : ",
# takes name of source file
source_file_name=raw_input()


print "Destination file name : ",
#takes name of destination file
destination_file_name=raw_input()


f=open(source_file_name,'r')
f2=open(destination_file_name,"w")

lines=f.readlines()
fin=''

for line in lines:
    strin=''
    l=line.split("\n")
    l=l[0]
#    print l
    strin=l
    strin=re.sub("eax","rax",l)
    strin=re.sub("ebx","rbx",strin)
    strin=re.sub("ecx","rcx",strin)
    strin=re.sub("edx","rdx",strin)
    fin=fin+strin+"\n"
    
""" add=[]
    words=l[0].split()
    for word in words:
        if word=='eax,':
            strin=strin + 'rax,'
        elif word=='ebx,':
            strin=strin + 'rbx,'
        elif word=='ecx,':
            strin=strin + 'rcx,'
        elif word=='edx,':
            strin=strin + 'rdx,'
        elif word=='esp,':
            strin=strin + 'rsp,'
        elif word=='ecx,':
            strin=strin + 'rcx,'
        elif word=='ecx,':
            strin=strin + 'rcx,'
        elif word=='eax':
            strin=strin + 'rax'
        elif word=='ebx':
            strin=strin + 'rbx'
        elif word=='ecx':
            strin=strin + 'rcx'
        elif word=='edx':
            strin=strin + 'rdx'
        elif word=='esp':
            strin=strin + 'rsp'
        elif word=='ecx':
            strin=strin + 'rcx'
        elif word=='ecx':
            strin=strin + 'rcx'
        else:
            strin=strin+word+' ' 
    """

f2.write(fin)

