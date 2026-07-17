class car:
    def __init__(self, name, farbe, gewicht, max_geschwindigkeit, akkustand, radstand_cm, sensoren):
        self.name = name
        self.farbe = farbe
        self.gewicht = gewicht
        self.max_geschwindigkeit = max_geschwindigkeit
        self.akkustand = akkustand
        self.radstand_cm = radstand_cm
        self.radstand_mm = int(radstand_cm * 10)
        self.sensoren = sensoren
        self.geschwindigkeit = 0

    def akku_pruefen(self):
        if self.akkustand == 100:
            print("Akku voll geladen.")
        elif self.akkustand >= 50:
            print("Akku ist ausreichend geladen.")
        elif 20 <= self.akkustand < 50:
            print("Bitte bald laden.")
        elif self.akkustand < 20:
            print("Akku kritisch! Sofort laden.")
        else:
            print("Fehler: Akkustand unbekannt.")

    def sensor_hinzufuegen(self, name):
        if name not in self.sensoren:
            self.sensoren.append(name)
            print(f"Sensor '{name}' hinzugefügt.")
        else:
            print(f"Sensor '{name}' ist bereits vorhanden.")

    def sensor_anzeigen(self):
        print("Sensoren:")
        for sensor in self.sensoren:
            if sensor == "Ultraschall":
                print(f"- {sensor} (Achtung: Hinderniserkennung aktiv)")
            else:
                print(f"- {sensor}")

    def geschwindigkeit_setzen(self, neu):
        self.geschwindigkeit = neu
        print(f"Geschwindigkeit gesetzt auf {neu} km/h.")
        if neu > self.max_geschwindigkeit:
            diff = neu - self.max_geschwindigkeit
            print(f"Achtung: {diff} km/h über dem Limit!")

    def status_ausgeben(self):
        print(f"Fahrzeug: {self.name}")
        print(f"Farbe: {self.farbe}")
        print(f"Gewicht: {self.gewicht} kg")
        print(f"Max. Geschwindigkeit: {self.max_geschwindigkeit} km/h")
        print(f"Akkustand: {self.akkustand}%")
        print(f"Radstand: {self.radstand_cm} cm / {self.radstand_mm} mm")
        print(f"Sensoren: {', '.join(self.sensoren)}")
        print(f"Aktuelle Geschwindigkeit: {self.geschwindigkeit} km/h")
