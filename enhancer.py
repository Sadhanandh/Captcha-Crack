#!/usr/bin/python
import Image
import sys
import os
val =0

if len(sys.argv)>1:
	inp = sys.argv[1]
else :
	inp = 'test.gif'


if len(sys.argv)>2:
	txt = sys.argv[2]
else :
	txt = 'none'

if len(sys.argv)>3:
	cn = sys.argv[3]
else :
	cn = ""

#im = Image.open('%d.gif'%(val))
im = Image.open("input"+cn+"/"+inp)
im = im.convert("RGB")
start =6
en = im.size[0]-1
box = (start,0,en,25)
img1 = im.crop(box)
x = img1.load()
for i in range(en-start):
	for j in range(25):
		if x[i,j] == (102,102,102):
			x[i,j] = (255,255,255)
		elif x[i,j] ==(153,153,153):
			x[i,j] = (255,255,255)
		else:
			x[i,j] = (0,0,0)


img1 = img1.convert('1')
filn = "Score.txt"
if not os.path.exists('output'+cn):
	os.makedirs('output'+cn)
img1.save(os.path.join('output'+cn,inp))
if not os.path.exists('text_output'+cn):
	os.makedirs('text_output'+cn)
dat = open(os.path.join('text_output'+cn,inp[:inp.rfind('.')]+'.txt'),"w")
filler = open(os.path.join(".",filn),"a")


from pytesser import pytesser
text = pytesser.image_file_to_string(os.path.join('output'+cn,inp))
print text.strip('\n')
dat.write("Guessed "+text.strip('\n')+'\n')
dat.write("Actual "+txt)
if txt==text.strip('\n'):
	dat.write("Success!")
	filler.write("1"+"\n")
else:
	dat.write("Failed!")
	filler.write("0"+"\n")
dat.close()
filler.close()
