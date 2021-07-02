import mysql.connector as mysql

try:
	con = mysql.connect(
		host = 'localhost', 
		user = 'root', 
		password = '',
		database = 'my_books')
	cursor = con.cursor()
	print('Conectado com sucesso.')
	cursor.execute('''
			CREATE TABLE books(
				id INT AUTO_INCREMENT PRIMARY KEY,
				nome_livro varchar(30),
				autor varchar(30),
				paginas INT
			)
			''')
	print('Tabela criada com sucesso.')
	con.commit()
	con.close()
	print('Desconectado com sucesso.')

except:
	print('Não foi possível conectar ao banco de dados.')