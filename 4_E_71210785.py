u = int(input("Dari Suku berapa : ")) 
un = int(input("Suku yang dicari : "))
a = float(input("Angka awal : "))
r = float(input("Rasio : "))

hasil = 0
for n in range(u, un+1):
    suku = a*(r**(n-1)) # Rumus mencari suku
    print(suku)

print('Jumlah suku ke',un, end="")
print ("" ,"=",suku)

# Terimakasih Salam dari binjai mudah"an benar
