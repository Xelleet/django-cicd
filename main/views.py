from django.shortcuts import render

def index(request):
    result = 0

    if request.method == 'POST':
        result = int(request.POST.get('num1')) + int(request.POST.get('num2'))

    return render(request, 'index.html', {'result': result})