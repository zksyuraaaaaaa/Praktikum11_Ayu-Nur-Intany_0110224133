class Gempa:
    # konstruktor inisialisasi atribut lokasi dan skala
    def __init__(self,lokasi,skala):
        # atribut
        self.lokasi = lokasi
        self.skala = skala

    # method menentukan dampak skala gempa
    def dampak(self):
        #statment / logika
        if self.skala < 2:
            print("Dampak tidak terasa")
        elif self.skala >= 2 and self.skala <= 4:
            print("Dampak Gempa Bangunan Retak-Retak")
        elif self.skala >= 4 and self.skala <= 6:
            print("Dampak Gempa Bangunan Roboh")
        elif self.skala > 6:
            print("Dampak Gempa Bangunan Roboh dan Berpotensi Tsunami")
        
    #menampilkan lokasi dan skala
        print(f"lokasi gempa: {self.lokasi}")
        print(f"skala gempa: {self.skala}")