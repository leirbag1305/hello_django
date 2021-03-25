from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, num1, num2):
    saida = num1 + num2
    return HttpResponse('<h1>Soma de {} + {} = {}</h1>' .format(num1, num2, saida))
def subtracao(request, num1, num2):
    saida = num1 - num2
    return HttpResponse('<h1>Subtração de {} - {} = {}</h1>' .format(num1, num2, saida))
def multiplicacao(request, num1, num2):
    saida = num1 * num2
    return HttpResponse('<h1>Multiplicação de {} * {} = {}</h1>' .format(num1, num2, saida))
def divisao(request, num1, num2):
    saida = num1 / num2
    return HttpResponse('<h1>Divisão de {} / {} = {}</h1>' .format(num1, num2, saida))
