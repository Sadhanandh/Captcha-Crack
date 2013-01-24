#!/usr/bin/python
import Image
import sys
import os
val =0

if len(sys.argv)>1:
	inp = sys.argv[1]
else :
	inp = 'test.gif'
#im = Image.open('%d.gif'%(val))
im = Image.open(inp)
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

if not os.path.exists('output'):
	os.makedirs('output')
img1.save(os.path.join('output',inp))
if not os.path.exists('text_output'):
	os.makedirs('text_output')
dat = open(os.path.join('text_output',inp[:inp.rfind('.')]+'.txt'),"w")


from pytesser import pytesser
text = pytesser.image_file_to_string(os.path.join('output',inp))
print text.strip('\n')
dat.write(text.strip('\n'))
dat.close()
