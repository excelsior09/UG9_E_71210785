n = input("Nama : ")
ttl = input("Tempat tanggal lahir : ")

a = n.rsplit(" ",1)
b = ttl.split(" ",1)

print("Haloo!" ,a[1] +"," ,a[0])
print("Anda lahir di" ,b[0] ,"pada tanggal" ,b[1])
