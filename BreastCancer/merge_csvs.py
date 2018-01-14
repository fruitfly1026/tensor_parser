fout=open("merged5.csv","a")
for line in open("/home/wafa/BreastCancer/100001.csv"):
    fout.write(line)
# now the rest:    
for num in range(100002,125921):
    f = open("/home/wafa/BreastCancer/"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
