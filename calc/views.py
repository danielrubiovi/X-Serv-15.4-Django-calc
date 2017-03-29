from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def operaciones (self,num1,operando,num2):

	print ('NUM 2:'+ str(num2))

	if operando == '+':
		suma = int(num1) + int(num2)
		htmlAnswer = '<body><h3> La suma de '
		htmlAnswer += str(num1) + str(operando) + str(num2) + ' = '
		htmlAnswer += str(suma) + '</h3></body>'

	elif operando == '-':
		resta = int(num1) - int(num2)
		htmlAnswer = '<body><h3> La resta de '
		htmlAnswer += str(num1) + str(operando) + str(num2) + ' = '
		htmlAnswer += str(resta) + '</h3></body>'

	elif operando == '/':
		division = int(num1) / int(num2)
		htmlAnswer = '<body><h3> La division de '
		htmlAnswer += str(num1) + str(operando) + str(num2) + ' = '
		htmlAnswer += str(division) + '</h3></body>'

	elif operando == '*':
		multiplicacion = int(num1) * int(num2)
		htmlAnswer = '<body><h3> La multiplicacion de '
		htmlAnswer += str(num1) + str(operando) + str(num2) + ' = '
		htmlAnswer += str(multiplicacion) + '</h3></body>'

	else:
		htmlAnswer = '404 Not Found'

	return HttpResponse (htmlAnswer)