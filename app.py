from tkinter import *
from tkinter import ttk 
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import cv2


#-------------------------------cores ------------------------------------
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit

#-------------------------------cores ------------------------------------

janela= Tk()
janela.title="conversor foto"
janela.geometry("400x520")
janela.configure(background="#feffff")
janela.resizable(width=FALSE, height=FALSE)

estilo=ttk.Style(janela)
estilo.theme_use("clam")

imag_logo=Image.open("logo.png")
imag_logo=imag_logo.resize((50,50))
imag_logo= ImageTk.PhotoImage(imag_logo)


app_logo=Label(janela,
               image=imag_logo,
               text="imagem para desenho a lápis",
               width=400,
               compound=LEFT,
               relief=RAISED,
               anchor=NW,
               font=("System 15 bold"),
               bg=co1,
               fg=co4
               )


app_logo.place(x=0,y=0)



#rodape

imagem = Image.open("cao.jpg")
imagem = imagem.resize((250, 250))  # Atribua o resultado do resize de volta à variável
imagem = ImageTk.PhotoImage(imagem)

app_rodap = Label(janela,
                 image=imagem,
                 bg=co1,
                 fg=co4
                 )
app_rodap.place(x=60, y=60)

#-----------------------label de configurações----------------------------------

app_opc=Label(janela,
               text="configurações--------------------------------------------".upper(),
               anchor=NW,
               font=("Verdana 7 bold"),
               bg=co1,
               fg=co4
               )
app_opc.place(x=10, y=360)
#------------------------------------------Slider-----------------------------------

escala= Scale(
    janela, from_=0,
              to=255,
              length=120,
              bg=co1,
              fg="red",
              orient=HORIZONTAL
              )
escala.place(x=10,y=380)

#---------------------------------botoes de acao--------------------------------------------------


btn_esc=Button(janela,
               text="Escolher Imagem".upper(),
               width=18,
               font=("Roboto 10 bold"),
               bg=co1,
               overrelief=RIDGE,
               fg=co4
               )
btn_esc.place(x=210, y=390)

#botao de conversao

btn_conv=Button(janela,
               text="converter".upper(),
               width=18,
               font=("Roboto 10 bold"),
               bg=co1,
               overrelief=RIDGE,
               fg=co4
               )
btn_conv.place(x=210, y=425)

#minha assinatura

app_assina=Label(janela,
               text="desenvolvido por Helio Tomé",
               anchor=NW,
               font=("Verdana 10 bold"),
               bg=co1,
               fg=co4
               )
app_assina.place(x=50, y=480)




janela.mainloop()



