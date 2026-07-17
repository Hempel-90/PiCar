class PiCar:
    def __init__(self, name, farbe, akkustand, geschwindigkeit, max_geschwindigkeit, sensoren=None):
        self.name = name
        self.farbe = farbe
        self.akkustand = akkustand  # in Prozent
        self.geschwindigkeit = geschwindigkeit  # aktuell km/h
        self.max_geschwindigkeit = max_geschwindigkeit
        self.sensoren = sensoren if sensoren is not None else []

    def akku_status(self):
        return f"Akkustand: {self.akkustand} %"

    def fahrzeug_status(self):
        return (f"\nFahrzeug '{self.name}' in Farbe {self.farbe}: "
                f"\nAkkustand {self.akkustand} %, \nGeschwindigkeit {self.geschwindigkeit} km/h "
                f"(max. {self.max_geschwindigkeit} km/h), \nSensoren: {', '.join(self.sensoren)}")

    def beschleunigen(self, wert):
        if self.akkustand <= 5:
            print("\nWARNUNG: Akku zu schwach zum Beschleunigen!")
            return
        self.geschwindigkeit += wert
        if self.geschwindigkeit > self.max_geschwindigkeit:
            self.geschwindigkeit = self.max_geschwindigkeit
        print(f"Beschleunigt auf {self.geschwindigkeit} km/h.")

    def bremsen(self, wert):
        self.geschwindigkeit -= wert
        if self.geschwindigkeit < 0:
            self.geschwindigkeit = 0
        print(f"Gebremst auf {self.geschwindigkeit} km/h.")

    def akku_entladen(self):
        if self.akkustand > 0:
            self.akkustand -= 1
            if self.akkustand < 0:
                self.akkustand = 0

    def sensor_status(self):
        if not self.sensoren:
            print("Keine Sensoren installiert.")
        else:
            for sensor in self.sensoren:
                print(f"Sensor '{sensor}': OK")
