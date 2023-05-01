from django.shortcuts import render
from django.http import JsonResponse
import os 
from .models import Word
from . word_utils import is_valid_word, is_fancy_word, comp_response
# Create your views here.

def home(request):

    if request.method == 'POST':
        computer_word = "waiting..."
        current_word = request.POST.get('current_word', '')
        print("Entered word is: ", current_word)
        if is_valid_word(current_word):
            computer_word = comp_response()
            if is_fancy_word(current_word):
                message = "valid and fancy"
            else:
                message = "valid but not fancy"
        else:
            message = "invalid"
        return render(request, 'home.html', {'current_word':current_word, 'computer_word':computer_word,'message':message})

    else:
        current_word = "undetected"
        message = "waiting"
    # if request.method == 'POST':
    #     current_word = request.POST['current_word']
    #     current_player = request.POST['current_player']
    #     next_word = request.POST['next_word']
    #     if is_valid_word(current_word):
    #         if is_fancy_word(current_word):
    #             # word = Word(word=next_word, player=current_player)
    #             # word.save()

    #             current_word = next_word
    #             message = "You scored a point!"

    #         else:
    #             message = "Invalid word!"
    # else:
    #     message = "Invalid word!"
    #     current_word = ''
    #     message = "Welcome to the game!"

    # try:
    # #     previous_word = Word.objects.latest('timestamp')
    #     # previous_player = previous_word.player
    #     cuurent_word = ''
    #     message = "Let's go!"
    # except Word.DoesNotExist:
    #     previous_word = ''
    #     previous_player = ''

    return render(request, 'home.html', {'current_word':current_word, 'message':message})


    