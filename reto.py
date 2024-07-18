import sys
import time

# Introducción del juego
print("¡Hola! Bienvenido a CHRONO GEM")
time.sleep(1)
print("Juego creado por Ismael Avila y Alejandra Peralvo")
time.sleep(1)
print("Esperamos que el juego sea de tu agrado y puedas ganar ¡Buena suerte!")
time.sleep(2)
print("Hola, viajero. Gracias por venir a ayudarnos a salvar la casa Cordero. Te sumergirás en el siglo XIX para ayudarnos a recuperar las gemas. Lucharás contra los okoropos y devolverás la paz y la tranquilidad.")
time.sleep(4)

fuerza = 0  # Inicializamos fuerza

# Presentación de personajes
print("Para poder continuar, especifica qué personaje de la familia Cordero deseas representar:")
time.sleep(4)
personajes = {
    "a": "Luis Cordero (Piel mestiza, Cabello Castaño, Barba abundante)",
    "b": "Jesus Davila Cordero (Piel mestiza, Cabello negro recogido en dos trenzas, vestido de color vino, Amuletos en las muñecas)",
    "c": "Teresa de Jesus Cordero (Piel mestiza, Cabello y cuello tapados por una sotana de monja)"
}

for key, value in personajes.items():
    print(f"{key}) {value}")

personaje = input("Por favor escoge su personaje (a, b o c): ").strip().lower()

# Poderes
if personaje == 'a':
    print("Hola Luis Cordero, tu habilidad son los conocimientos en botánica.")
    fuerza += 2
elif personaje == 'b':
    print("Hola Jesus Davila Cordero, tu habilidad son los conocimientos literarios.")
    fuerza += 2
elif personaje == 'c':
    print("Hola Teresa de Jesus Cordero, tu habilidad son los conocimientos religiosos.")
    fuerza += 2

# Función para evaluar la respuesta
def evaluar_respuesta(respuesta, respuesta_correcta):
    return respuesta.lower() == respuesta_correcta.lower()

# Función para hacer preguntas
def hacer_pregunta(pregunta_obj):
    global fuerza  # Hacemos que fuerza sea global
    while True:
        print("\n" + pregunta_obj["pregunta"])
        for opcion, respuesta in pregunta_obj["respuestas"].items():
            print(f"{opcion}: {respuesta}")

        respuesta = input("Respuesta: ").strip().upper()

        if evaluar_respuesta(respuesta, pregunta_obj["respuesta_correcta"]):
            print("\n""¡Respuesta correcta!")
            break
        else:
            fuerza -= 0.5  # Restar 0.5 a la fuerza
            print(f"Tu respuesta es incorrecta. Fuerza actual: {fuerza:.1f}. Inténtalo de nuevo.")
            time.sleep(1)

        if fuerza <= 0:
            print("Te has quedado sin fuerza. Fin del juego.")
            sys.exit()  # Terminar el juego si la fuerza llega a 0

def pelea_jefe(fuerza_jefe):
    global fuerza
    if fuerza > fuerza_jefe:
        print('¡Has ganado la pelea!')
    else:
        print('¡Has perdido!')
        print('Espero que en el próximo intento puedas ganar.')
        sys.exit()

