#-*- coding:utf-8-*-
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) / 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)
#
# print quicksort([3,6,8,10,1,2,1])
#
# x=True;y=False;
# hello='hello';world='world'
# print hello+' '+world
# print '%s %s'%(hello,world)
# print x and y
#
# print hello.capitalize()
# print hello.center(5)
# print hello.replace('l','aa')
# print hello.strip()

# xs=[3,1,3];
# print xs
# x=xs.pop()
# print xs

# nums=range(5)
# print nums
# print nums[:2]

# animals=['cat','dog','monkey'];
# for animal in animals:
#     print animal;
#
# for idx,animal in enumerate(animals):
#     print '#%d,%s'%(idx+1,animal);

# nums=range(5);
# squares=[];
# for x in nums:
#     squares.append(x**2);
# print squares

# nums=[2,3,1,5];
# squares=[x**2 for x in nums if x%2==0];
# print squares
# nums.sort()
# print nums
#
# a='hello world'
# print a.upper()

# d={'cat':'cute','dog':'furry'}
# print d['cat']
# print 'cat' in d
# d['fish']='wet'
# print d['fish']
# print d.get('cats','N/A')
# del d['fish']
# print d

# d={'cat':2,'human':4,'spider':8};
# for animal in d:
#     legs=d[animal];
#     print 'A %s has %d legs'%(animal,legs)
# for animal,legs in d.iteritems():
#     print 'A %s has %d legs'%(animal,legs)

# nums=range(5);
# even_num_to_square={x:x**2 for x in nums if x%2==0}
# print even_num_to_square
# print even_num_to_square.values()

# animals={'cat','dog'};
# print 'cat'in animals;
# animals.add('fish')
# print animals
# print type(animals)
# animals.add('cat');
# print len(animals)
# animals.remove('cat')
# print len(animals)

# animals={'cat','dog','fish'};
# for animal,d in enumerate(animals):
#     print '#%d:%s'%(animal,d)

# from math import sqrt
# nums={int(sqrt(x)) for x in range(30)}
# print nums

# d={(x,x+1):x for x in range(10)};
# print d
# t=(5,6)
# print d[t]

# def  sign(x):
#     if x > 0:
#         return 'positive'
#     elif x < 0:
#         return 'negative'
#     else:
#         return 'zero'
#
# for x in [-1, 0, 1]:
#     print sign(x)

# def hello(name,loud=False):
#     if loud:
#         print 'HELLO,%s' % name.upper()
#     else:
#         print 'HELLO,%s!'% name
#
# hello('bob')
# hello('freb',loud=True)

# class   greeter(object):
#     def __init__(self, name):
#         self.name = name
#     def greet(self,loud=False):
#         if loud:
#             print 'HELLO,%s!'% self.name.upper()
#         else:
#             print 'Hello,%s' % self.name
#
# g=greeter('fred')
# g.greet()
# g.greet(loud=True)
# import matplotlib
# import numpy
# import scipy
# import matplotlib.pyplot as plt
#
# plt.plot([1,2,3])
# plt.ylabel('some numbers')
# plt.show()

# import numpy as np
# # a=np.array([[1,2,3],[4,5,6]])
# # print type(a)
# # print a.shape
# # print a[0],a[1]
# # print a
# a=np.ones((2,2))
# b=np.full((2,2),4)
# print a
# print b
# c=np.eye(2,k=-1)
# print c
# d=np.random.randn(2,3)
# print d

# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8],[9,0,11,12]])
# b=a[:2,1:3]
# print a
# print b
# print a[0,1]
# b[0,0]=111
# print b
# print a[0,1]
# row_r1 = a[1, :]
# row_r2 = a[1:2, :]
# print row_r1, row_r1.shape
# print row_r2, row_r2.shape
# print a[[0,1,2],[0,1,1]]
# print np.array([a[0, 0], a[1, 1], a[2, 1]])
#
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print a
# b = np.array([0, 2, 0])
# print a[np.arange(3), b]
# a[np.arange(3), b] += 10
# print a

# import numpy as np
# a = np.array([[1, 2], [3, 4], [5, 6]])
# print a
# bool_idx = (a > 2)
# print bool_idx
# print a[bool_idx]
# print a[a > 2]

# import numpy as np
# x = np.array([1, 2], dtype=np.int64)
# print x.dtype

