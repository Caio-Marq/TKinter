import tkinter as tk

# 1. JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Login - a+")
janela.geometry("1440x900")
janela.configure(bg="#ffffff")


# 2. CONTAINER CENTRALIZADO
container = tk.Frame(janela, bg="#ffffff")
container.place(relx=0.5, rely=0.5, anchor="center")


# 3. LOGÓTIPO ("a+")
logo = tk.Label(
    container,
    text="a+",
    font=("Helvetica", 65, "bold"),
    fg="#2B8FCB",
    bg="#ffffff",
)
logo.pack(pady=(0, 30))


# ==============================================================================
# 4. CAMPO DE E-MAIL COM PLACEHOLDER INTELIGENTE
# ==============================================================================
def ao_focar_email(event):
    if entrada_email.get() == "e-mail":
        entrada_email.delete(0, tk.END)
        entrada_email.config(fg="#333333")  # Cor do texto digitado


def ao_desfocar_email(event):
    if entrada_email.get().strip() == "":
        entrada_email.insert(0, "e-mail")
        entrada_email.config(fg="#999999")  # Cor do texto de dica


entrada_email = tk.Entry(
    container,
    font=("Arial", 12),
    bg="#EAEAEA",
    fg="#999999",
    bd=0,
    relief="flat",
    width=32,
    justify="center",
)
entrada_email.insert(0, "e-mail")
# Eventos para fazer a mensagem sumir/aparecer
entrada_email.bind("<FocusIn>", ao_focar_email)
entrada_email.bind("<FocusOut>", ao_desfocar_email)
entrada_email.pack(ipady=12, pady=8)


# ==============================================================================
# 5. CAMPO DE SENHA COM BOTÃO PARA VISUALIZAR SENHA
# ==============================================================================
frame_senha = tk.Frame(container, bg="#ffffff")
frame_senha.pack(pady=8)

entrada_senha = tk.Entry(
    frame_senha,
    font=("Arial", 12),
    bg="#EAEAEA",
    fg="#333333",
    bd=0,
    relief="flat",
    show="*",  # Inicia oculta
    width=28,
    justify="center",
)
entrada_senha.pack(side="left", ipady=12)


def alternar_visualizacao_senha():
    if entrada_senha.cget("show") == "*":
        entrada_senha.config(show="")
        btn_olho.config(text="🙈")  # Ícone para ocultar
    else:
        entrada_senha.config(show="*")
        btn_olho.config(text="👁")  # Ícone para mostrar


btn_olho = tk.Button(
    frame_senha,
    text="👁",
    font=("Arial", 11),
    bg="#EAEAEA",
    fg="#666666",
    bd=0,
    relief="flat",
    activebackground="#EAEAEA",
    highlightbackground="#EAEAEA",
    command=alternar_visualizacao_senha,
    cursor="hand2",
    width=3,
)
btn_olho.pack(side="right", ipady=10)
# ==============================================================================


# 6. BOTÃO "ACESSAR"
botao_entrar = tk.Button(
    container,
    text="ACESSAR",
    font=("Arial", 11, "bold"),
    bg="#2B8FCB",
    fg="#ffffff",
    activebackground="#206e9c",
    activeforeground="#ffffff",
    highlightbackground="#ffffff",
    bd=0,
    relief="flat",
    width=32,
    cursor="hand2",
)
botao_entrar.pack(ipady=12, pady=(25, 15))


# 7. LINK "PRIMEIRO ACESSO"
link_primeiro_acesso = tk.Label(
    container,
    text="PRIMEIRO ACESSO",
    font=("Arial", 10, "bold"),
    fg="#2B8FCB",
    bg="#ffffff",
    cursor="hand2",
)
link_primeiro_acesso.pack(pady=10)


# INICIAR APLICAÇÃO
janela.mainloop()