# Preguntas del nivel 1: EL CINE
preguntas_nivel1 = [
    {
        "pregunta": "¿Cuál es una de las películas más reconocidas del cine cuencano?",
        "respuestas": {
            "A": "Rosa ",
            "B": "El secreto de Magdalena",
            "C": "A tus espaldas"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Quién es un destacado director de cine cuencano?",
        "respuestas": {
            "A": "Sebastián Cordero ",
            "B": "Tania Hermida ",
            "C": "Tito Jara"
        },
        "respuesta_correcta": "C"
    }
]

print("\nNivel 1: EL CINE")
for pregunta in preguntas_nivel1:
    hacer_pregunta(pregunta)
    fuerza += 3.0

fuerza_jefe = 6
print(f"Tu fuerza actual es: {fuerza}")
time.sleep(1)
print('Oh no, encontraste al primer jefe.')
time.sleep(1)
print('JEFE GRIS')
time.sleep(1)
print(f'Su fuerza es de: {fuerza_jefe}')
time.sleep(1)
pelea_jefe(fuerza_jefe)

# Preguntas del nivel 2: EL JARDIN
preguntas_nivel2 = [
    {
        "pregunta": "¿Cuál es una de las especies de plantas endémicas más conocidas en la región de Cuenca?",
        "respuestas": {
            "A": "Rosa ",
            "B": "Orchidaceae",
            "C": "Quercus"
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el uso tradicional de la planta Achupalla en Cuenca?",
        "respuestas": {
            "A": "Medicinal ",
            "B": "Alimenticio",
            "C": "Ornamental "
        },
        "respuesta_correcta": "A"
    }
]

print("\nNivel 2: EL JARDIN")
for pregunta in preguntas_nivel2:
    hacer_pregunta(pregunta)
    fuerza += 2.5  # Incrementar fuerza por responder correctamente

fuerza_jefe = 10
print(f"Tu fuerza actual es: {fuerza}")
time.sleep(1)
print('Oh no, encontraste al segundo jefe.')
time.sleep(1)
print('JEFE VERDE')
time.sleep(1)
print(f'Su fuerza es de: {fuerza_jefe}')
time.sleep(1)
pelea_jefe(fuerza_jefe)

# Preguntas del nivel 3: LA MUSICA
preguntas_nivel3 = [
    {
        "pregunta": "¿Qué famoso músico cuencano es conocido por su contribución a la música ecuatoriana y especialmente al pasillo?",
        "respuestas": {
            "A": "Julio Jaramillo",
            "B": "Carlos Bonilla Chávez",
            "C": "Abdon Calderón",
            "D": "Luis Enrique Góngora "
        },
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Qué instrumento es comúnmente utilizado en la música tradicional cuencana?",
        "respuestas": {
            "A": "Guitarra",
            "B": "Bandola",
            "C": "Armónica "
        },
        "respuesta_correcta": "B"
    }
]

print("\nNivel 3: LA MUSICA")
for pregunta in preguntas_nivel3:
    hacer_pregunta(pregunta)
    fuerza += 2.5  # Incrementar fuerza por responder correctamente

fuerza_jefe = 15
print(f"Tu fuerza actual es: {fuerza}")
time.sleep(1)
print('Oh no, encontraste al tercer jefe.')
time.sleep(1)
print('JEFE AZUL')
time.sleep(1)
print(f'Su fuerza es de: {fuerza_jefe}')
time.sleep(1)
pelea_jefe(fuerza_jefe)

# Preguntas del nivel 4: EL TEATRO
preguntas_nivel4 = [
    {
        "pregunta": "¿Cuál es una compañía de teatro reconocida en Cuenca?",
        "respuestas": {
            "A": "Teatro Malayerba ",
            "B": "Teatro del Pueblo",
            "C": "Grupo de Teatro Barojo ",
            "D": "Teatro Ensayo"
        },
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿En qué mes se suele celebrar el Festival Internacional de Teatro de Cuenca?",
        "respuestas": {
            "A": "Enero",
            "B": "Abril",
            "C": "Agosto",
            "D": "Octubre"
        },
        "respuesta_correcta": "D"
    }
]

print("\nNivel 4: EL TEATRO")
for pregunta in preguntas_nivel4:
    hacer_pregunta(pregunta)
    fuerza += 2.5  # Incrementar fuerza por responder correctamente

fuerza_jefe = 20
print(f"Tu fuerza actual es: {fuerza}")
time.sleep(1)
print('Oh no, encontraste al cuarto jefe.')
time.sleep(1)
print('JEFE ROJO')
time.sleep(1)
print(f'Su fuerza es de: {fuerza_jefe}')
time.sleep(1)
pelea_jefe(fuerza_jefe)

# Mensaje final
print(f"\n¡Felicidades! Has completado todas las pruebas y derrotado a todos los jefes. Tu fuerza final es de {fuerza}. ¡Gracias por jugar a CHRONO GEM!")
