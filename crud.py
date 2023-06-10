import os
import sqlite3
from tkinter import messagebox

db_path = os.path.abspath("registronotas.db")

class AlunoGUI:
    def __init__(self, root):
        # ...
        
        # Conexão com o banco de dados
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
        # Criação da tabela alunos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                cpf TEXT PRIMARY KEY,
                nome TEXT,
                data_nascimento TEXT,
                sexo TEXT,
                idade INTEGER,
                av1 REAL,
                av2 REAL,
                media REAL
            )
        ''')
        
        self.conn.commit()
        
    def cadastrar_aluno(self):
        cpf = self.entry_cpf.get()
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        sexo = self.entry_sexo.get()
        idade = int(self.entry_idade.get())
        av1 = float(self.entry_av1.get())
        av2 = float(self.entry_av2.get())
        media = (av1 + av2) / 2
        
        try:
            # Inserir aluno no banco de dados
            self.cursor.execute('''
                INSERT INTO alunos (cpf, nome, data_nascimento, sexo, idade, av1, av2, media)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (cpf, nome, data_nascimento, sexo, idade, av1, av2, media))
            
            self.conn.commit()
            
            messagebox.showinfo("Cadastro", "Aluno cadastrado com sucesso!")
            self.limpar_campos()
            
        except sqlite3.Error as e:
            messagebox.showerror("Erro", "Erro ao cadastrar aluno: " + str(e))
            
    def exibir_alunos(self):
        try:
            # Recuperar alunos do banco de dados
            self.cursor.execute("SELECT * FROM alunos")
            rows = self.cursor.fetchall()
            
            if not rows:
                messagebox.showinfo("Alunos", "Não há alunos cadastrados!")
                return
            
            lista_alunos = ""
            for row in rows:
                lista_alunos += f"CPF: {row[0]}\n"
                lista_alunos += f"Nome: {row[1]}\n"
                lista_alunos += f"Data de Nascimento: {row[2]}\n"
                lista_alunos += f"Sexo: {row[3]}\n"
                lista_alunos += f"Idade: {row[4]}\n"
                lista_alunos += f"Notas: AV1={row[5]}, AV2={row[6]}\n"
                lista_alunos += f"Média: {row[7]}\n"
                lista_alunos += "----------------------------------------\n"
            
            messagebox.showinfo("Alunos", lista_alunos)
            
        except sqlite3.Error as e:
            messagebox.showerror("Erro", "Erro ao exibir alunos: " + str(e))
            
    def atualizar_aluno(self):
        cpf = self.entry_cpf.get()
        
        try:
            # Verificar se o aluno existe no banco de dados
            self.cursor.execute("SELECT * FROM alunos WHERE cpf=?", (cpf,))
            row = self.cursor.fetchone()
            
            if not row:
                messagebox.showerror("Atualização", "Aluno não encontrado!")
                return
            
            nome = self.entry_nome.get()
            data_nascimento = self.entry_data_nascimento.get()
            sexo = self.entry_sexo.get()
            idade = int(self.entry_idade.get())
            av1 = float(self.entry_av1.get())
            av2 = float(self.entry_av2.get())
            media = (av1 + av2) / 2
            
            # Atualizar informações do aluno no banco de dados
            self.cursor.execute('''
                UPDATE alunos
                SET nome=?, data_nascimento=?, sexo=?, idade=?, av1=?, av2=?, media=?
                WHERE cpf=?
            ''', (nome, data_nascimento, sexo, idade, av1, av2, media, cpf))
            
            self.conn.commit()
            
            messagebox.showinfo("Atualização", "Informações do aluno atualizadas com sucesso!")
            self.limpar_campos()
            
        except sqlite3.Error as e:
            messagebox.showerror("Erro", "Erro ao atualizar aluno: " + str(e))
            
    def deletar_aluno(self):
        cpf = self.entry_cpf.get()
        
        try:
            # Deletar aluno do banco de dados
            self.cursor.execute("DELETE FROM alunos WHERE cpf=?", (cpf,))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Deleção", "Aluno deletado com sucesso!")
                self.limpar_campos()
            else:
                messagebox.showerror("Deleção", "Aluno não encontrado!")
                
        except sqlite3.Error as e:
            messagebox.showerror("Erro", "Erro ao deletar aluno: " + str(e))
