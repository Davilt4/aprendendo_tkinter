from tkinter import *
from tkinter import ttk
import sqlite3
import webbrowser

root = Tk()

class Functions():

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.email = self.email_entry.get()
        self.cidade = self.cidade_entry.get()

    def limparCampos(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    
    def conexaoBanco(self):
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor(); print("Conexão realizada com sucesso!")

    def desconectaBanco(self):
        self.conn.close();print("Conexão encerrada com sucesso!")

    def montaTabelas(self):

        self.conexaoBanco()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(40) NOT NULL,
                email VARCHAR(40) NOT NULL,
                cidade VARCHAR(40) 
            );
        """)
        self.conn.commit(); print("Tabela criada com sucesso!")
        self.desconectaBanco()

    def addCliente(self):

        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.email = self.email_entry.get()
        self.cidade = self.cidade_entry.get()

        self.conexaoBanco()
        self.cursor.execute("""INSERT INTO clientes (nome, email, cidade) VALUES (?, ?, ?)""", (self.nome, self.email, self.cidade))
        self.conn.commit()
        self.desconectaBanco()
        self.selectLista()
    
    def selectLista(self):
        
        self.listaClientes.delete(*self.listaClientes.get_children())
        self.conexaoBanco()
        lista = self.cursor.execute("""SELECT cod, nome, email, cidade FROM clientes ORDER BY nome ASC""")
        for i in lista:
            self.listaClientes.insert("", END, values=i)
        self.desconectaBanco()
    
    def doubleClick(self, event):

        self.limparCampos()

        self.listaClientes.selection()

        for i in self.listaClientes.selection():
            col1, col2, col3, col4 = self.listaClientes.item(i, 'values')

            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.email_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleteCliente(self):

        self.variaveis()
        self.conexaoBanco()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo))
        self.conn.commit()
        self.desconectaBanco()
        self.limparCampos()
        self.selectLista()
   
    def alterarCliente(self):

        self.variaveis()
        self.conexaoBanco()
        self.cursor.execute("""UPDATE clientes SET nome = ?, email = ?, cidade = ? WHERE cod = ?""", (self.nome, self.email, self.cidade, self.codigo))
        self.conn.commit()
        self.desconectaBanco()
        self.selectLista()
        self.limparCampos()

    def buscaCliente(self):
        self.conexaoBanco()
        self.listaClientes.delete(*self.listaClientes.get_children())

        self.nome.entry.insert(END, '%')
        nome = self.nome_entry.get() #Problema aqui "NAO ESTA RECONDENDO O NOME"
        self.cursor.execute("""SELECT cod, nome, email, cidade FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)

        buscar = self.cursor.fetchall()
        for i in buscar:
            self.listaClientes.insert("", END, values=i)

        self.limparCampos()

        self.desconectaBanco()   

class Application(Functions):

    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame_1()
        self.list_frame_2()
        self.montaTabelas()
        self.selectLista()
        self.menus()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#222831')
        self.root.geometry('700x500')
        self.root.resizable(False, False)

    def frames(self): 
        self.frame_1 = Frame(self.root,bd=4,bg="#222831",highlightbackground="#EEEEEE",highlightthickness=0)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root,bd=4,bg="#31363F",highlightbackground="#EEEEEE",highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        self.bt_limpar = Button(self.frame_1,text='Limpar',bg="#76ABAE",command=self.limparCampos)
        self.bt_limpar.place(relx=0.2, rely=0.10, relwidth=0.1, relheight=0.15,)

        self.bt_buscar = Button(self.frame_1,text='Buscar',bg="#76ABAE",command=self.buscaCliente)
        self.bt_buscar.place(relx=0.3, rely=0.10, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1,text='Novo',bg="#76ABAE",command=self.addCliente)
        self.bt_novo.place(relx=0.5, rely=0.10, relwidth=0.1, relheight=0.15)
    
        self.bt_alterar = Button(self.frame_1,text='Alterar',bg="#76ABAE",command=self.alterarCliente)
        self.bt_alterar.place(relx=0.6, rely=0.10, relwidth=0.1, relheight=0.15)

        self.bt_excluir = Button(self.frame_1,text='Excluir',bg="#76ABAE", command=self.deleteCliente)
        self.bt_excluir.place(relx=0.7, rely=0.10, relwidth=0.1, relheight=0.15)

        self.lb_codigo = Label(self.frame_1,text='Código',bg="#31363F",fg="#EEEEEE")
        self.lb_codigo.place(relx=0.05, rely=0.01)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.09)

        self.lb_nome = Label(self.frame_1,text='Nome',bg="#31363F",fg="#EEEEEE")
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.50, relwidth=0.75)

        self.lb_email = Label(self.frame_1,text='Email',bg="#31363F",fg="#EEEEEE")
        self.lb_email.place(relx=0.05, rely=0.65)

        self.email_entry = Entry(self.frame_1)
        self.email_entry.place(relx=0.05, rely=0.80, relwidth=0.2)

        self.lb_cidade = Label(self.frame_1,text='Cidade',bg="#31363F",fg="#EEEEEE")
        self.lb_cidade.place(relx=0.3, rely=0.65)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.3, rely=0.80, relwidth=0.4)

    def list_frame_2(self):
        self.listaClientes = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))

        self.listaClientes.heading('#0', text='')
        self.listaClientes.heading('#1', text='Cod')
        self.listaClientes.heading('#2', text='Nome')
        self.listaClientes.heading('#3', text='Email')
        self.listaClientes.heading('#4', text='Cidade')

        self.listaClientes.column('#0', width=1)
        self.listaClientes.column('#1', width=50)
        self.listaClientes.column('#2', width=200)
        self.listaClientes.column('#3', width=125)
        self.listaClientes.column('#4', width=125)

        self.listaClientes.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.85)

        self.scroolbar = Scrollbar(self.frame_2, orient='vertical')
        self.scroolbar.place(relx=0.96, rely=0.01, relwidth=0.03, relheight=0.85)
        self.listaClientes.configure(yscrollcommand=self.scroolbar.set)
        self.scroolbar.configure(command=self.listaClientes.yview)

        self.listaClientes.bind("<Double-1>", self.doubleClick)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()
    
        menubar.add_cascade(label='Opções', menu=filemenu)
        menubar.add_cascade(label='Sobre', menu=filemenu2)
        
        filemenu.add_command(label='Sair', command=quit)

        def linkedin():
            webbrowser.open('https:/www.linkedin.com/in/davi-leite-alencar-a79608230/')

        filemenu2.add_command(label='Davi Leite', command=linkedin)

Application()