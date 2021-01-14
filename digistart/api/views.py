from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
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
            
            print(operacoes)
            print(valores_base10)
            
        return Response(data_return, status=status_return)

    