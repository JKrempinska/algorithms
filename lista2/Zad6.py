import os
import random
import shutil

def create_dir(path, filename, n):
        if n==0:
            pass
        if random.randint(0,1) == 0:
            dir = 'folder'+str(n)+'1'
            new_path1 = os.path.join(path, dir)
            os.mkdir(new_path1)
            n=n-1
            if random.randint(0,1) == 1:
                file_path1 = os.path.join(new_path1, filename)
                f = open(file_path1,'x')
            if n>0:
                create_dir(new_path1,filename,n)
        elif random.randint(0,1) == 1:
            dir = 'folder'+str(n)+'1'
            new_path1 = os.path.join(path, dir)
            os.mkdir(new_path1)
            dir = 'folder'+str(n)+'2'
            new_path2 = os.path.join(path, dir)
            os.mkdir(new_path2)
            n=n-1
            if random.randint(0,1) == 1:
                file_path1 = os.path.join(new_path1, filename)
                f = open(file_path1,'x')
                file_path2 = os.path.join(new_path2, filename)
                f = open(file_path2,'x')
            if n>0:
                create_dir(new_path1,filename,n)
                create_dir(new_path2,filename,n)         

#create_dir('C:/Users/julka/PWR/3_sem/algorytmy/lista2','file',3)
        
def find_file(path, filename):
    results = []
    for element in os.listdir(path):
        element_path = os.path.join(path, element)
        if os.path.isfile(element_path) and element == filename:
            results.append(element_path)
        elif os.path.isdir(element_path):
            results.extend(find_file(element_path, filename))
    return results

#print(find_file('C:/Users/julka/PWR/3_sem/algorytmy/lista2','file'))

def delete_dir(path,dirname):
    dir_path = os.path.join(path, dirname)
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    else:
        pass

#delete_dir('C:/Users/julka/PWR/3_sem/algorytmy/lista2','folder31')