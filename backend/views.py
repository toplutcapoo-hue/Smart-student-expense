import sys
import os
# This line tells the computer to look "up" one folder for your files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .import budget
from .import expense
from .import expense_service
from .import users
from .database import database
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense, Category


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'total_spent': total,
        'categories': Category.objects.all()
    })


@login_required
def add_expense(request):
    if request.method == 'POST':
        Expense.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            amount=request.POST.get('amount'),
            category_id=request.POST.get('category')
        )
    return redirect('dashboard')


from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
# Create your views here.
