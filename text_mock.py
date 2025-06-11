import pytest
from unittest.mock import MagicMock
import requests

@pytest.fixture

def buscar_resposta_com_mock():
    mock = MagiMock(spec=request.Response)
    mock.status_code = 200
    mock.json.return_value ={'mensagem':'Acesso com sucesso'}
    return mock

def test_conferencia_resposa_com_mock():
    resposta = buscar_resposta_com_mock
    assert resposta.status_code ==200
    assert resposta.json() == {'mensagem':'Acesso com sucesso'}