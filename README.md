# Desafio digistart Software

Foi escolhida a opção 2 **Problmea da operação em binário**, fazendo um WEB REST capaz de operar um expressão de números binários, retornando a resposta também em números binários.

Aceitando-se os seguintes operadores

- (+) adição

- (-) subtração

- (/) divisão

- (*) multiplicação

- (%) porcentagem



**Requisitos**

- Python



**Inicialização**

- Acessar o diretório e executar os comandos `pip install -r requirement.txt `

- Agora basta iniciar a aplicação com o comando `python manage.py runserver`



**Requisição**

Deve ser realizado uma requisição POST para o endereço http://localhost:8000/api/binarie



**Request**

- Pode ser pasado mais de um operador entre os valores

- É necessário a chave do JSON estar nomeada como **expression**

- É necessário informar no mínimo uma operação (dois valores e o sinal da operação entre eles)



**Exemplo 1**

```json
{ "expression": "110010 + 10100 " }
```

**Exemplo 2**

```json
{ "expression": "110010 + 10100 * 100" }
```



**Response  - Sucesso**

```json
{
    "sucess": true,
    "message": {
        "result": "1001000",
        "decimalExpression": "18 * 4",
        "decimalResult": 72
    }
}
```


