from turing import*



def color_filter(im, weight=0.4,tmax=4000,f=0.035,k=0.06,d=0.4):
    arr = np.zeros((im.size[1],im.size[0] , 3))
    for i in range(3):
        constraint = (255-np.array(im, dtype=float)[:,:,i])/255*weight
        A,B = run(constraint,f, k, d, tmax)
        arr[:,:,i] = (1-B/weight*0.99)*255
    return Image.fromarray(np.array(arr,dtype='uint8'), 'RGB')


def grey_filter(im, weight=0.4,tmax=4000,f=0.035,k=0.06,d=0.4):
    im = im.convert('L')
    arr = np.zeros(im.size)
    constraint = (255-np.array(im, dtype=float))/255*weight
    A,B = run(constraint,f, k, d, tmax)
    arr = (1-B/weight*0.99)*255
    return Image.fromarray(np.array(arr,dtype='uint8'), 'L')
