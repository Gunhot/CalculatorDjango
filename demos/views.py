from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculator(request):
    #데이터 받아오기
    # num1 = int(request.GET.get('num1'))
    # num2 = int(request.GET.get('num2'))
    # operators = request.GET.get('operators')
    # #request로부터 해당 변수의 이름을 GET으로 가져온다
    
    # #데이터 계산
    # if operators == '+':
    #     result = num1 + num2
    # elif operators == '-':
    #     result = num1 - num2
    # elif operators == '*':
    #     result = num1 * num2
    # elif operators == '/':
    #     if num2 == 0 :
    #         result = 0
    #     else :
    #         result = num1 / num2
    # else :
    #     result = 0
    
    # #데이터 응답
    # #result라는 변수를 result라는 이름으로 사용가능해진다
    # return render(request, 'calculator.html', {'a' : str(result)})
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')
    #request로부터 해당 변수의 이름을 GET으로 가져온다
    
    #데이터 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        if num2 == 0 :
            result = 0
        else :
            result = int(num1) / int(num2)
    else :
        result = 0
    
    #데이터 응답
    #result라는 변수를 result라는 이름으로 사용가능해진다
    return render(request, 'calculator.html', {'a' : str(result)})

    # 이것은 templates는 써서 return 한 것
    # request랑 template이름은 필수야
    # templates폴더는 같은 위치에...
    #redirect와의 차이 : redirect는 이동 + render는 가져오기

    # return HttpResponse("계산기 시작")
    # 이것은 어떠한 model과 template을 사용하지는 않은 것
