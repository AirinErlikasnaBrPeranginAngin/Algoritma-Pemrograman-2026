"""
Nama: Airin Erlikasna Br Perangin Angin
NIM: 2225250196
kelas: 3-B
"""

print ("KALKULATOR KOORDINAT DUA TITIK")
x1 = float (input ("x titik A: "))
y1 = float (input ("y titik A: "))
x2 = float (input ("x titik B: "))
y2 = float (input ("y titik B: "))

dx = x2 - x1 
dy = y2 - y1
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5
xt = (x1 + x2) / 2
yt = (y1 + y2) / 2

print (f"dx = {dx:.2f}")
print (f"dy = {dy:.2f}")
print (f"Jarak = {jarak:.2f}")
print (f"Titik tengan = ({xt:.2f}, {yt:.2f})")