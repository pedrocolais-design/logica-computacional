# Lista de mensagens simuladas
mensagens = [
    "Oi, como você está?",
    "Você viu aquele filme novo?",
    "Que horas você vai chegar?",
    "Vamos sair mais tarde?"
]

# Função para responder às mensagens
def responder(mensagem):
    print(f"Respondendo: {mensagem}")

# Loop para ler e responder até não houver mais mensagens
while mensagens:
    mensagem = mensagens.pop(0)  # Pega a primeira mensagem da lista
    print(f"Lendo mensagem: {mensagem}")
    responder(mensagem)

print("Não há mais mensagens.")

# Valor que você quer alcançar
valor_objetivo = 100

# Valor economizado por semana
economia_semanal = 10

# Variável para acompanhar o total economizado
total_economizado = 0

# Variável para contar as semanas
semanas = 0

# Loop while para economizar até alcançar o valor objetivo
while total_economizado < valor_objetivo:
    total_economizado += economia_semanal  # Adiciona a economia semanal ao total
    semanas += 1  # Conta mais uma semana

# Resultado final
print(f"Você precisará de {semanas} semanas para economizar R$ {valor_objetivo}.")


# Lista de presença com os nomes dos alunos
presenca = ["Ana", "Carlos", "Fernanda", "João", "Maria", "Lucas"]

# Nome do aluno que queremos verificar
aluno_procurado = "João"

# Loop para verificar se o aluno está na lista de presença
encontrado = False  # Variável para controlar se o aluno foi encontrado

for aluno in presenca:
    if aluno == aluno_procurado:
        encontrado = True
        break  # Encerra o loop assim que o aluno for encontrado

# Resultado
if encontrado:
    print(f"{aluno_procurado} está na sala.")
else:
    print(f"{aluno_procurado} não está na sala.")

