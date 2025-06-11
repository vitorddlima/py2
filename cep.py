import requests

def buscar_cep (cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}01001000/json/')
    
    if resposta.status_code != 200:
        return 'Cep Invalido'
    else:
        cep_encontrado = resposta.json()
        return cep_encontrado
    
cep =input("Informe o cep: ")
resultado = buscar_cep(cep)

print(f"Rua: {resultado['lograduro']}")
