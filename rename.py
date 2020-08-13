import os

path = './'
dirs = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for dirr in d:
        dirs.append(os.path.join(r, dirr))
ndirs=[]
dirrr=[]
for f in dirs:
    if not f.startswith('./.git') :
        dirrr.append(f)
        w = f.replace('-', ' ')
        w = w.title()
        w = w.replace('.I', '.i')
        w = w.replace('.ipynb_Checkpoints', '.ipynb_checkpoints')
        
        ndirs.append(w) 
for nn,on in zip(dirrr,ndirs):
    try:
#     print(nn,on)
        os.rename(nn,on)
    except Exception as e:
        print(e)


files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.ipynb' in file:
            files.append(os.path.join(r, file))
nfiles = []
for f in files:
    w = f.replace('-', ' ')
    w = w.title()
    w = w.replace('.I', '.i')
    w = w.replace('.ipynb_Checkpoints', '.ipynb_checkpoints')
    nfiles.append(w)
for nn,on in zip(nfiles,files):
    try:
#     print(nn,on)
        os.rename(on,nn)
    except Exception as e:
        print(e)