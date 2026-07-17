from picar import PiCar

def check_fahrzeug(car: PiCar):
    print(f"\n{car.fahrzeug_status()}")
    car.sensor_status()
    if car.akkustand < 10:
        print("\nWARNUNG: Akkustand ist kritisch!")

def menue(car: PiCar):
    while True:
        print("--------------------------------------------------")
        print("\t||||||--- PiCar-Menü ---||||||")
        print("--------------------------------------------------")
        print("\n\t1. Fahrzeugstatus")
        print("\t2. Beschleunigen")
        print("\t3. Bremsen")
        print("\t4. Sensorstatus")
        print("\t5. Testfahrt \n\t   (automatisch beschleunigen & bremsen)")
        print("\n\t6. Beenden")
        print("\n--------------------------------------------------")


        wahl = input("\nWähle eine Option (1-6): ")

        if wahl == "1":
            print(f"\n{car.fahrzeug_status()}\n")
        elif wahl == "2":
            try:
                wert = int(input("\nGeschwindigkeit erhöhen um km/h: "))
                car.beschleunigen(wert)
            except ValueError:
                print("\nBitte eine gültige Zahl eingeben.")
        elif wahl == "3":
            try:
                wert = int(input("\nGeschwindigkeit verringern um km/h: "))
                car.bremsen(wert)
            except ValueError:
                print("\nBitte eine gültige Zahl eingeben.")
        elif wahl == "4":
            car.sensor_status()
        elif wahl == "5":
            print("\nStarte Testfahrt...")
            while car.akkustand >= 10:
                car.beschleunigen(10)
                print(f"\n{car.fahrzeug_status()}")
                car.bremsen(10)
                car.akku_entladen()
            print("\nTestfahrt beendet: Akku zu niedrig.")
        elif wahl == "6":
            print("\nProgramm beendet.")
            break
        else:
            print("\nUngültige Eingabe, bitte erneut versuchen.")

def main():
    mein_auto = PiCar(
        name = "PiCar",
        farbe = "Schwarz",
        akkustand = 100,
        geschwindigkeit = 0,
        max_geschwindigkeit = 50,
        sensoren=["Ultraschall", "Temperatur", "GPS"]
    )

    check_fahrzeug(mein_auto)
    menue(mein_auto)

if __name__ == "__main__":
    main()
