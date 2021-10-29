import pynput
from time import sleep
from playsound import playsound

onHold = True
mouse = pynput.mouse.Controller()
teclado = pynput.keyboard.Controller()

def fazendaUm():

    proximoAnimal(1, 1)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 2)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 3)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 3)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 4)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 4)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 1)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)

    proximoAnimal(1, 1)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.15)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()

def fazendaDois():
    pass



def pegarAnimalUm():
    global mouse

    mouse.position = (892, 633)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)

def pegarAnimalDois():
    global mouse

    mouse.position = (906, 492)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)

def colocarFilhote():
    global mouse
    global teclado

    mouse.position = (1336, 440)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.09)
    mouse.position = (624, 311)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.09)
    mouse.position = (765, 340)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(1.2)
    teclado.tap(pynput.keyboard.Key.esc)
    sleep(0.01)
    teclado.tap('s')

def alimentarAnimal():
    global mouse
    global teclado

    mouse.position = (1271, 440)
    sleep(0.09)
    mouse.press(pynput.mouse.Button.left)
    sleep(0.09)
    mouse.position = (719, 539)
    sleep(0.09)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.09)
    teclado.tap(pynput.keyboard.Key.esc)
    sleep(0.01)
    teclado.tap('s')

def tampaoUm():
    global mouse
    global teclado
    posAnterior = mouse.position

    teclado.tap('s')
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.18)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalDois()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)
    mouse.position = posAnterior
    sleep(0.09)
    teclado.tap('s')

def tampaoDois():
    global mouse
    global teclado
    posAnterior = mouse.position

    teclado.tap('s')
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.18)
    proximoAnimal(0, 0)
    sleep(0.09)
    pegarAnimalUm()
    sleep(0.09)
    colocarFilhote()
    sleep(0.09)
    proximoAnimal(0, 0)
    sleep(0.09)
    alimentarAnimal()
    sleep(0.09)
    mouse.position = posAnterior
    sleep(0.09)
    teclado.tap('s')

def gerenciarDiario():
    global mouse
    posAnterior = mouse.position

    mouse.position = (174, 689)
    sleep(0.11)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.11)
    mouse.position = (1397, 440)
    sleep(0.11)
    mouse.press(pynput.mouse.Button.left)
    sleep(0.11)
    mouse.position = (78, 530)
    sleep(0.11)
    mouse.release(pynput.mouse.Button.left)
    sleep(0.11)
    mouse.position = (98, 691)
    sleep(0.11)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.11)
    mouse.position = posAnterior

def gerenciarDiarioUpar():
    global mouse
    posAnterior = mouse.position

    mouse.position = (174, 689)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.09)
    mouse.position = (173, 502)
    sleep(0.16)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.09)
    mouse.position = posAnterior
    sleep(0.16)
    mouse.click(pynput.mouse.Button.left, 1)

def teste():
    global mouse

    mouse.position = (765, 340)
    mouse.move(-115, -68)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(137, -55)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(140, 162)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(140, 162)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(-140, 137)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(-140, 137)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(-115, -68)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

    mouse.position = (765, 340)
    mouse.move(-115, -68)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)
    sleep(1.35)

def testTwo():
    global mouse

    mouse.position = (765, 340)
    mouse.move(137, -55)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.right, 1)

def proximoAnimal(numeroPrimeiraCondicao, numeroSegundaCondicao):
    global mouse
    global teclado

    if(numeroPrimeiraCondicao == 1):
        mouse.position = (765, 340)
        if(numeroSegundaCondicao == 1):
            mouse.move(-115, -68)

        elif(numeroSegundaCondicao == 2):
            mouse.move(137, -55)

        elif(numeroSegundaCondicao == 3):
            mouse.move(140, 162)

        elif(numeroSegundaCondicao == 4):
            mouse.move(-140, 137)

        else:
            pass

        sleep(0.09)
        mouse.click(pynput.mouse.Button.right, 1)
        sleep(1.35)

    else:
        pass

    mouse.position = (747, 316)
    sleep(0.02)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.02)
    mouse.position = (797, 316)
    sleep(0.02)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.02)
    mouse.position = (797, 388)
    sleep(0.02)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.02)
    mouse.position = (747, 388)
    sleep(0.02)
    mouse.click(pynput.mouse.Button.left, 1)

def mensagem():
    global mouse
    global teclado
    posAnterior = mouse.position

    teclado.tap(pynput.keyboard.Key.esc)
    sleep(0.09)
    mouse.position = (1198, 22)
    sleep(0.09)
    mouse.click(pynput.mouse.Button.left, 1)
    sleep(0.09)
    mouse.position = posAnterior

def pressionar(key):

    global onHold
    global mouse

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
        if(key == pynput.keyboard.Key.f1):
            tampaoUm()

        elif(key == pynput.keyboard.Key.f2):
            tampaoDois()

        elif(key == pynput.keyboard.Key.f3):
            gerenciarDiario()

        elif(key == pynput.keyboard.Key.f4):
            gerenciarDiarioUpar()

        elif(key == pynput.keyboard.Key.f5):
            mensagem()

def soltar(key):
    pass

playsound('ProgramaAberto.mp3')
with pynput.keyboard.Listener(on_press=pressionar, on_release=soltar) as listener:
    listener.join()
