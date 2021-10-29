import pynput
from playsound import playsound

onHold = True
mouse = pynput.mouse.Controller()
teclado = pynput.keyboard.Controller()

def pressionar(key):

    global onHold
    global mouse
    global teclado

    if(key == pynput.keyboard.Key.f9):
        playsound('ProgramaFechado.mp3')
        return False

    if(key == pynput.keyboard.Key.f10):
        onHold = not onHold

        if(onHold == False):
            playsound('ProgramaFuncionando.mp3')

        else:
            playsound('ProgramaPausado.mp3')

    if(onHold == False):
        if(key == pynput.keyboard.Key.f5):
            print("{0}".format(mouse.position))

        elif(key == pynput.keyboard.Key.f1):
            mouse.move(0, -1)

        elif(key == pynput.keyboard.Key.f2):
            mouse.move(0, 1)

        elif(key == pynput.keyboard.Key.f3):
            mouse.move(-1, 0)

        elif(key == pynput.keyboard.Key.f4):
            mouse.move(1, 0)

        else:
            pass

def soltar(key):
    pass

playsound('ProgramaAberto.mp3')
with pynput.keyboard.Listener(on_press=pressionar, on_release=soltar) as listener:
    listener.join()