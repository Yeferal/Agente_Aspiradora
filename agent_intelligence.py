import threading
import time
import random

def execAgentStupid(sqr1, sqr2):
    pos = 1
    for i in range(3):
        action = random.choice([1,2,3])
        # Accion de la Aspiradora
        if action == 1:
            print(f"agent limpia cuadro")
            time.sleep(1)
        elif action == 2:
            if pos == 1:
                print(f"agent mueve a la derecha")
                pos = 2
                time.sleep(1)
            elif pos == 2:
                print(f"agent mueve a la izquierda")
                pos = 1
                time.sleep(1)
        elif action == 3:
            print("Agente no hace nada")
            time.sleep(1)


def execAgentIntelligence(sqr1, sqr2):
    if sqr1:
        print("Agente limpia el cuadro 1")
        time.sleep(1)
        if sqr2:
            print("Agente se mueve a la izquierda")
            time.sleep(1)
            print("Agente limpia el cuadro 2")
            time.sleep(1)
        else:
            print("Agente no limpia el cuadro 2")
            time.sleep(1)
    elif sqr2:
        print("Agente se mueve a la derecha")
        time.sleep(1)
        print("Agente limpia el cuadro 2")
        time.sleep(1)
    else:
        print("Agente no limpia ninguno de los dos cuadros")
        time.sleep(1)

def actionsIntelligence():
    for i in range(1):
        # Accion del usuario
        sqr2 = random.choice([True, False])
        sqr1 = random.choice([True, False])
        if sqr1 and sqr2:
            print("Usuario ensucia los dos cuadros")
        elif sqr1:
            print("Usuario ensucia el cuadro de la derecha")
        elif sqr2:
            print("Usuario ensucia el cuadro de la izquierda")
        else:
            print("Usuario no ensucia ninguno de los cuadros")

        thread = threading.Thread(target=execAgentIntelligence, args=(sqr1, sqr2))
        thread.start()

        thread.join()
        print("Finalizan el Agente Inteligente")


def actionsEstupid():
    for i in range(1):
        # Accion del usuario
        sqr2 = random.choice([True, False])
        sqr1 = random.choice([True, False])
        if sqr1 and sqr2:
            print("Usuario ensucia los dos cuadros")
        elif sqr1:
            print("Usuario ensucia el cuadro de la izquierda")
        elif sqr2:
            print("Usuario ensucia el cuadro de la derecha")
        else:
            print("Usuario no ensucia ninguno de los cuadros")

        thread = threading.Thread(target=execAgentStupid, args=(sqr1, sqr2))
        thread.start()

        thread.join()
        print("Finalizan el Agente Estupido")



def generateAccition():
    print("========================== Agente Estupid ===========================")
    actionsEstupid()
    print("\n======================== Agente Intelligence ========================")
    actionsIntelligence()



generateAccition()