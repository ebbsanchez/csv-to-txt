import os, time, csv

def mktime():
    #return 'yyyy/mm/dd'
    return time.strftime('%Y-%m-%d') 

#csv name and make save dir
csvdir = 'test.csv' 
savedir = mktime()+'_'+csvdir[0:-4] 
if not os.path.exists(savedir):
    os.makedirs(savedir)

#write txt 
f = open(csvdir, 'r')
for row in csv.reader(f):
    print row
    tname, data = row[0], row[1]
    f2=open( os.path.join(savedir, tname) + '.txt', 'w')
    f2.write(data)
    f2.close
    
f.close()
