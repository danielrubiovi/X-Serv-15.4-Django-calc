from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def operaciones (self,num1,operando,num2):

	if operando == '+':
		suma = int(num1) + int(num2)
		htmlAnswer = '<body><h3> La suma da: '
		htmlAnswer += str(suma) + '</h3></body>'

	elif operando == '-':
		resta = int(num1) - int(num2)
		htmlAnswer = '<body><h3> La resta da: '
		htmlAnswer += str(resta) + '</h3></body>'

	elif operando == '/':
		division = int(num1) / int(num2)
		htmlAnswer = '<body><h3> La division da: '
		htmlAnswer += str(division) + '</h3></body>'

	elif operando == '*':
		multiplicacion = int(num1) * int(num2)
		htmlAnswer = '<body><h3> La multiplicacion da: '
		htmlAnswer += str(multiplicacion) + '</h3></body>'

	else:
		htmlAnswer = '404 Not Found'

	return HttpResponse (htmlAnswer)