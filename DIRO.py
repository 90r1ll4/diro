#importing lib
import sys
import urllib.request
import urllib.error
he=open("header.txt",'r')
con=he.read()
print(con+"\n")
print("usage: url  options wordlist file-ext \n" )
print("type script name and o to see the options  ")
try:
   if str(sys.argv[1])=='o':
       print("v ------> own wordlist \nvv ------> re define common wordlist file \nvvv ------> pre define big wordlist file")
       exit()
except:
       pass
if len(sys.argv) !=5:
   print("usage: url  options wordlist file-ext\n" )
   sys.exit(0)
#if not enough arguments are there

baseurl=str(sys.argv[1])
options=str(sys.argv[2])
wordlist=str(sys.argv[3])
ext=str(sys.argv[4])
#if options[0] != '-' or wordlist[0] !='-' or ext[0]!='-' :
#    print("You forgot - ")
#    exit()
baseurl=baseurl.strip("-")
wordlist=wordlist.strip("-")
ext=ext.strip("-")
opt=options.strip('-')
#storing instructions
if opt=='v':
    print("using your wordlist file... \n")
elif opt=='vv':
     print("using system common file... \n")
     worldist='wordlist.txt'
elif opt=='vvv':
       print("using system big wordlist file takes more time... \n")
       wordlist='bigwordlist.txt'

file1=open(wordlist,'r')
found=[]
for file in file1:
  file=file.strip("\n")
  ext=ext.rstrip()
  url=baseurl+file+"."+str(ext.strip("."))
  try:
    req=urllib.request.urlopen(url)
    if(req.getcode()==200):
      found.append(url)
    req.close()
  except (urllib.error.HTTPError,urllib.error.URLError) as e:
     pass

if(len(found)>0):
   print("the following website exist:\n")
   for filename in found:
        print (filename+"\n")
else:
    print("No Directory found \n")
