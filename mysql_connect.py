'''
MySQL Connect class

'''
import mysql.connector as mysql

class Funcs:
	def conecta_bd(self):
		try:
			self.con = mysql.connect(
				host = 'localhost',
				database = 'my_books',
				user = 'root',
				passwd = '')

			self.cursor = con.cursor()
			print('Conectado ao banco de dados.')

		except:
			print('Falha ao conectar ao banco de dados.')

	def desconecta_bd(self):
		self.con.close()
		print('Desconectou com sucesso.')

	def cria_tabela(self, tabela):
		self.conecta_bd()
		self.cursor.execute('''
				CREATE TABLE IF NOT EXISTS livros(
					id INT AUTO_INCREMENTE PRIMARY KEY,
					nome_livro varchar(80),
					autor varchar(80),
					paginas INT
				);
			''')
		self.con.commit()
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
        self.conn.commit()
        self.desconecta_bd()