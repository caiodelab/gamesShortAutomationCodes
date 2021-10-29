import pynput
from time import sleep
from playsound import playsound

mouse = pynput.mouse.Controller()
teclado = pynput.keyboard.Controller()
onHold = True
teclaCtrl = False
posUm = (0, 0)
posDois = (0, 0)
posTres = (0, 0)

def pressionar(key):

    global mouse
    global teclado
    global onHold
    global teclaCtrl
    global posUm
    global posDois
    global posTres

    if(key == pynput.keyboard.Key.ctrl_l):
        teclaCtrl = True

    else:
        pass

    if(teclaCtrl == True):
        if(key == pynput.keyboard.Key.f4):
            onHold = not onHold

            if(onHold == False):
                playsound('ProgramaFuncionando.mp3')

            else:
                playsound('ProgramaPausado.mp3')

        elif(key == pynput.keyboard.Key.f5):
            playsound('ProgramaFechado.mp3')
            teclaCtrl = False
            return False

        else:
            pass

    if(((teclaCtrl == True) and (onHold == False)) and (key == pynput.keyboard.Key.f1)):
        posAnterior = mouse.position

        mouse.click(pynput.mouse.Button.left, 1)
        sleep(0.05)
        mouse.position = (384, 20)
        sleep(0.05)
        mouse.click(pynput.mouse.Button.left, 1)
        sleep(0.05)
        mouse.click(pynput.mouse.Button.left, 1)
        sleep(0.05)
        mouse.position = posAnterior

    elif(((teclaCtrl == True) and (onHold == False)) and (key == pynput.keyboard.Key.f2)):
        posUm = mouse.position
        playsound('pingNormal.mp3')
        sleep(3)
        posDois = mouse.position
        playsound('pingNormal.mp3')
        sleep(3)
        posTres = mouse.position
        playsound('pingSucesso.mp3')

    elif(((teclaCtrl == True) and (onHold == False)) and (key == pynput.keyboard.Key.f3)):
        mouse.position = posUm
        sleep(0.05)
        mouse.click(pynput.mouse.Button.right, 1)
        sleep(0.05)
        mouse.position = posDois
        sleep(0.05)
        mouse.click(pynput.mouse.Button.left, 1)
        sleep(0.05)
        mouse.position = posTres
        sleep(0.05)
        mouse.click(pynput.mouse.Button.left, 1)

    else:
        pass

def soltar(key):
    global teclaCtrl

    if(key == pynput.keyboard.Key.ctrl_l):
        teclaCtrl = False

    else:
        pass

playsound('ProgramaAberto.mp3')
with pynput.keyboard.Listener(on_press=pressionar, on_release=soltar) as listener:
    listener.join()