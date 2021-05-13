from django.shortcuts import render

def calculate(request):
    return render(request, "calculate.html")

def result(request):
    firstNumber = int(request.GET['firstnumber'])
    secondNumber = int(request.GET['secondnumber'])
    select = request.GET['select']

    
    if select == '+':
        result=firstNumber+secondNumber
    if select == '-':
        result=firstNumber-secondNumber
    if select== '*':
        result=firstNumber*secondNumber
    if select== '/':
        if secondNumber==0:
            result="division by zero"
        else:
            result=firstNumber/secondNumber

    return render(request, 'result.html', {'result' : result})