import csv
from datetime import datetime

class Utils:
    @staticmethod
    def akku_pruefen(akkustand: int) -> bool:
        if akkustand == 100:
            print("\nAkku voll geladen.")
        elif akkustand >= 50:
            print("\nAkku ist ausreichend geladen.")
        elif 20 <= akkustand < 50:
            print("\nBitte bald laden.")
        elif akkustand < 20:
            print("\nAkku kritisch! Sofort laden.")
            return False
        else:
            print("\nFehler! Akkustand kann nicht ermittelt werden.")
        return True

    @staticmethod
    def sensor_detektieren(sensoren_liste: list[str], sensor_name: str) -> bool:
        return sensor_name in sensoren_liste

    @staticmethod
    def neuer_sensor(name: str, einheit: str) -> dict:
        return {"Name": name, "Einheit": einheit}

    @staticmethod
    def aktuelle_zeit() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def verlauf_speichern(datei: str, verlauf: list[str]):
        with open(datei, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for eintrag in verlauf:
                writer.writerow([eintrag])

    @staticmethod
    def verlauf_laden(datei: str) -> list[str]:
        try:
            with open(datei, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                return [zeile[0] for zeile in reader if zeile]
        except FileNotFoundError:
            return []
