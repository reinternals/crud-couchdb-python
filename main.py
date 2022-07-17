# - Modulo necessário para realizar as operações de CRUD no couchDB.
import couchdb	   							  # pip install couchdb

# Função - CREATE.
def fCreate():
	nome = input('Insira o nome do funcionario: ')
	departamento = input('Insira o departamento: ')
	empresa = input('Insira a empresa: ')
	query = {'nome':f'{nome}','departamento':f'{departamento}','empresa':f'{empresa}'}
	db.save(query)

# Função - READ.
def fRead():
	vId = input('Informe o ID do documento: ') # 0d05e9c61a75afccf20f8ee434000388
	doc = db.get(f"{vId}")
	print(doc)

# Função - UPDATE.
def fUpdate():
	vId = input('Informe o ID do funcionario: ')
	doc = db[vId]
	nome = input('Insira o nome do funcionario: ')
	departamento = input('Insira o departamento: ')
	empresa = input('Insira a empresa: ')

	doc['nome'] = nome
	doc['departamento'] = departamento
	doc['empresa'] = empresa
	db[doc.id] = doc

# Função - DELETE.
def fDelete():
	vId = input('Informe o ID do documento que deseja deletar: ')
	doc = db[vId]
	db.delete(doc)

# Função - Continuar.
def fContinuar():
	vContinuar = input('deseja realizar outra consulta? s - sim. n - nao.')
	if vContinuar.lower() == 's':
		fMenu()
	elif vContinuar.lower() == 'n':
		exit()
	else:
		print('Opcao invalida!')
		fContinuar()

# Função - Menu.
def fMenu():
	print('Escolha uma das opções abaixo.')
	print('1 - CREATE.\n2 - READ.\n3 - UPDATE.\n4 - DELETE.\n5 - SAIR.')
	escolha = input('Digite o numero da opcao: ')
	if escolha == '1':
		fCreate()
	elif escolha == '2':
		fRead()
	elif escolha == '3':
		fUpdate()
	elif escolha == '4':
		fDelete()
	elif escolha == '5':
		exit()
	else:
		print('opcao invalida!')
		fContinuar()

# - Conexão com o couchDB.
user = input('Insira o nome de usuario: ')
password = input("Insira a senha: ")
conexao = couchdb.Server(f"http://{user}:{password}@localhost:5984/")

# - Conexao com o banco de dados empresa.
banco = 'empresa'
db = conexao[banco]

# - Chama a função fMenu.
fMenu()
