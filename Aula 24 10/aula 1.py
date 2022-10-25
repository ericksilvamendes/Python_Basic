"""UM GERENTE CONTAVIL ARMAZENA EM UM ARQUIVO TODOS OS DADOS DO FUNCIONÁRIO DA EMPRESA PHILCO.
CADA FUNCIONARIO SOBRE SUA RESPONSABILIDADE POSSUI UM ID, NOME E UM USUARIO 

1 - CRIE UM ARQUIVO FUNCIONARIO.TXT QUE ARMAZANA  O ID E O NOME DE SEUS FUNCIONARIOS.

2 - CRIE UM ARQUIVO SALARIO.TXT QUE POSSUI O ID DO FUNCIONÁRIO E SEU RESPETIVO SALÁRIO.

3 - CADASTRE, PARA TESTE CINCO FUNCIONARIO, ESCREVA UM PROGRAMA QUE PERMITA CONSULTAR O SALÁRIO DE CADA
 FUNCIONÁRIO, A PARTIR DO SEU NOME OU ID. IMPRIMIR A LINHA CORRESPNDENTE AO NOME NO ARQUIVO SALARIO.TXT
"""

#title() Deixa a primeira letra maiuscúla
func = input ("Digite o nome ou número do funcionário ").title()
#iniciar a variavel que usaremos futuramente fora do loop
with open("funcionario.txt",'r', encoding = 'utf-8') as arquivo1:
    funcionario_id = -1
    for linha in arquivo1:
        linha = linha.split()
        
        if linha[0] == func or linha [1] == func:
            funcionario_id = linha[0]
            nome_funcionario = linha[1]   
            
            break


with open("salario.txt",'r', encoding = 'utf-8') as arquivo2:
    salario = 0
    for linha in arquivo2:
        linha2 = linha.split()
        if linha2[0] == funcionario_id:
            print('ID:',funcionario_id)
            salario = linha2[1]
            print('Salario:',salario)
            print(nome_funcionario)

            break


    
    





with open("salario.txt",'r', encoding = 'utf-8') as funcionarios:
    lista_Salario = funcionarios.readlines()


        
            

            
    
    


