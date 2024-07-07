import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def biggest_element(S):
    if len(S)==1:
        return S[0]
    else:
        x = biggest_element(S[1:])
        if x > S[0]: 
            return x
        else:
            return S[0]

n_list = [1,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900]

def create_lists(nr_of_elements):
    test_list = []
    for i in range(len(nr_of_elements)):
        test_list.append(list(np.random.randint(0,10,n_list[i],dtype='int64')))
    return test_list

test_list=create_lists(n_list)

times=[]
for i in range(len(test_list)):
    m_times=[]
    test_list=create_lists(n_list)
    for _ in range(100):
        start = time.time()
        biggest_element(test_list[i])
        end = time.time()
        m_times.append(end-start)
    times.append(sum(m_times)/100)

yt = times




def func(x, a, c):
    return a * x^2 + c

fig, ax = plt.subplots(1,2,figsize=(15,10))
ax[0].plot(n_list,yt,'-o')
ax[1].loglog(n_list,yt)
xd = np.linspace(0,900)
y = func(xd, 2.5, 0.5)
rng = np.random.default_rng()
popt, pcov = curve_fit(func, xd, y)
#plt.plot(n_list, yt, 'b-', label='data')
ax[1].plot(xd, func(xd, *popt))
plt.show()