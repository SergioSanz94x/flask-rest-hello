from random import randint
name = input("Su nombre?: ")
print(f"{name} tiene 8 intentos para adivinar el numero secreto o su perrito sera secuestrado")
jugar = input("Se atreve a jugar?: ")
out_of_time = input(
    "Da igual lo que responda el tiempo se le acaba y no hay mas opciones... algo que comentar antes de empezar?")
numero_secreto = randint(1, 100)
intentos_restantes = 8
numero_intento = 1
while intentos_restantes > 0:
    mensaje_numero = input(f"intento {numero_intento}/8 ingrese su numero: ")
    numero = int(mensaje_numero)
    if numero < 1 or numero > 100:
        print("☢️​ No juegues con mi paciencia... o tu perrito sufrira las consecuencias 🐶💔​")
    elif numero < numero_secreto:
        print("Mas arriba 👆​")
    elif numero > numero_secreto:
        print("Mas abajo 👇​​")
    else:
        print("Felicidades tu caniche volvera a casa!!🐶​​:v:​")
        break
    numero_intento += 1
    if numero_intento == 9:
        print(
            f"Lo siento {name} el numero era {numero_secreto} 🥵​ su perro sera parte de nuestro asado 😈​")
        break
