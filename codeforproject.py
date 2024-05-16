import random

Score = 100

Categories = {     
    "La Rutina Diaria": ["acordar", "acostar", "afeitar", "despedir", "despertar", "dormir", "duchar", "enojar", "ir", "levantar", "llamar", "maquillar", "peinar", "poner", "preocupar", "probar", "quedar", "quitar", "secar", "sentar", "sentir", "vestir", "antes", "luego", "durante", "entonces", "algo", "alguien", "nada", "nadie"],
    "La Comida": ["helado", "mananza", "naranja", "mango", "platano", "uva", "arandano", "fresa", "frambuesa", "cereza", "circula", "limon", "melon", "pera", "pomelo", "aquacate", "pan", "trigo", "cereal", "maiz", "leche", "agua", "zumo", "cafe", "te", "resfrescos", "cafeina", "grasa", "zanahoria", "ajo"],
    "Las Fiestas": ["amistad", "quinceanera", "anversario", "boda", "cumpleanos", "fiesta", "invitado", "invitada", "navidad", "sorpresa", "brindar", "celebrar", "divertirse", "invitar", "regalar", "reirse", "relajarse", "sonreir", "sorprender", "flan", "champan"],
    "En El Consultorio": ["salud", "boca", "brazo", "cabeza", "corazón", "cuello", "cuerpo", "dedo", "estómago", "garganta", "hueso", "nariz", "oído", "ojo", "oreja", "pie", "pierna", "rodilla", "tobillo", "accidente", "antibiótico", "aspirina", "clínica", "consultorio", "dentista", "doctor", "enfermero", "farmacia", "gripe", "hospital"],
    "La Technologia": ["teclado", "ordenador", "computadora", "pantalla", "raton", "escritorio", "icono", "antivirus", "archivo", "altavoce","giga", "impresora", "tableta", "telefono", "movil", "estufa", "cafetera", "congelador", "electrodomestico", "microonda", "lavadora", "lavaplatos", "refrigerador", "secadora", "tostadora", "tecnologia", "luz", "electricidad", "television", "carro"],
    "La Vivienda": ["sotano", "piso", "entrada", "patio", "sala", "comodo", "dormitorio", "cortina", "vecino", "mudarse", "afuera", "alquiler", "atillo", "barrio", "balcon", "comedor", "apartamento", "cocina", "escalera", "garaje", "hogar", "casa", "oficina", "jardin", "pasillo", "alguilar", "condominio", "vivienda", "ventana", "puerta"]
}

CategoryName, SecretWord = random.choice(list(Categories.items()))
SecretWord = random.choice(SecretWord)
Result = ["You Suck Failure", "You Won!"]
CorrectSpots = ["_"] * len(SecretWord)


print("Category:", CategoryName)
print("Please input a word with exactly", len(SecretWord), "letters.")

for turn in range(1, 11):
    print("-----------------------------------------------")
    print("Attempt number:", turn)
    guess = input("Alvidas la palabra: ").lower()
   
    if len(guess) != len(SecretWord) or not guess.isalpha():
        print("Please input a word with exactly", len(SecretWord), "letters.")
        continue

    if guess == SecretWord:
        print(Result[1])
        print("Your final score was: " + str(Score) + "%")
        break

    correct_guesses = 0  
    for i in range(len(SecretWord)):
        if CorrectSpots[i] == guess[i]:
            continue
            
        if guess[i] == SecretWord[i]:
            CorrectSpots[i] = guess[i]
            correct_guesses += 1

    if correct_guesses > 0:
        print("Nice guess!")
    else:
        for i in range(len(SecretWord)):
            if CorrectSpots[i] == '_':
                CorrectSpots[i] = SecretWord[i]
                print("No worries. We opened up " + SecretWord[i] + " to help you out.")
                Score = Score - 10
                break

    print("Your result so far:")
    print(" ".join(CorrectSpots))

else:
    print(Result[0])

print("Refresh the website to play again!")
