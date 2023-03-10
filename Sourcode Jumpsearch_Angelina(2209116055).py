import math

def jump_search(arr, x):
    n = len(arr)
    jump = int(math.sqrt(n))
    left, right = 0, 0

    while right < n and arr[right] < x:
        left = right
        right = min(n - 1, right + jump)

    for i in range(left, right + 1):
        if arr[i] == x:
            return i

    return -1

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# mencari Arsel di Index 0
idx = jump_search(var, "Arsel")
if idx != -1:
    print("Arsel di Index", idx)
else:
    print("Arsel tidak ditemukan")

# mencari Avivah di Index 1
idx = jump_search(var, "Avivah")
if idx != -1:
    print("Avivah di Index", idx)
else:
    print("Avivah tidak ditemukan")

# mencari Daiva di Index 2
idx = jump_search(var, "Daiva")
if idx != -1:
    print("Daiva di Index", idx)
else:
    print("Daiva tidak ditemukan")

# mencari Wahyu di Index 3 pada kolom 0
if type(var[3]) == list:
    col = var[3]
    idx = jump_search(col, "Wahyu")
    if idx != -1:
        print("Wahyu di Index 3 pada kolom 0")
    else:
        print("Wahyu tidak ditemukan pada kolom 0")

# mencari Wibi di Index 3 pada kolom 1
if type(var[3]) == list:
    col = var[3]
    idx = jump_search(col, "Wibi")
    if idx != -1:
        print("Wibi di Index 3 pada kolom 1")
else:
        print("Wibi tidak ditemukan pada kolom 1")