#!./env/bin/python
import pygame

# import time
import random

pygame.init()

blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

ancho_pantalla = 800
alto_pantalla = 600

dis = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

pygame.display.set_caption("Serpiente de Tono")

juego_acabado = False

bloque_serpiente = 10
velocidad_serpiente = 15

reloj = pygame.time.Clock()

tipo_letra = pygame.font.SysFont("bahnschrift", 25)
tipo_letra_puntos = pygame.font.SysFont("comicsansms", 35)


def tus_puntos(puntos):
    valor = tipo_letra_puntos.render("Puntos: " + str(puntos), True, amarillo)
    dis.blit(valor, [0, 0])


def nuestra_serpiente(bloque_serpiente, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(
            dis, negro, [round(x[0]), round(x[1]), bloque_serpiente, bloque_serpiente]
        )


def mensaje(msg, color):
    mesg = tipo_letra.render(msg, True, color)
    dis.blit(mesg, [round(ancho_pantalla / 6), round(alto_pantalla / 3)])


def bucle_juego():
    juego_acabado = False
    juego_cerrado = False

    x1 = ancho_pantalla / 2
    y1 = alto_pantalla / 2

    cambio_x1 = 0
    cambio_y1 = 0

    lista_serpiente = []
    largo_serpiente = 1

    comida_x = round(random.randrange(0, ancho_pantalla - bloque_serpiente) / 10) * 10
    comida_y = round(random.randrange(0, alto_pantalla - bloque_serpiente) / 10) * 10

    while not juego_acabado:
        while juego_cerrado is True:
            dis.fill(azul)
            mensaje("Has perdido. Q para salir, C para continuar", rojo)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        juego_acabado = True
                        juego_cerrado = False
                    if event.key == pygame.K_c:
                        bucle_juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego_acabado = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambio_x1 = -bloque_serpiente
                    cambio_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    cambio_x1 = bloque_serpiente
                    cambio_y1 = 0
                elif event.key == pygame.K_UP:
                    cambio_y1 = -bloque_serpiente
                    cambio_x1 = 0
                elif event.key == pygame.K_DOWN:
                    cambio_y1 = bloque_serpiente
                    cambio_x1 = 0

        if x1 >= ancho_pantalla or x1 < 0 or y1 >= alto_pantalla or y1 < 0:
            juego_cerrado = True

        x1 += cambio_x1
        y1 += cambio_y1
        dis.fill(azul)
        pygame.draw.rect(
            dis, verde, [comida_x, comida_y, bloque_serpiente, bloque_serpiente]
        )
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)

        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        for x in lista_serpiente[:-1]:
            if x == cabeza_serpiente:
                juego_cerrado = True

        nuestra_serpiente(bloque_serpiente, lista_serpiente)
        tus_puntos(largo_serpiente - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = (
                round(random.randrange(0, ancho_pantalla - bloque_serpiente) / 10) * 10
            )
            comida_y = (
                round(random.randrange(0, alto_pantalla - bloque_serpiente) / 10) * 10
            )
            largo_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()
    quit()


bucle_juego()
