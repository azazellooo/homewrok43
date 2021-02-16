from django.shortcuts import render


def calculate_view(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')
    elif request.method == 'POST':
        result = 0
        if request.POST.get('operation') == '+':
            result += int(request.POST.get('first_num')) + int(request.POST.get('second_num'))
        elif request.POST.get('operation') == '-':
            result += int(request.POST.get('first_num')) - int(request.POST.get('second_num'))
        elif request.POST.get('operation') == '*':
            result += int(request.POST.get('first_num')) * int(request.POST.get('second_num'))
        elif request.POST.get('operation') == '/':
            result += int(request.POST.get('first_num')) / int(request.POST.get('second_num'))
        context = {
            'result': f'Result: {request.POST.get("first_num")} {request.POST.get("operation")} {request.POST.get("second_num")} = {result}'
        }
        print(request.POST)
        print(context)
        return render(request, 'calculator.html', context)




# Create your views here.
