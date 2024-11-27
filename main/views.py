from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Question
import random

def home(request):
    questions = Question.objects.all().order_by('-timestamp')
    paginator = Paginator(questions, 17)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'questions':questions, 'questions': page_obj}
    return render(request, 'main/home.html', context)

def ask_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        ip_address = get_client_ip(request)
        answer = 'yes' if random.choice([True, False]) else 'no'
        Question.objects.create(text=question_text, ip_address=ip_address, answer=answer)
        return redirect('home')
    return redirect('home')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')
