import math

def fibonacchi_search(list, x):
    # Inisialisasi variabel
    fib_k2 = 0  # fib(k-2)
    fib_k1 = 1  # fib(k-1)
    fib_k = fib_k2 + fib_k1  # fib(k)

    # Menentukan bilangan fibonacci terbesar yang <= panjang list
    while fib_k < len(list):
        fib_k2 = fib_k1
        fib_k1 = fib_k
        fib_k = fib_k2 + fib_k1

    # Memulai pencarian
    offset = -1
    while fib_k > 1:
        i = min(offset + fib_k2, len(list) - 1)
        if list[i] < x:
            fib_k = fib_k1
            fib_k1 = fib_k2
            fib_k2 = fib_k - fib_k1
            offset = i
        elif list[i] > x:
            fib_k = fib_k2
            fib_k1 = fib_k1 - fib_k2
            fib_k2 = fib_k - fib_k1
        else:
            return i

    # Kasus khusus jika elemen yang dicari berada pada posisi terakhir
    if fib_k1 and list[offset + 1] == x:
        return offset + 1

    # Jika elemen tidak ditemukan
    return -1

# Contoh penggunaan
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print("Arsel di index", fibonacchi_search(var, "Arsel"))
print("Avivah di index", fibonacchi_search(var, "Avivah"))
print("Daiva di index", fibonacchi_search(var, "Daiva"))
print("Wahyu di index 3 pada kolom ", fibonacchi_search(var[3], "Wahyu"))
print("Wibi di index 3 pada kolom ", fibonacchi_search(var[3], "Wibi"))
