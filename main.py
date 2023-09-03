import tkinter
from tkinter import ttk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#------------------Autenticação firestore
cred = credentials.Certificate('ezpoint-cd326-firebase-adminsdk-6yfjv-7e14cc16f2.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# CARACTERIZANDO A PÁGINA -------------------

window = tkinter.Tk()
window.title("Login")

frame = tkinter.Frame(window)
frame.pack()

# FUNCÕES DE VERIFICAÇÃO DE USUÁRIO ---------

def confirmação():
    primeiro_nome = primeiro_nome_input.get()
    sobrenome = sobrenome_input.get()
    atuação = area_box.get()
    senha = senha_input.get()

    if primeiro_nome and sobrenome and atuação and senha:
        tkinter.messagebox.showinfo(title="Confirmado", message="Login concluído!")
      
        result = db.collection('Funcionarios').where('email', '==', email).get()

            if len(result) and len == 0:
    else:
        tkinter.messagebox.showwarning(title="Erro", message="É necessário completar todos os campos de informações!!")

#------------------------------------------------1ª PARTE------------------------------------------------

# TITULO ------------------------------------

infouser_frame = tkinter.LabelFrame(frame, text="")
infouser_frame.grid(row=0, column=0, padx=20, pady=20)

# INSERIR O NOME E SOBRENOME ----------------

primeiro_nome = tkinter.Label(infouser_frame, text="Nome")
primeiro_nome.grid(row=0, column=0)
sobrenome = tkinter.Label(infouser_frame, text="Sobrenome")
sobrenome.grid(row=0, column=1)
primeiro_nome_input = tkinter.Entry(infouser_frame)
sobrenome_input = tkinter.Entry(infouser_frame)
primeiro_nome_input.grid(row=1, column=0, padx=20, pady=20)
sobrenome_input.grid(row=1, column=1, padx=20, pady=20)

#------------------------------------------------2ª PARTE------------------------------------------------

# TITULO ------------------------------------

infosenha_frame = tkinter.LabelFrame(frame, text="")
infosenha_frame.grid(row=2, column=0, padx=20, pady=20)

# INSERIR A SENHA ---------------------------

senha = tkinter.Label(infosenha_frame, text="Senha")
senha.grid(row=0, column=0)
senha_input = tkinter.Entry(infosenha_frame)
senha_input.grid(row=1, column=0, padx=20, pady=20)

# INSERIR AREA DE ATUAÇÃO --------------------

area = tkinter.Label(infosenha_frame, text="Área em que atua")
area.grid(row=0, column=1)
area_box = ttk.Combobox(infosenha_frame,values=[ "", "Produção", "Supervisor", "Produção Química", "Soldador"])
area_box.grid(row=1, column=1, padx=20, pady=20)

#------------------------------------------------3ª PARTE------------------------------------------------

# BOTÃO DE LOGIN -------------------------

botao = tkinter.Button(frame, text="Login", command=confirmação)
botao.grid(row=4, column=0, sticky="news", padx=20, pady=20)




window.mainloop()