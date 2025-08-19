import time
from pynput import keyboard
import sys

# Zeitfenster in Sekunden, um eine Eingabe als zusammenhängenden Scan zu erkennen
SCAN_TIMEOUT = 0.3


class LiveBarcodeListener:
    def __init__(self):
        self.buffer = []
        self.last_press_time = time.time()

    def on_press(self, key):
        current_time = time.time()

        # Puffer zurücksetzen, wenn die Eingabepause zu lang war (Beginn eines neuen Scans)
        if current_time - self.last_press_time > SCAN_TIMEOUT:
            # Wenn der vorherige Puffer nicht leer war, mache einen Zeilenumbruch
            if self.buffer:
                print("\n--- Neue Sequenz erkannt ---\n")
            self.buffer = []

        self.last_press_time = current_time

        # Füge die aktuelle Taste (lesbar formatiert) dem Puffer hinzu
        try:
            key_representation = key.char
        except AttributeError:
            key_representation = f'<{key.name}>'

        # Ignoriere 'None' Werte, die bei manchen Tasten-Events auftreten können
        if key_representation:
            self.buffer.append(key_representation)

        # 🔴 Live-Anzeige: Gib den aktuellen Puffer aus, ohne eine neue Zeile zu beginnen
        # Das \r (Carriage Return) setzt den Cursor an den Zeilenanfang
        # Ein Leerzeichen am Ende löscht eventuelle Reste der vorherigen, längeren Zeile
        sys.stdout.write(f"Live-Input: {' '.join(self.buffer)}      \r")
        sys.stdout.flush()

        # Wenn die Enter-Taste gedrückt wird, schließe die Zeile sauber ab
        if key == keyboard.Key.enter:
            print()  # Springe zur nächsten Zeile, damit die Ausgabe nicht überschrieben wird
            # Optional: Hier könnte man eine Zusammenfassung drucken


# --- Start des Programms ---
print("Live Barcode-Debugger gestartet. Warte auf Eingabe...")
print("Jeder Tastenanschlag wird sofort angezeigt. Drücke 'Esc' zum Beenden.\n")

listener = LiveBarcodeListener()
with keyboard.Listener(on_press=listener.on_press) as k_listener:
    k_listener.join()