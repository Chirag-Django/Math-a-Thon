from django.shortcuts import render
from random import randint

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def add(request):
    num1 = randint(0,10)
    num2 = randint(0,10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        if not answer:
            my_answer = 'You forgot to answer!'
            color = 'warning'
            return render(request, 'add.html',
                          {'num1': old_num1, 'num2': old_num2,'my_answer':my_answer, 'color':color})
        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct Answer! " + str(old_num1) + " + " + str(old_num2)  + " equals " + str(correct_answer)
            color = 'info'
        else:
            my_answer = "Incorrect Answer! " + str(old_num1) + " + " + str(old_num2) + ' is not equal to '+ answer  + "! It is " + str(correct_answer) +"!"
            color = 'danger'
        return render(request,'add.html', {'answer': answer, 'my_answer': my_answer,'num1': num1,'num2': num2, 'color':color})
    return render(request,'add.html', {'num1': num1,'num2': num2,})

def substract(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        if not answer:
            my_answer = 'You forgot to answer!'
            color = 'warning'
            return render(request, 'substract.html',
                          {'num1': old_num1, 'num2': old_num2,'my_answer':my_answer, 'color':color})
        correct_answer = int(old_num1) - int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct Answer! " + str(old_num1) + " - " + str(old_num2) + " equals " + str(correct_answer)
            color = 'info'
        else:
            my_answer = "Incorrect Answer! " + str(old_num1) + " - " + str(
                old_num2) + ' is not equal to ' + answer + "! It is " + str(correct_answer) + "!"
            color = 'danger'
        return render(request, 'substract.html',
                      {'answer': answer, 'my_answer': my_answer, 'num1': num1, 'num2': num2, 'color': color})
    return render(request, 'substract.html', {'num1': num1, 'num2': num2, })

def multiply(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        if not answer:
            my_answer = 'You forgot to answer!'
            color = 'warning'
            return render(request, 'multiply.html',
                          {'num1': old_num1, 'num2': old_num2,'my_answer':my_answer, 'color':color})
        correct_answer = int(old_num1) * int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct Answer! " + str(old_num1) + " x " + str(old_num2) + " equals " + str(correct_answer)
            color = 'info'
        else:
            my_answer = "Incorrect Answer! " + str(old_num1) + " x " + str(
                old_num2) + ' is not equal to ' + answer + "! It is " + str(correct_answer) + "!"
            color = 'danger'
        return render(request, 'multiply.html',
                      {'answer': answer, 'my_answer': my_answer, 'num1': num1, 'num2': num2, 'color': color})
    return render(request, 'multiply.html', {'num1': num1, 'num2': num2, })

def divide(request):
    num1 = randint(0, 10)
    num2 = randint(1, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        if not answer:
            my_answer = 'You forgot to answer!'
            color = 'warning'
            return render(request, 'divide.html',
                          {'num1': old_num1, 'num2': old_num2,'my_answer':my_answer, 'color':color})
        correct_answer = round((int(old_num1) / int(old_num2)),2)
        if round(float(answer),2) == correct_answer:
            my_answer = "Correct Answer! " + str(old_num1) + " / " + str(old_num2) + " equals " + str(correct_answer)
            color = 'info'
        else:
            my_answer = "Incorrect Answer! " + str(old_num1) + " / " + str(old_num2) + ' is not equal to ' + answer + "! It is " + str(correct_answer) + "!"
            color = 'danger'
        return render(request, 'divide.html',
                      {'answer': answer, 'my_answer': my_answer, 'num1': num1, 'num2': num2, 'color': color})
    return render(request, 'divide.html', {'num1': num1, 'num2': num2, })
