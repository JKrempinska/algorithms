import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

n_list = [100,500,1000,5000,10000,25000,50000,75000,100000]#,150000,200000,300000,600000,800000,1000000]#,1200000,2000000,4000000,6000000,8000000,10000000]#,100000000]
def create_lists(nr_of_elements):
    test_list = []
    for i in range(len(nr_of_elements)):
        test_list.append(list(np.random.randint(0,10,n_list[i],dtype='int64')))
    return test_list

times=[]
test_list=create_lists(n_list)
for i in range(len(test_list)):
    m_times=[]
    test_list=create_lists(n_list)
    for _ in range(100):
        start = time.time()
        sorted(test_list[i])
        end = time.time()
        m_times.append(end-start)
    times.append(m_times)

y=[]
for i in range(len(n_list)):
    y.append(sum(times[i])/100)

x = n_list
rng = np.random.default_rng()
y_noise = 0.2 * rng.normal(size=)
ydata = y + y_noise
popt, pcov = curve_fit(y,x, ydata)


