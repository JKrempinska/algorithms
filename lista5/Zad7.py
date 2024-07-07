import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
 
def animate(arr, sorting_func, plot_title, save, save_frames=1000):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title(plot_title)
 
    bars = ax.bar(range(n), arr, align="edge")  
    ax.set_xlim(0, n)
    ax.set_ylim(0, int(1.1*n))
    iteration = [0]
    def _animate(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
   
    anim = FuncAnimation(fig, func=_animate,
        fargs=(bars, iteration), frames=sorting_func, interval=10,
        repeat=False, save_count=save_frames)
    if save:
        writer = PillowWriter(fps=30)
        anim.save(plot_title + ".gif", writer=writer)
    plt.show()

def heap(arr, n, i):
    root = i
    lc = 2*i + 1
    rc = 2*i + 2
    if lc < n  and arr[i] < arr[lc]:
        root = lc
    if rc < n and arr[root] < arr[rc]:
        root = rc
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heap(arr, n, root)
 
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heap(arr, n, i)
        yield arr
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield arr
        heap(arr, i, 0)
        yield arr
 
array = [i for i in range(100)]
random.shuffle(array)
animate(array, heap_sort(array), "heap sort", False)
