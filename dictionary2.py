name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

bigcount=None
bigword=None
counts=dict()
lst=list()

for line in handle:
    
    if not line.startswith("From:"): continue
    else:
        words=line.split()
        lst.append(words[1])
        
for word in lst:
        counts[word]=counts.get(word,0)+1

for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
