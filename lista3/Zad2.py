import time
from tqdm import tqdm
import matplotlib.pyplot as plt

def pop_time(seq,index):
    start = time.perf_counter()
    seq.pop(index)
    end = time.perf_counter()
    return end-start

index_list = [1,100,1000,10000,100000,1000000,5000000,10000000,100000000]

test_list=[]
n=100000001
for i in tqdm(range(n)):
    test_list.append(0)

times_list = []
for i in tqdm(range(len(index_list))):
    times = 0
    for _ in range(101):
        times += pop_time(test_list,index_list[i])
        test_list.append(0)
    times_list.append(times/101)

print(times_list)
x = index_list      
y = times_list
plt.scatter(x,y)    
plt.show()

#Wniosek: Wszystkie wartości czasu są na podobnym poziomie
