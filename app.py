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






#####################função para salvar imagem####################################

def salvar_imagem():
    pass

#-------------------------------label do cabeçlho--------------------------------
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




#####################função para abrir imagem####################################
global imagem_original

imagem_original=[]

label_imagem = Label(janela, bg="#ffffff")
label_imagem.place(x=100, y=100)  # Posição mais centralizada

def abrir_imagem():
    global imagem_tk  # Importante manter a referência
    
    caminho = fd.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Arquivos de imagem", "*.png *.jpg *.jpeg"),)
    )
    
    if not caminho:  # Se o usuário cancelar
        return
    
    try:
        print(f"Arquivo selecionado: {caminho}")  # Debug
        
        # Abre e redimensiona a imagem
        img_pil = Image.open(caminho)
        print(f"Tamanho original: {img_pil.size}")  # Debug
        img_pil = img_pil.resize((190, 270))
        
        # Converte para formato Tkinter
        imagem_tk = ImageTk.PhotoImage(img_pil)
        
        # Atualiza o Label
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk  # Mantém a referência!
        
        print("Imagem carregada com sucesso!")  # Debug
    except Exception as e:
        print(f"Erro ao carregar imagem: {e}")  # Debug
    
#----------------------------rodape-----------------------------------------


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
               fg=co4,
               command=abrir_imagem
               )
btn_esc.place(x=210, y=390)

#botao de conversao----------------------------------------------------

btn_salvar=Button(janela,
               text="Salvar".upper(),
               width=18,
               font=("Roboto 10 bold"),
               fg="white",
               bg="green",
               overrelief=RIDGE,
               
               )
btn_salvar.place(x=210, y=425)

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



