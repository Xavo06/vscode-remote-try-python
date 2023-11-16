#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'Hello Wold' to the console
print("Hola Jugador!")
import random

def obtener_opcion_oponente():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def determinar_ganador(jugador, oponente):
    if jugador == oponente:
        return "Empate"
    elif (
        (jugador == "piedra" and oponente == "tijeras") or
        (jugador == "papel" and oponente == "piedra") or
        (jugador == "tijeras" and oponente == "papel")
    ):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    puntaje = 0

    while True:
        print("\nElija una opción: piedra, papel o tijeras")
        jugador = input("Tu elección: ").lower()

        if jugador not in ["piedra", "papel", "tijeras"]:
            print("Opción no válida. Por favor, elija piedra, papel o tijeras.")
            continue

        oponente = obtener_opcion_oponente()

        resultado = determinar_ganador(jugador, oponente)

        print(f"\nTu elección: {jugador}")
        print(f"Elección del oponente: {oponente}")
        print(f"Resultado: {resultado}")

        if resultado == "Ganaste":
            puntaje += 1
        elif resultado == "Perdiste":
            puntaje -= 1

        print(f"\nPuntaje actual: {puntaje}")

        jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            break

    print(f"\n¡Gracias por jugar! Tu puntaje final es: {puntaje}")

if __name__ == "__main__":
    jugar()
