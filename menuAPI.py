import os
import requests
#funcao de lumpar
def limpar():
	os.system( 'cls' if os.name == 'nt' else 'clear')
#funcao do cep	
def cep():
	limpar()
	print("\nVerificacao de CEP")
	cep = input("digite um cep valido: ")
	
	url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
	resposta = requests.get(url)
	dados = resposta.json()
	
	if "message" in dados:
		print("erro: ", dados["message"])
	else:
		print(dados["city"])
		print(dados["state"])
		print(dados["neighborhood"])

	input("\nPresione enter para sair do menu")
#funcao do ddd
def ddd():
	limpar()
	
	print("\nVerificador de DDD")
	ddd = input("digite um ddd valido: ")
	
	url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
	
	resposta = requests.get(url)
	dados = resposta.json()
	
	if "message" in dados:
		print("erro: ", dados["message"])
	else:
		print(dados["cities"])
		print(dados["state"])
				
	input("\nPresione enter para sair do menu: ")
#menU
def menu():
	while True:
		limpar()
		
		
		print("\nSeu menu de info")
		print("1-verificar CEP")
		print("2-verificar DDD")
		print("3-sair")
		
		opcao = input("escolha uma opcao: " )

		match opcao:
		      		case "1":
		      			cep()
		      		case "2":
		      			ddd()
		      		case "3":
		      			print("saindo...")
		      			limpar()
		      			break
		      		case _:
		      			print("selecione uma opcao valida")
		      			input("\nAperte enter pra continuar")
    	
menu()
#vai se ferrar q bagulho estressante 
#depois de horas eu consegui, nao entendi nada do que eu fiz, mas consegui :)
