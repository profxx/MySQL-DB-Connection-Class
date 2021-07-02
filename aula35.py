import mysql.connector as mysql

class Funcs:	
	def conecta_bd(self):
		try:
			self.con = mysql.connect(
				host = 'localhost', 
				user = 'root', 
				password = '',
				database = 'my_books')
			self.cursor = con.cursor()
			print('Conectado com sucesso.')

		except:
			print('Não foi possível conectar ao banco de dados.')

	def cria_tabela(self):
		self.cursor.execute('''
			CREATE TABLE books(
				id INT AUTO_INCREMENT PRIMARY KEY,
				nome_livro varchar(30),
				autor varchar(30),
				paginas INT
			)
			''')
	def insere_livro(self, livro, autor, paginas):
		self.cursor.execute('''
			INSERT INTO books VALUES (?, ?, ?);
			''', (livro, autor, paginas))
		print(f'{livro} insterido com sucesso.')
	
	def desconecta_bd(self):
		self.con.close()
		print('Desconectado com sucesso.')




