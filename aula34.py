# Conectar ao MySQL pelo Python
# 1 - XAMPP instalado no PC / RemoDB no celular - iniciar
# 2 - Acessar o 'localhost' - http://localhost/phpmyadmin/
# 3 - Criar um DB (banco de dados)
# 4 - Baixar a biblioteca mysql-connector-python (pip)
#     - Digite no terminal: pip install mysql-connector-python
# 5 - Criar uma conexão Python-MySQL
#     - importar mysql.connector
#     - tentar acessar o DB
#		- criar um objeto para conexão
#       - criar um objeto para o cursor
# 6 - Criar uma tabela com os parâmetros a armazenar
import mysql.connector as mysql

try:
	con = mysql.connect(host = 'localhost', user = 'root', password = '')
	cursor = con.cursor()
	print('Conectado com sucesso.')

except:
	print('Não foi possível conectar ao banco de dados.')