# import numpy
# x = numpy.array([[1, 2], [3, 4]], dtype=numpy.float32)
# y = numpy.array([[5, 6], [7, 8]], dtype=numpy.float32)
# print x+y
# print numpy.add(x, y)
# print x-y
# print numpy.subtract(x, y)
# print x*y
# print numpy.multiply(x, y)
# print x/y
# print numpy.divide(x, y)
# print numpy.sqrt(x)


# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
# v = np.array([9, 10])
# w = np.array([11, 12])
# print x.dot(y)
# print np.dot(x, y)
# print np.dot(x, v)
# print x.dot(v)

# x = np.array([1, 2])
# print np.sum(x, axis=0)
# print x
# print x.T
#
# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# v = np.array([1, 0, 1])
# y = np.empty_like(x)
# for i in range(4):
#     y[i, :] = x[i, :] + v
# print y
# vv = np.tile(v, (4, 1))
# y = x + v
# print y

# v = np.array([1, 2, 3])
# w = np.array([3, 4])
# print np.reshape(v, (3, 1))*w
# x = np.array([[1, 2, 3], [4, 5, 6]])
# print x+v
# print (x.T+w).T
# print x+np.reshape(w, (2, 1))
# print x*2


import numpy as np
import os
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt

# path = os.getcwd()                        # 当前脚本路径
# parent_path = os.path.dirname(path)        # 当前脚本上级路径
# path = parent_path+r'\assets\test\dog.jpg'
# img = imread(path)
# print img.dtype, img.shape
# img_tinted = img*[1, 0.95, 0.9]
# img_tinted = imresize(img_tinted, (300, 300))
# imsave(parent_path+r'\assets\test\img_tinted.jpg', img_tinted)
# plt.subplot(1, 2, 1)
# plt.imshow(img)
# plt.subplot(1, 2, 2)
# plt.imshow(img_tinted)
# plt.show()

# import numpy as np
# from scipy.spatial.distance import pdist, squareform
#
# x = np.array([[0, 1], [1, 0], [2, 0]])
# print x
# d = squareform(pdist(x, 'euclidean'))
# print d

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 3*np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.title('sine and cosine')
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.legend(['sine', 'cosine'])
# plt.show()


import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt
import os
# 作者：杜客
# 链接：https://zhuanlan.zhihu.com/p/20894041
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class NearestNeighbor(object):
  def __init__(self):
    pass

  def train(self, X, y):
    """ X is N x D where each row is an example. Y is 1-dimension of size N """
    # the nearest neighbor classifier simply remembers all the training data
    self.Xtr = X
    self.ytr = y

  def predict(self, X):
    """ X is N x D where each row is an example we wish to predict label for """
    num_test = X.shape[0]
    # lets make sure that the output type matches the input type
    Ypred = np.zeros(num_test, dtype = self.ytr.dtype)

    # loop over all test rows
    for i in xrange(num_test):
      # find the nearest training image to the i'th test image
      # using the L1 distance (sum of absolute value differences)
      distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)
      min_index = np.argmin(distances) # get the index with smallest distance
      Ypred[i] = self.ytr[min_index] # predict the label of the nearest example
# 读取包中的数据
def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict
adr = os.getcwd()
adr_parent = os.path.dirname(adr)
# 读取训练集数据
for i in range(5):
    dir_img = adr_parent+r'\assets\cifar-10-batches-py\data_batch_'+str(i+1)
    a = unpickle(dir_img)
    b = a['data']
    d = a['labels']
    if i is 0:
        Xtr_rows = b
        Ytr = d
    else:
        Xtr_rows = np.append(Xtr_rows, b, axis=0)
        Ytr = np.append(Ytr, d, axis=0)
# 读取测试集数据
dir_img1 = adr_parent+r'\assets\cifar-10-batches-py\test_batch'
a1 = unpickle(dir_img1)
Xte_rows = a1['data']
Yte = a1['labels']

nn = NearestNeighbor()
nn.train(Xtr_rows, Ytr)
Yte_predict = nn.predict(Xte_rows)
print 'accuracy:%f'%(np.mean(Yte_predict==Yte))

# c = b[2, :]
# print len(c)
# d = np.reshape(c, (32, 32, 3), order='F')
#
# print d
# plt.imshow(d)
# plt.show()

