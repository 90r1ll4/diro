import sys
import urllib.request
import urllib.error
he=open("header.txt",'r')
con=he.read()
print(con+"\n")
print("usage: url site-ext options wordlist  \n" )
print("type script name and o to see the options  ")


if str(sys.argv[1])=='o':
     print("v ------> own wordlist \nvv ------> re define common wordlist file \nvvv ------> pre define big wordlist file")
     exit()
wordist="wordlist.txt"
baseurl=str(sys.argv[1])
options=str(sys.argv[3])
ext=str(sys.argv[2])
try:
    wordlist=str(sys.argv[4])
    wordlist=wordlist.strip("-")
except:
    pass

#if options[0] != '-' or wordlist[0] !='-' or ext[0]!='-' :
#    print("You forgot - ")
#    exit()
baseurl=baseurl.strip("-")

ext=ext.strip("-")
opt=options.strip('-')

def enu(baseurl,wordlist,ext):
    file1=open(wordlist,'r')
    found=[]
    for file in file1:
      file=file.strip("\n")
      ext=ext.rstrip()
      baseurl.rstrip('/')
      url=baseurl+"/"+file+"."+str(ext.strip("."))
      try:
        req=urllib.request.urlopen(url)
        if(req.getcode()==200):
          found.append(url)
        req.close()
      except (urllib.error.HTTPError) as e:
         pass

    if(len(found)>0):
       print("the following website exist:\n")
       for filename in found:
            print (filename+"\n")
    else:
        print("No Directory found \n")


if opt=='v':
     print("using your wordlist file... \n")
     enu(baseurl,wordlist,ext)
elif opt=='vv':
     print("using system common file... \n")
     wordlist='wordlist.txt'
     enu(baseurl,wordlist,ext)
elif opt=='vvv':
     print("using system big wordlist file takes more time... \n")
     wordlist='filelist.txt'
     enu(baseurl,wordlist,ext)
