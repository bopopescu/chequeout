from django.shortcuts import render
from . import process_dialog
from django.shortcuts import redirect
from amzsear import AmzSear
import os
import json
from pprint import pprint
from . import scrape
import time

dialog_response = ''
project_id = 'checkout-231218'
session_id = 0
language_code = "en"

# Create your views here.
def chat(request):
    return render(request, 'chat/chat.html', {})
def dialog(request):
    # TODO: pass in dialog_response for context

    if request.method == "POST":
        texts = [request.POST['message']]
        entities = scrape.detect_items(texts[0])
        item_list = []
        card = ''
        for entity in entities:
            print(u'{:<16}: {}'.format('name', entity.name))
            item_list.append(entity.name)
        print(item_list)
        dialog_response = process_dialog.detect_intent_texts(project_id, session_id, texts, language_code)
        for item in item_list:
            print("amzsear '" + item + "' -d -o json > chat/output.json")
            os.system("amzsear '" + item + "' -d -o json > chat/output.json" )
            time.sleep(3)
            while(True):
                with open('chat/output.json') as f:
                    data = json.load(f)
                    print(data)
                    if data != {}:
                        card += scrape.return_card_string()
                        break
                    else:
                        os.system("amzsear '" + item + "' -d -o json > chat/output.json" )


        print(card)
    return render(request, 'chat/dialog.html', {'message': dialog_response,
                                                'response': card})
def result(request):
    # TODO: pass in the final results after running web scraping scripts
    return render(request, 'chat/result.html', {})
