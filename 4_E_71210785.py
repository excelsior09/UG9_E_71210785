u = int(input("Dari Suku berapa : "))
un = int(input("Suku akhir : "))
a = float(input("Angka awal : "))
r = float(input("Rasio : "))

hasil = 0
for n in range(u, un+1):
    suku = a*(r**(n-1))
    print(suku)

print('Jumlah suku ke',un, end="")
print ("=",suku)
