numeroDeAlunos = 0
nome=input("digite o nome do aluno: ")
while nome != 'ninguem' and numeroDeAlunos < 5:
    numeroDeAlunos = numeroDeAlunos + 1
    maiorNota = 0 
    contador = 0
    somaNotas = 0
    sobrenome= input('digite o sobrenome do aluno: ')
    
    while contador < 4 :
        nota=float(input("digite a nota do aluno: "))
        somaNotas = somaNotas + nota

        contador+=1
        if(contador==1):
            maiorNota = nota
        else:
            if(nota>maiorNota):
                maiorNota = nota


    media = somaNotas/contador
    print('')
    print('Aluno avaliado foi: '+ nome + ' '+ sobrenome)
    print("A média de notas é: ", media)
    print("A maior nota foi: ", maiorNota)
    print('')
    



