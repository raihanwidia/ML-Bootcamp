class Cat:
    def __init__(self, name, tipe, umur, makanan):
        self.name = name
        self.tipe = tipe
        self.umur = umur
        self.makanan = makanan
    def meow(self):
        print(f"Kucing {self.name} bilang: Meow!")
    
    def run(self):
        print(f"Kucing {self.name} sedang berlari.")
    
    def eat(self):
        print(f"Kucing {self.name} sedang makan {self.makanan}.")
    def ultah(self, selamat = "Selamat ulang tahun!"):
        self.umur += 1
        print(f"Kucing {self.name} ulang tahun! Sekarang berumur {self.umur} tahun. {selamat}")
    
    def age(self):
        print(f"Kucing {self.name} berumur {self.umur} tahun.")
tom = Cat("Tom", "Anggora", 3, "Ikan")
garfield = Cat("Garfield", "Persia", 4, "Lasagna")
tom.meow()
tom.run()
tom.eat()
tom.ultah()
tom.age()
garfield.meow()
garfield.run()
garfield.eat()
garfield.ultah()
garfield.age()
garfield.ultah("Semoga panjang umur dan sehat selalu!")
print(isinstance(tom, Cat))