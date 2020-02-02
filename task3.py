arrA = [2, 4, 6, 8, 10, 12, 14, 16, 20, 22, 24, 26, 28, 30, 32]

cof = int(len(arrA) / 2)
print(cof)

arrB = arrA[:cof]
print(arrB, "ArrB")
arrC = arrA[cof:]
print(arrC, "ArrC")