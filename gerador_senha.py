#@ title **gerador de senha**
import string
import random
def gerar_senha(tamanho=8): #define tamanho da senha
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = "".join(random.choice(caracteres) for _ in range(tamanho))
  return senha

tamanho = int(input("digite o tamanho da senha: "))
senha = gerar_senha(tamanho)
print(f'Sua senha é : {senha}')