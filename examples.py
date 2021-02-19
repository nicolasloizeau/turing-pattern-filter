from filters import*



fname = 'centralpark.jpg'
size = 600
d = 0.3*size/400
im = Image.open(fname)
ratio = size/im.size[0]
im = im.resize((size, int(ratio*im.size[1])))
im = grey_filter(im,d=d,tmax=5000)
im.save('centralpark_2.png')


fname = 'bach.jpg'
size = 400
d = 0.4*size/400
im = Image.open(fname)
ratio = size/im.size[0]
im = im.resize((size, int(ratio*im.size[1])))
im = grey_filter(im,d=d)
im.save('bach_2.png')


fname = 'mozart.jpg'
size = 400
d = 0.6*size/400
im = Image.open(fname)
ratio = size/im.size[0]
im = im.resize((size, int(ratio*im.size[1])))
im = color_filter(im)
im.save('mozart_2.png')
