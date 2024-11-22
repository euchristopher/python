nome = "Marcos Christopher Moura Oliveira Rodrigues"

# Conta apenas as letras, ignorando espaços
somente_letras = "".join(c for c in nome if c.isalpha()) # Filtra apenas letras

# Operações
print(somente_letras.upper()) # Nome em letras maiúsculas, sem espaços
print(somente_letras.lower()) # Nome em letras minúsculas, sem espaços
print(len(somente_letras)) # Número de letras (sem espaços ou outros caracteres)
print(len(nome.split()[0])) # Primeiro nome e mostra a quantidade de string