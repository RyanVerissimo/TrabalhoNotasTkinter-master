import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self, cpf, nome, data_nascimento, sexo, idade, av1, av2):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.idade = idade
        self.av1 = av1
        self.av2 = av2
        self.media = (av1 + av2) / 2

class AlunoGUI:
    def __init__(self, root):
        self.alunos = []
        self.root = root
        self.root.title("Sistema de Registro de Notas")
        
        # Labels
        self.lbl_cpf = tk.Label(root, text="CPF:")
        self.lbl_cpf.grid(row=0, column=0, sticky=tk.E)
        self.lbl_nome = tk.Label(root, text="Nome:")
        self.lbl_nome.grid(row=1, column=0, sticky=tk.E)
        self.lbl_data_nascimento = tk.Label(root, text="Data de Nascimento:")
        self.lbl_data_nascimento.grid(row=2, column=0, sticky=tk.E)
        self.lbl_sexo = tk.Label(root, text="Sexo:")
        self.lbl_sexo.grid(row=3, column=0, sticky=tk.E)
        self.lbl_idade = tk.Label(root, text="Idade:")
        self.lbl_idade.grid(row=4, column=0, sticky=tk.E)
        self.lbl_av1 = tk.Label(root, text="AV1:")
        self.lbl_av1.grid(row=5, column=0, sticky=tk.E)
        self.lbl_av2 = tk.Label(root, text="AV2:")
        self.lbl_av2.grid(row=6, column=0, sticky=tk.E)
        
        # Entry fields
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.grid(row=0, column=1)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=1, column=1)
        self.entry_data_nascimento = tk.Entry(root)
        self.entry_data_nascimento.grid(row=2, column=1)
        self.entry_sexo = tk.Entry(root)
        self.entry_sexo.grid(row=3, column=1)
        self.entry_idade = tk.Entry(root)
        self.entry_idade.grid(row=4, column=1)
        self.entry_av1 = tk.Entry(root)
        self.entry_av1.grid(row=5, column=1)
        self.entry_av2 = tk.Entry(root)
        self.entry_av2.grid(row=6, column=1)
        
        # Buttons
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_aluno)
        self.btn_cadastrar.grid(row=7, column=0, pady=10)
        self.btn_exibir = tk.Button(root, text="Exibir Alunos", command=self.exibir_alunos)
        self.btn_exibir.grid(row=7, column=1)
        self.btn_atualizar = tk.Button(root, text="Atualizar Aluno", command=self.atualizar_aluno)
        self.btn_atualizar.grid(row=8, column=0, pady=10)
        self.btn_deletar = tk.Button(root, text="Deletar Aluno", command=self.deletar_aluno)
        self.btn_deletar.grid(row=8, column=1)
        
    def cadastrar_aluno(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        sexo = self.entry_sexo.get()
        idade = self.entry_idade.get()
        av1 = float(self.entry_av1.get())
        av2 = float(self.entry_av2.get())
        
        aluno = Aluno(cpf, nome, data_nascimento, sexo, idade, av1, av2)
        self.alunos.append(aluno)
        
        messagebox.showinfo("Cadastro", "Aluno cadastrado com sucesso!")
        
        self.limpar_campos()
        
    def exibir_alunos(self):
        if not self.alunos:
            messagebox.showinfo("Alunos", "Não há alunos cadastrados!")
            return
        
        lista_alunos = ""
        for aluno in self.alunos:
            lista_alunos += f"CPF: {aluno.cpf}\n"
            lista_alunos += f"Nome: {aluno.nome}\n"
            lista_alunos += f"Data de Nascimento: {aluno.data_nascimento}\n"
            lista_alunos += f"Sexo: {aluno.sexo}\n"
            lista_alunos += f"Idade: {aluno.idade}\n"
            lista_alunos += f"Notas: AV1={aluno.av1}, AV2={aluno.av2}\n"
            lista_alunos += f"Média: {aluno.media}\n"
            lista_alunos += "----------------------------------------\n"
        
        messagebox.showinfo("Alunos", lista_alunos)
        
    def atualizar_aluno(self):
        cpf = self.entry_cpf.get()
        aluno_atualizar = None
        
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                aluno_atualizar = aluno
                break
        
        if aluno_atualizar is None:
            messagebox.showerror("Atualização", "Aluno não encontrado!")
            return
        
        aluno_atualizar.nome = self.entry_nome.get()
        aluno_atualizar.data_nascimento = self.entry_data_nascimento.get()
        aluno_atualizar.sexo = self.entry_sexo.get()
        aluno_atualizar.idade = self.entry_idade.get()
        aluno_atualizar.av1 = float(self.entry_av1.get())
        aluno_atualizar.av2 = float(self.entry_av2.get())
        aluno_atualizar.media = (aluno_atualizar.av1 + aluno_atualizar.av2) / 2
        
        messagebox.showinfo("Atualização", "Informações do aluno atualizadas com sucesso!")
        
        self.limpar_campos()
        
    def deletar_aluno(self):
        cpf = self.entry_cpf.get()
        
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                self.alunos.remove(aluno)
                messagebox.showinfo("Deleção", "Aluno deletado com sucesso!")
                self.limpar_campos()
                return
        
        messagebox.showerror("Deleção", "Aluno não encontrado!")
        
    def limpar_campos(self):
        self.entry_cpf.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_data_nascimento.delete(0, tk.END)
        self.entry_sexo.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_av1.delete(0, tk.END)
        self.entry_av2.delete(0, tk.END)

root = tk.Tk()
app = AlunoGUI(root)
root.mainloop()
