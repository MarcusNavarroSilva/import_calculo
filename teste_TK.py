from tkinter import Button, Label, Tk

def dizer_ola():
    rotulo_ola_mundo.config(text="ola mundo!!")

janela = Tk()
janela.title("dizer ola")

janela.maxsize(width=500, height=500,)
janela.minsize(width=450, height=540)
botao_dizer_ola = Button(janela, text="ola mundo!!", command=dizer_ola)
botao_dizer_ola.pack(pady=20)

rotulo_ola_mundo = Label(janela, text="xau, mundo")
rotulo_ola_mundo.pack()

janela.mainloop()