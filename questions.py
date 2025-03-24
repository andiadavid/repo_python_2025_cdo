import random
#nueva libreria ingresada
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta 
    print(questions[question_index])
    #se muestran las respuestas posibles
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        # modifico la entrada 
        #user_answer = int(input("Respuesta: ")) - 1
        user_answer = input("Respuesta: ")
        
        # valido si NO es un entero (termino de inmediato con exit status igual a 1)
        #print("el tipo ingresado: ", type(user_answer))
        if user_answer.isdigit(): #importante los parentesis, parametros de la funcion
            user_answer = int(user_answer) - 1
            #print("el tipo ingresado: ", type(user_answer))
            # Se verifica si la respuesta es correcta
            if user_answer == correct_answers_index[question_index]:
                print("¡Correcto!")
                break
            
            #valido si el int esta fuera de rango (termino de inmediato con exit status igual a 1)
            else:
                print("respueta invalida (fuera rango)")
                sys.exit(1) # se necesita importar el sys(libreria)
            
        else:    
            print("respueta invalida (no es un integer)")
            sys.exit(1) # se necesita importar el sys(libreria)
        
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()
#modificacion provando un diff
