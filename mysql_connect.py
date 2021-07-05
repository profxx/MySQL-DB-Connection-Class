'''
MySQL Connect class

'''
import mysql.connector as mysql		# pip install mysql-connector-python

class Funcs:

	def conecta_bd(self):					# CONEXÃO
		try:
			self.con = mysql.connect(		# Conectar
				host = '127.0.0.1',			# -
				database = 'my_books',		# -
				user = 'root',				# -- Parâmetros necessários
				passwd = '')				# - 

			self.cursor = con.cursor()		# Criar cursor
			print('Conectado ao banco de dados.')

		except:
			print('Falha ao conectar ao banco de dados.')

	def desconecta_bd(self):
		self.con.close()					# Desconecta
		print('Desconectou com sucesso.')

	def cria_tabela(self):					# Cria tabelas
		self.conecta_bd()
		self.cursor.execute('''
				CREATE TABLE IF NOT EXISTS books(
					id INT AUTO_INCREMENT PRIMARY KEY,
					nome_livro varchar(80),
					autor varchar(80),
					paginas INT
				);
			''')
		self.con.commit()					# Salva a alteração
		print('Banco de Dados criado com sucesso.')
		self.desconecta_bd()

	def variaveis(self):
		self.nome_livro = input('Nome do livro: ')
		self.autor = input('Autor: ')
		self.paginas = int(input('Qtd páginas: '))

	def insere_livro(self):
		self.variaveis()
		self.conecta_bd()
		self.cursor.execute("""
            INSERT INTO books(nome_livro, autor, paginas)
            VALUES (?, ?, ?);""", (self.nome_livro, self.autor, self.paginas))
		self.con.commit()
		self.desconecta_bd()

#Programa Principal
a = Funcs()
a.cria_tabela()
a.insere_livro()