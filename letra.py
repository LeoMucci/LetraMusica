import time
from threading import Thread, Lock
import sys
import pygame
import tkinter as tk

Trava = Lock()

def AnimarTexto(WidgetTexto, Texto, Atraso=0.2):
    with Trava:
        for Caractere in Texto:
            WidgetTexto.insert(tk.END, Caractere)
            WidgetTexto.update()
            time.sleep(Atraso)
        WidgetTexto.insert(tk.END, "\n")

def CantarLetra(WidgetTexto, Letra, Atraso=0.2):
    AnimarTexto(WidgetTexto, Letra, Atraso=Atraso)

def TocarMusica(Arquivo):
    pygame.mixer.init()
    pygame.mixer.music.load(Arquivo)
    pygame.mixer.music.play()

# o numero é o tempo que a letra aparece, depois colocar a letra referente ao tempo
def CantarMusica(WidgetTexto):
    LetraTempo = [
        (29, "Paz, "), 
        (32, "Eu quero paz"), 
        (37, "Já me cansei de ser a última a saber de ti"), 
        (46, "Se todo mundo sabe quem te faz"),
        (51, "Chegar mais tarde"),
        (53, "Eu já cansei de imaginar você com ela"),
        
        (60, "Diz pra mim"),
        (63, "Se vale a pena, amor"),
        (66, "A gente ria tanto desses nossos desencontros"),
        (70, "Mas você passou do ponto"),
        (72, "E agora eu já não sei mais"),
        
        (77, "Eu quero paz"),
        (81, "Quero dançar com outro par"),
        (85, "Pra variar, amor"),
        (90, "Não dá mais pra fingir que ainda não vi"),
        (95, "As cicatrizes que ela fez"),
        
        (100, "Se desta vez"),
        (102, "Ela é senhora deste amor"),
        (107, "Pois vá embora, por favor"),
        (112, "Que não demora pra essa dor"),
        (117, "Sangrar")
    ]
    
    TempoInicio = time.time()
    
    for TempoLetra, Letra in LetraTempo:
        TempoDecorrido = time.time() - TempoInicio
        TempoEspera = TempoLetra - TempoDecorrido
        
        if TempoEspera > 0:
            time.sleep(TempoEspera)
        
        CantarLetra(WidgetTexto, Letra, Atraso=0.15)

def IniciarMusica():
    Root = tk.Tk()
    Root.title(":(")
    
    Root.configure(bg="black")
    
    WidgetTexto = tk.Text(Root, height=20, width=80, font=("Helvetica", 14), bg="black", fg="white")
    WidgetTexto.pack(padx=10, pady=10)
    
    # se quiser coloca a musica aq p sincronizar melhor com a letra
    ArquivoMusica = 'D:\\Los hermanos - A outra.mp3' 

    ThreadMusica = Thread(target=TocarMusica, args=(ArquivoMusica,))
    ThreadMusica.start()

    ThreadLetras = Thread(target=CantarMusica, args=(WidgetTexto,))
    ThreadLetras.start()

    Root.mainloop()

if __name__ == "__main__":
    IniciarMusica()
