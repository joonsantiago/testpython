from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import math

# Create your views here.


# api_view
@api_view(['POST'])
def member_api(request):
    """
    API endpoint that allows member to be viewed or edited made by function.
    """
    if request.method == 'POST':
        
        expression = ""
        sucess = True      
        
        data_return = {
            "sucess": True,
            "message": ""
        }
        
        status_return = status.HTTP_200_OK
        
        try:
            expression = request.data['expression']
        except:
            status_return = status.HTTP_406_NOT_ACCEPTABLE
            data_return["sucess"] = False
            data_return["message"] = "The 'expression' field is required."
            sucess = False
        
        if sucess:
            expression = expression.strip()
            valores_base10, operacoes = serializerBinarieExpression(expression)
                        
            if(len(valores_base10) < 2 or len(operacoes) == 0):
                status_return = status.HTTP_406_NOT_ACCEPTABLE
                data_return["sucess"] = False
                data_return["message"] = "Required send two binaries values and minimun one operation."
                sucess = False
        
        if(sucess):
            try:
                total, expression_decimal = serializerDecimalExpression(valores_base10, operacoes)
                total_binario = decimalToBinarie(total)
                
                resp = {
                    "result": total_binario,
                    "decimalExpression": expression_decimal,
                    "decimalResult": total
                }
                data_return["message"] = resp
            except:
                status_return = status.HTTP_406_NOT_ACCEPTABLE
                data_return["sucess"] = False
                data_return["message"] = "An invalid or uninterpretable value was reported."
                sucess = False
                                        
            
        return Response(data_return, status=status_return)


def serializerBinarieExpression(expression):
    
    valores = []
    operacoes = []
    valores_base10 = []
    v = ""       
    
    for i in range(len(expression)):
        char =  expression[i]
        if(char == "1" or char == "0"):
            v += (char)
        else:
            if(char.strip() != ""):
                operacoes.append(char)
                
            if(v != ""):
                valores.append(v)
            v = ""
    else:
        valores.append(v)
    
    
    for i in valores:
        size_number = len(i) -1
        sum = 0
        for j in range(len(i)):
            exp = size_number - j
            sum += (2 ** exp) * int(i[j])
        else:
            valores_base10.append(sum)
            
    return valores_base10, operacoes 
 
def makeOperation(value_one, value_two, operation):
    if operation == "+":
        return value_one + value_two
    elif operation == "-":
        return value_one - value_two
    elif operation == "*":
        return value_one * value_two
    elif operation == "/":
        return value_one / value_two
    elif operation == "%":
        return (value_two * value_one) / 100
    
    return 0
    
    
def decimalToBinarie(valor):
    
    value_str = ""
    division = valor
    
    while division > 1:
        v = division / 2
        decimal, integer = math.modf(v)
        value_str = "1" + value_str if decimal > 0 else "0" + value_str
        division = integer
    else:
        value_str = "1" + value_str if division == 1 else "0" + value_str
    
    return value_str

def serializerDecimalExpression(valores_base10, operacoes):
    expression_decimal = ""
    total = 0
    for i in range(len(valores_base10)):
        if(i == 0):
            total = valores_base10[i]
            expression_decimal += "%s " % (total)
        else:                    
            v = valores_base10[i]
            op = operacoes[(i - 1)]
            total = makeOperation(total, v, op)
            expression_decimal += "%s %s " % (op, v)
        

    total = (total * -1) if total < 0 else total 
    
    return total, expression_decimal.strip()