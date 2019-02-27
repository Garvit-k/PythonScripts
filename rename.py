from os import *
i=1
indir = "data\\"
outdir="datare\\"
f=listdir(indir)
for files in f:
    rename(path.join(indir,files),path.join(outdir,str(i)+".jpg"))
    i=i+1
