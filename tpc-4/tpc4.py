print("\nMenu:")
print("(1) Criar Lista Aleatória")
print("(2) Ler Lista")
print("(3) Soma")
print("(4) Média")
print("(5) Maior")
print("(6) Menor")
print("(7) Esta Ordenada por Ordem Crescente")
print("(8) Esta Ordenada por Ordem Decrescente")
print("(9) Procurar um Elemento")
print("(0) Sair")
opcao=int(input("Selecione uma opção"))

while opcao!=0:
        print("\nMenu:")
        print("(1) Criar Lista Aleatória")
        print("(2) Ler Lista")
        print("(3) Soma")
        print("(4) Média")
        print("(5) Maior")
        print("(6) Menor")
        print("(7) Esta Ordenada por Ordem Crescente")
        print("(8) Esta Ordenada por Ordem Decrescente")
        print("(9) Procurar um Elemento")
        print("(0) Sair")
        opcao=int(input("Selecione uma opção"))

        import random

        while opcao!=0:
            if opcao==1:
                tamanholista=random.randint(0,100)
                lista=[random.randint(0, 100) for _ in range(tamanholista)]
                print(lista)
            
            elif opcao==2:
                tamanholista=int(input("diz o nr de nrs"))
                def leLista(oi):
                    lista=[]
                    while oi>0:
                        x=int(input("Diz o numero"))
                        oi=oi-1
                        lista.append(x)
                    return lista
                print(leLista(tamanholista))
            
            elif opcao==3:
                soma = sum(lista)
                print("A soma dos elementos da lista é:", soma)

            elif opcao==4:
                soma = sum(lista)
                media = soma / len(lista)
                print("A média dos elementos da lista é:", media)

            elif opcao==5:
                maior = max(lista)
                print("O maior elemento da lista é:", maior)

            elif opcao==6:
                menor = min(lista)
                print("O menor elemento da lista é:", menor)

            elif opcao==7:
                def crescente(lista):
                    for i in range(len(lista) - 1):
                        if lista[i] > lista[i + 1]:
                            print("Sim, a lista está ordenada de forma crescente.")
                        else:
                            print("Não, a lista ão está ordenada de forma crescente.")

            elif opcao==8:
                def crescente(lista):
                    for i in range(len(lista) - 1):
                        if lista[i] < lista[i + 1]:
                            print("Sim, a lista está ordenada de forma decrescente.")
                        else:
                            print("Não, a lista ão está ordenada de forma decrescente.")

            elif opcao==9:
                elemento_procurado = int(input("Diga o número procurado"))
                try:
                    indice = lista.index(elemento_procurado)
                    print(f"O elemento {elemento_procurado} está na posição {indice} da lista.")
                except ValueError:
                    print(f"O elemento {elemento_procurado} não está na lista.")