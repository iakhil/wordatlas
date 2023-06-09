from django.shortcuts import render
from django.http import JsonResponse
import os 
import json 
import requests 
from .models import Word
from . word_utils import is_valid_word, is_fancy_word, comp_response, comp_response_up
# Create your views here.
all_comp_words = [] 

def get_meaning(word):

    req = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
    data = json.loads(requests.get(req).text)
    if len(data) == 1:
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
    else:
        meaning = "Definition not available."
    return meaning

def home(request):

    score = request.session.get('score', 0)
    if request.method == 'POST':
        current_word = request.POST.get('current_word', '')
        ending_letter_user = current_word[-1]
        #computer_word = all_comp_words[-2] if len(all_comp_words) > 1 else all_comp_words[-1]
        # all_comp_words.append(comp_response())
        # computer_word = all_comp_words[-2]
        # ending_letter_comp = computer_word[-1]
        message = "default messsage"
        print("Entered word is: ", current_word)
        if is_valid_word(current_word):
            if len(all_comp_words) > 0:
                ending_letter_comp = all_comp_words[-1][-1]
                if current_word[0] != ending_letter_comp:
                    message = f"Word should begin with the letter: {ending_letter_comp}"

            if is_fancy_word(current_word):
                message = "Valid and fancy"
                score += 1
            else:
                message = "Valid but not fancy"
                request.session['score'] = 0
                score = 0
        else:
            message = "invalid"
            score = 0
            request.session['score'] = 0

        computer_word = comp_response_up(ending_letter_user)
        comp_word_meaning = get_meaning(computer_word)
        ending_letter_comp = computer_word[-1]
        all_comp_words.append(computer_word) 

        request.session['score'] = score
        return render(request, 'home.html', {'score': score, 'comp_word_meaning': comp_word_meaning, 'ending_letter':ending_letter_comp, 'computer_word':computer_word,'message':message, 'all_comp_words':all_comp_words})

    else:
        request.session['score'] = 0
        message = "Welcome to the game!"
        # ending_letter = all_comp_words[-1][-1]
        # computer_word = all_comp_words[-1]
        message = "Enter your first word!"
        return render(request, 'home.html', {'score': score, 'ending_letter':"NA", 'computer_word':"NA",'message':message, 'all_comp_words':all_comp_words})

    