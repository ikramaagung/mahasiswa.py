import math

class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius ** 2

# Membuat objek
blt = Lingkaran(7)

# Memanggil metode
print(f"Luas lingkaran dengan radius {blt.radius} cm adalah {blt.hitung_luas():.2f} cm²")
