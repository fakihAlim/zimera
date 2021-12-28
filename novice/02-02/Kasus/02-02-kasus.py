# Biasanya programmer akan membuat unit test terlebih dahulu 
# sebelum membuat method / function di Python. 
# Meskipun demikian ada yang berpendapat bahwa hal tersebut 
# hanya akan membuat situasi lebih kompleks. 
# Pada kasus ini kita akan mengimplementasikan unit testing di class yang sudah dibuat. 
# Buatlah unit testing pada source code yang sudah anda kerjakan 
# di berbagai source code yang sudah anda buat sebelum ini. 
# Push ke repo untuk 5 source code saja dan kemudian jelaskan dalam README.md.

def luas_persegi(panjang, lebar):
    return panjang * lebar

def segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def trapesium (sisi_sejajar, tinggi):
    return 0.5 * sisi_sejajar * tinggi

def layang (d1, d2):
    return 0.5 * d1 * d2

def lingkaran(jari):
    return 3.14 * jari * jari

def testing():
    assert luas_persegi(10,10)==100
    assert layang(10,10) == 50
    assert segitiga(10,10) == 50
    assert trapesium(10,10 ) == 50
    assert lingkaran(10) == 314
