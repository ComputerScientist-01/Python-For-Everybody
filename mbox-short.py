fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
word1=[]
for line in fh:
    line=line.rstrip()
    words=line.split()
    if not line.startswith("From:"): continue
    else:
        word1.append(words[1])
        print(words[1])
        count+=1
        #print(words)

print("There were", int(count), "lines in the file with From as the first word")
