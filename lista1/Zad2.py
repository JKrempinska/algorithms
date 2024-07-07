import time
import matplotlib.pyplot as plt
import numpy.random as npr
from tqdm import tqdm
 
def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total

def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total

def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex
    sums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
    for j in range(n):
        for k in range(1+j):
            total += A[k]
    if B[i] == total:
        count += 1
    return total

all_times = []

n_list = [100,500,1000,2000,3000,4000,4500,5000]
def create_lists(nr_of_elements):
    test_list = []
    for i in range(len(nr_of_elements)):
        test_list.append(list(npr.randint(0,10,n_list[i],dtype='int64')))
    return test_list


def measure_time(func_name, t_list1=create_lists(n_list), t_list2=create_lists(n_list)):
    times = []
    for i in range(len(t_list1)):
        m_times = []
        t_list1 = create_lists(n_list)
        for _ in tqdm(range(100)):
            start = time.time()
            if func_name != example4:
                func_name(t_list1[i])
            elif func_name == example4:
                t_list2 = create_lists(n_list)
                func_name(t_list1[i],t_list2[i])
            end = time.time()
            m_times.append(end-start)
        times.append(m_times)
    return times

t1 = measure_time(example1)
t2 = measure_time(example2)
t3 = measure_time(example3)
t4 = measure_time(example4)

x1=[]
x2=[]
x3=[]
x4=[]
for i in range(len(n_list)):
    x1.append(sum(t1[i])/100)
    x2.append(sum(t2[i])/100)
    x3.append(sum(t3[i])/100)
    x4.append(sum(t4[i])/100)
y = n_list


fig, ax = plt.subplots(2,1,figsize=(12,15))
ax[0].plot(y,x1, '-o',label='1')
ax[0].plot(y,x2,'-o', label='2')
ax[0].plot(y,x3,'-o', label='3')
ax[0].plot(y,x4,'-o', label='4')
ax[1].loglog(y,x1, label='1')
ax[1].loglog(y,x2, label='2')
ax[1].loglog(y,x3, label='3')
ax[1].loglog(y,x4, label='4')

plt.legend()
plt.show()
