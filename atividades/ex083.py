expr = input('Digite a expressão: ')  # Não precisa do str(), o input já retorna uma string
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')  # Adiciona '(' na pilha
    elif simb == ')':
        if len(pilha) > 0:  # Verifica se há algum '(' para ser fechado
            pilha.pop()  # Fecha o parêntese removendo o '(' da pilha
        else:
            print('Expressão inválida')  # Se não houver '(' para fechar
            break
else:
    # Se a pilha estiver vazia, significa que todos os parênteses foram fechados corretamente
    if len(pilha) == 0:
        print('Expressão válida')
    else:
        print('Expressão inválida')  # Caso haja parênteses não fechados
