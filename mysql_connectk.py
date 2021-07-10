'''
MySQL Connect class

'''
from configparser import Error
import mysql.connector as mysql		# pip install mysql-connector-python

class Funcs:

	def conecta_bd(self):					# CONEXÃO
		try:
			self.con = mysql.connect(		# Conectar
				host = 'localhost',			# -
				user = 'root')				# - 

			self.cursor = self.con.cursor()		# Criar cursor
			self.usarBD("my_books")
			print('Conectado ao banco de dados.')

		except Error as err:
			print('Falha ao conectar ao banco de dados.')
			print(err)
	
	def usarBD(self, bd):
		try:
			self.cursor.execute(f"USE {bd}")
		except:
			self.cursor.execute(f"CREATE DATABASE {bd}")
			self.cursor.execute(f"USE {bd}")

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
		self.cursor.execute('''
            INSERT INTO books(nome_livro, autor, paginas)
            VALUES (?, ?, ?);''', (self.nome_livro, self.autor, self.paginas))
		self.con.commit()
		self.desconecta_bd()
	
	
if __name__ == "__main__":
	#Programa Principal
	a = Funcs()
	a.conecta_bd()