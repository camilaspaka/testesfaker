import json
from faker import Faker
import random

fake = Faker('pt_BR')

def gerar_documento():
    tipo_documento = fake.random_element(['RG', 'CPF', 'CNH'])
    return {'documento': fake.numerify('############'), 'tipoDocumento': tipo_documento}

def gerar_telefone():
    return {
        'codigoTelefone': fake.random_int(min=1, max=9999999),
        'tipoTelefone': fake.random_element(['Cel', 'Res']),
        'ddd': fake.random_int(min=10, max=99),
        'numeroTelefone': fake.numerify('###########'),
        'pais': 'Brasil',
        'contato': fake.random_element(['S', 'N'])
    }

def gerar_endereco():
    return {
        'codigoEndereco': fake.random_int(min=1, max=9999999),
        'tipoEndereco': fake.random_element(['C', 'P']),
        'logradouro': fake.random_element(['Casa', 'Condominio', 'Predio']),
        'numero': fake.building_number(),
        'complemento': fake.random_element(['Bloco A', 'Sala 101', 'Casa 2']),
        'bairro': fake.bairro(),
        'cidade': fake.city(),
        'uf': fake.random_element(['SP', 'RJ', 'MG', 'RS', 'SC', 'PR', 'BA', 'CE', 'PE', 'DF']),
        'cep': fake.numerify('########'),
        'pais': 'Brasil',
        'contato': fake.random_element(['S', 'N'])
    }

def gerar_email():
    return {
        'codigoEmail': fake.random_int(min=1, max=9999999),
        'tipoEmail': fake.random_element(['P', 'T']),
        'email': fake.free_email(),
        'contato': fake.random_element(['S', 'N'])
    }

def gerar_cliente():
    cliente = {
        'cliente': {
            'idCliente': fake.random_int(min=1, max=9999999),
            'tipoCliente': 'PF',
            'nomeCliente': fake.name(),
            'nomeSocial': fake.name(),
            'nomePai': fake.first_name_male(),
            'nomeMae': fake.first_name_female(),
            'genero': fake.random_element(['F', 'M']),
            'estadoCivil': fake.random_element(['S', 'C', 'D', 'V']),
            'score': fake.random_int(min=0, max=10),
            'patrimonio': round(fake.random.uniform(0, 1000000), 2),
            'nascimento': fake.date_of_birth(minimum_age=18).strftime('%Y-%m-%d'),
            'pep': fake.random_element(['S', 'N']),
            'documentos': {
                'cpf': fake.numerify('###########'),
                'documentos': [gerar_documento()]
            },
            'telefones': [gerar_telefone()],
            'enderecos': [gerar_endereco()],
            'emails': [gerar_email()],
        },
    }
    return cliente

# Gera dados para 300 clientes
clientes = [gerar_cliente() for _ in range(300)]

# Estrutura do arquivo JSON
estrutura_json = {"clientes": clientes}

# Salva os dados em um arquivo JSON
with open('dados.json', 'w', encoding='utf-8') as json_file:
    json.dump(estrutura_json, json_file, ensure_ascii=False, indent=2)

print("Dados exportados para dados.json.")
