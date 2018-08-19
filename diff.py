import difflib
hd = difflib.HtmlDiff()
loads = ''
with open('code/three.txt','r') as load:
    loads = load.readlines()
    load.close()

mems = ''
with open('code/four.txt', 'r') as mem:
    mems = mem.readlines()
    mem.close()

with open('htmlout.html','a+') as fo:
    fo.write(hd.make_file(loads,mems))
    fo.close()