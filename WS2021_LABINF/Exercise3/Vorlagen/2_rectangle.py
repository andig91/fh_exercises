class rectangle:

    #Konstrutkor; self.<variablenname> ist eine KLassevariable für die ganze KLasse
    def __init__(self, l, b):
        self.b = b
        self.l = l
        l = 20  # existiert l nur im aktuellen BLock/Funktion (__init__)

    #Klassenfunktion
    def flaeche(self):
        return self.l * self.b

    def umfang(self):
        return 2* (self.l + self.b)

    def __str__(self):
        return f'Die Länge ist {self.l}m und die Breite ist {self.b}m\nUmfang: {self.umfang()}m, Fläche: {self.flaeche()}m²'


r = rectangle(10, 8)
print(r)
