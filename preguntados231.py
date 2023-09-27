import pygame
from preguntas import lista
from constantes import *

lista_preguntas = []
lista_opcion_a = []
lista_opcion_b = []
lista_opcion_c = []
lista_respuestas_correcta = []

for i in lista:
    lista_preguntas.append(i["pregunta"])
    lista_opcion_a.append(i["a"])
    lista_opcion_b.append(i["b"])
    lista_opcion_c.append(i["c"])
    lista_respuestas_correcta.append(i["correcta"])

titulo = ""
pregunta = ""
respuesta_a = ""
respuesta_b = ""
respuesta_c = ""
posicion = 0
puntaje = 0
errores = 0
respuesta_correcta = True
posicion_imagen = [30,100]

pygame.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) 
pygame.display.set_caption("Pygame") 

imagen = pygame.image.load("Preguntados.jpg") 
imagen = pygame.transform.scale(imagen,(80,80))

fuente = pygame.font.SysFont("Arial", 30)

texto_reiniciar = fuente.render("REINICIAR", True,COLOR_GRIS)
texto_siguente_preg = fuente.render("PREGUNTA", True,COLOR_GRIS)
texto_puntos = fuente.render("SCORE: ", True,COLOR_GRIS)
texto_pregunta = fuente.render(str(pregunta), True,COLOR_GRIS)
texto_puntaje = fuente.render(str(puntaje), True,COLOR_GRIS)


flag_correr = True
while flag_correr:

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN :
            posicion_click = list(evento.pos)
            print(posicion_click)

            if (posicion_click[0] > 300 and posicion_click[0] < 500) and (posicion_click[1] > 20 and posicion_click[1] < 120):
                if posicion >= len(lista_preguntas):
                    posicion = 0
                    puntaje = 0
                
                else:
                    pregunta = lista_preguntas[posicion]
                    respuesta_a = lista_opcion_a[posicion]
                    respuesta_b = lista_opcion_b[posicion]
                    respuesta_c = lista_opcion_c[posicion]

                    texto_pregunta = fuente.render(str(pregunta), True,COLOR_GRIS)
                    texto_puntos = fuente.render("SCORE: ", True,COLOR_GRIS)
                    texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_GRIS)
                    texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_GRIS)
                    texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_GRIS)
                    errores = 0
                    respuesta_correcta = False

            if (posicion_click[0]>300 and posicion_click[0]<500) and (posicion_click[1]>470 and posicion_click[1]<590):
                puntaje = 0
                posicion = 0
                errores = 0
                pregunta = lista_preguntas[posicion]
                respuesta_a = lista_opcion_a[posicion]
                respuesta_b =  lista_opcion_b[posicion]
                respuesta_c = lista_opcion_c[posicion]

                texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
                texto_puntos = fuente.render("SCORE: ", True,COLOR_GRIS)
                texto_puntaje = fuente.render(str(puntaje), True,COLOR_GRIS)
                texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_GRIS)
                texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_GRIS)
                texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_GRIS)


            elif lista_respuestas_correcta[posicion] == "a":
                if (posicion_click[0]> 20 and posicion_click[0] < 120) and (posicion_click[1] > 340 and posicion_click[1] < 390):
                    respuesta_correcta = True
                    if errores < 2:
                        puntaje = puntaje + 10
                        texto_puntaje = fuente.render(str(puntaje), True,COLOR_GRIS)
                        posicion = posicion + 1

                elif (posicion_click[0]>300 and posicion_click[0]<400) and (posicion_click[1]>340 and posicion_click[1]<390):
                    errores = errores + 1
                    respuesta_b = ""
                    texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_GRIS)

                elif (posicion_click[0] > 595 and posicion_click[0] < 680) and (posicion_click[1]>340 and posicion_click[1]<390):
                    errores = errores + 1
                    respuesta_c = ""
                    texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_GRIS)

                if errores == 2:
                    posicion = posicion + 1


            elif lista_respuestas_correcta[posicion] == "b":
                if (posicion_click[0]>300 and posicion_click[0]<400) and (posicion_click[1]>340 and posicion_click[1]<390):
                    respuesta_correcta = True
                    if errores < 2:
                        puntaje = puntaje + 10
                        texto_puntaje = fuente.render(str(puntaje), True,COLOR_GRIS)
                        posicion = posicion + 1

                elif (posicion_click[0]> 20 and posicion_click[0] < 120) and (posicion_click[1] > 340 and posicion_click[1] < 390):
                    errores = errores + 1
                    respuesta_a = ""
                    texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_GRIS)

                elif (posicion_click[0] > 595 and posicion_click[0] < 680) and (posicion_click[1]>340 and posicion_click[1]<390):
                    errores = errores + 1
                    respuesta_c = ""
                    texto_respuesta_c = fuente.render(str(respuesta_c), True,COLOR_GRIS)

                if errores == 2:
                    posicion = posicion + 1


            elif lista_respuestas_correcta[posicion] == "c":
                if (posicion_click[0] > 595 and posicion_click[0] < 680) and (posicion_click[1]>340 and posicion_click[1]<390):
                    respuesta_correcta = True
                    if errores < 2:
                        puntaje = puntaje + 10
                        texto_puntaje = fuente.render(str(puntaje), True,COLOR_GRIS)
                        posicion = posicion + 1

                elif (posicion_click[0]> 20 and posicion_click[0] < 120) and (posicion_click[1] > 340 and posicion_click[1] < 390):
                    errores = errores + 1
                    respuesta_a = ""
                    texto_respuesta_a = fuente.render(str(respuesta_a), True,COLOR_GRIS)

                elif (posicion_click[0]>300 and posicion_click[0]<400) and (posicion_click[1]>340 and posicion_click[1]<390):
                    errores = errores + 1
                    respuesta_b = ""
                    texto_respuesta_b = fuente.render(str(respuesta_b), True,COLOR_GRIS)

                if errores == 2:
                    posicion = posicion + 1



    pantalla.fill(COLOR_VERDE)
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,20,200,100))
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,440,200,100))

    if respuesta_correcta == False and errores < 2:
        pantalla.blit(texto_respuesta_a,(20,350))
        pantalla.blit(texto_respuesta_b,(300,350))
        pantalla.blit(texto_respuesta_c,(600,350))

    pantalla.blit(imagen, (posicion_imagen))
    pantalla.blit(texto_siguente_preg,(315,50))
    pantalla.blit(texto_reiniciar,(315,470))
    pantalla.blit(texto_pregunta,(20,200))

    pantalla.blit(texto_puntos,(310,120))
    pantalla.blit(texto_puntaje,(310,160))
    pygame.display.flip() 

pygame.quit()