from tkinter import *
root = Tk()

class Application:

    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame_1()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#222831')
        self.root.geometry('700x500')
        self.root.resizable(False, False)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=300)

    def frames(self): 
        self.frame_1 = Frame(self.root,bd=4,bg="#222831",highlightbackground="#EEEEEE",highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root,bd=4,bg="#31363F",highlightbackground="#EEEEEE",highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        self.bt_limpar = Button(self.frame_1,text='Limpar',bg="#76ABAE")
        self.bt_limpar.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1,text='Buscar',bg="#76ABAE")
        self.bt_buscar.place(relx=0.3, rely=0.2, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1,text='Novo',bg="#76ABAE")
        self.bt_novo.place(relx=0.6, rely=0.2, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1,text='Alterar',bg="#76ABAE")
        self.bt_alterar.place(relx=0.7, rely=0.2, relwidth=0.1, relheight=0.15)

        self.bt_excluir = Button(self.frame_1,text='Excluir',bg="#76ABAE")
        self.bt_excluir.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.15)

        self.lb_codigo = Label(self.frame_1,text='Código',bg="#31363F")
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.2, relwidth=0.09)
       

Application()
 