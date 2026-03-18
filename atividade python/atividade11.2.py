estoque = {}

print("bem-vindo ao sistema de gestão de estoque de produtos desenvolvido por Murilo Bondan")
while True:
    #while true é utilizado para criar um loop infinito, assim o sistema vai continuar rodando até que o usuário decida sair digitando 'sair'.
    operacao = input("deseja registrar a entrada e saída de produtos? (digite 'entrada' ou 'saída') ou 'sair'").lower()
    #lower é utilizado para converter a palavra para minúscula, assim o usuário pode digitar 'Entrada', 'ENTRADA', 'Saída', 'SAÍDA' ou 'sair' sem se preocupar com a caixa das letras.
    if operacao not in ['entrada', 'saída', 'sair']:
        #not in é utilizado para verificar se a operação digitada pelo usuário é diferente de 'entrada', 'saída' ou 'sair', caso seja diferente, o sistema vai mostrar uma mensagem de operação inválida e voltar para o início do loop, permitindo que o usuário digite uma operação válida.
        print("operação inválida. ")
        continue
    #continue é utilizado para voltar ao início do loop quando alguém digitar uma operação inválida.

    if operacao == 'sair':
        break
    #break é utilizado para sair do loop infinito quando o usuário digitar 'sair'.
    produto = input("digite o nome do produto: ").strip()
    #strip é utilizado para remover os espaços que ficam em branco no início e final da palavra, fazendo isso o usuário poderá escrever o produto com espaços que não terá problema. ex: "   arroz   " será convertido para "arroz" e não terá problema na hora de registrar a entrada ou saída do produto.
    qtd = int(input("digite a quantidade: "))


    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
        #get é utilizado para obter o valor do produto no dicionário estoque, se o produto não existir, ele retorna 0. 
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
        else:
            print("Erro: produto inexistente ou estoque insuficiente.")

print("\n ---Estoque Final---")
#print("\n") é utilizado para pular uma linha antes de imprimir o estoque final, deixando a saída mais organizada.
for p, q in estoque.items():
    #for p, q in estoque.items() é utilizado para percorrer o dicionário estoque e imprimir o nome do produto (p) e a quantidade (q) de cada produto no estoque final.
    print(f"{p}: {q}")
    #print(f"{p}: {q}") é utilizado para mostrar escrito o nome do produto (p) e a quantidade (q) de cada produto no estoque final, utilizando f-string para formatar a saída.