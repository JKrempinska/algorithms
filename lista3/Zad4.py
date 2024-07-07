from tqdm import tqdm
import time
import matplotlib.pyplot as plt

nr_of_elements = [100,1000,5000,10000,50000,100000,500000,1000000]
main_list = []
n=1000001
for i in tqdm(range(n)):
    main_list.append(0)

def extend_time(size):
    test_list = []
    list_to_add = main_list[:size]
    start = time.time()
    test_list.extend(list_to_add)
    end = time.time()
    return end - start

def append_time(size):
    test_list = []
    start = time.time()
    for _ in range(size):
        test_list.append(0)
    end = time.time()
    return end - start

times_list_e = []
times_list_a = []
for i in tqdm(range(len(nr_of_elements))):
    times_e = 0
    times_a = 0
    for _ in range(101):
        times_e += extend_time(nr_of_elements[i])
        times_a += append_time(nr_of_elements[i])
    times_list_e.append(times_e/100)
    times_list_a.append(times_a/100)

plt.plot(nr_of_elements, times_list_e, label = 'extend')
plt.plot(nr_of_elements, times_list_a, label = 'append')
plt.legend()
plt.show()