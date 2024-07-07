class Queue:
    DEFAULT_CAPACITY = 10 #początkowa pojemność kolejki

    def __init__(self):
        self._data = [None]*Queue.DEFAULT_CAPACITY #lista o długości 10 złożona z elementów None
        self._size = 0 #długość kolejki (liczba realnych elementów)
        self._front = 0 #indeks pierwszego elementu
        self._back = (self._front + self._size - 1)%(len(self._data))

    def __len__(self):
        return self._size 

    def is_empty(self):
        return self._size == 0 #zwraca True albo False

 
    def first(self):
        if self.is_empty():
            raise ValueError('Queue is empty') #jeżeli kolejka jest pusta zwraca błąd
        return self._data[self._front] #jeżeli nie jest pusta to zwraca pierwszy element (o indeksie 0)
    
    def last(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._data[(self._front + self._size - 1)%(len(self._data))]

    def delete_first(self): #metoda pobierająca (usuwająca) pierwszy element koljeki
        if self.is_empty():
            raise ValueError('Queue is empty')
        value = self._data[self._front] #value = pierwszy element z kolejki
        self._data[self._front] = None #pierwszy element staje się None
        self._front = (self._front+1)%len(self._data) #indeks pierwszego elementu = reszta z dzielenia((stary indeks+1)/długość kolejki)
        self._size -= 1 #rozmiar kolejki (nie None tylko realnych wartości)
        return value #zwrócenie pierwszego elementu

    def delete_last(self): #metoda pobierająca (usuwająca) pierwszy element koljeki
        if self.is_empty():
            raise ValueError('Queue is empty')
        self._back = (self._front + self._size - 1)%(len(self._data))
        value = self._data[self._back] #value = ostatni element z kolejki
        self._data[self._back] = None #ostatni element staje się None
        self._size -= 1 #rozmiar kolejki (nie None tylko realnych wartości)
        return value #zwrócenie ostatniego elementu

    def add_first(self,e): #dodawanie elementu e na koniec kolejki
        if self._size == len(self._data): #jeżeli ilość realnych elementów kolejki == długość ogólna, czyli lista z None'ów się zapełniła
            self.resize(2*len(self._data)) #to powiększ kolejkę dwukrotnie
        avail = (self._front-1)%len(self._data) #indeks końca kolejki = reszta z dzielenia((indeks pierwszego elementu+rozmiar realny)/rozmiar realny)
        self._data[avail] = e #przypisanie e indeksowi avail
        #self._back = (self._front + self._size - 1)%(len(self._data))
        self._size += 1 #informacja o powiększeniu realnej wielkości
        self._front = (self._front-1)%len(self._data)
        

    def add_last(self,e): #dodawanie elementu e na koniec kolejki
        if self._size == len(self._data): #jeżeli ilość realnych elementów kolejki == długość ogólna, czyli lista z None'ów się zapełniła
            self.resize(2*len(self._data)) #to powiększ kolejkę dwukrotnie
        avail = (self._front + self._size)%len(self._data) #indeks końca kolejki = reszta z dzielenia((indeks pierwszego elementu+rozmiar realny)/rozmiar realny)
        self._data[avail] = e #przypisanie e indeksowi avail
        self._size += 1 #informacja o powiększeniu realnej wielkości

    def resize(self,cap): #powiększenie kolejki
        old = self._data #stary rozmiar
        self._data = [None]*cap #rozmiar = nowa długość listy None'ów
        walk = self._front #walk = indeks pierwszego elementu
        for k in range(self._size): #dla k od 0 do ilości realnych elementów
            self._data[k] = old[walk] #nowy indeks = stary indeks olejnych elementów zaczynając od pierwszego elementu
            walk = (1 + walk)%len(old) #walk = indeks kolejnego elementu, czyli to całe to przesunięcie indeksów w lewo
        self._front = 0 #indeks pierwszego elementu = znowu 0 tak jak przy inicjalizacji

k = Queue()
for i in range(11):
    k.add_last(i)

print(k.first())
print(k.last())
print(k.delete_last())
print(k.last())
k.add_last(11)
print(k.delete_last())
k.add_first(111)
#print(k.delete_first())
#k.add_first(123)
k.add_last(112)
k.add_first(222)
print(k.first())
print(k.last())
