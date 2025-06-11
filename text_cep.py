import pytest
import requests

@pytest.fixture
def consulta_cep():
    resposta = requests.get('https://viacep.com.br/ws/01001000/json/')
    
    if resposta.status_code != 200:
        return 'Cep não encontrado'
    
    else:
        resposta.status_code= 200
        resposta.json()
        
        return resposta
global resposta


def test_cep_nao_encontrada(consulta_cep):
    resposta = consulta_cep
    assert not resposta == 'Cep não encontrado'
    
def teste_encontra_logradura(consultar_cep):
    resposta = consulta_cep
    assert rua ['logradouro'] =='Rua Tapajos'
    
       
def teste_encontra_logradura(consultar_cep):
    resposta = consulta_cep
    assert rua ['bairro'] =='Bom Retiro'
    
    
def teste_encontra_logradura(consultar_cep):
    resposta = consulta_cep
    assert rua ['estado'] =='Paraná'
        