from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    
    user_id = request.user.social_auth.get(provider='vk-oauth2').uid    
    token = '3e625bfc3e625bfc3e625bfc1d3e09536933e623e625bfc629e4872951fb2558db71494'
    version = 5.52

    response = requests.get(
        'https://api.vk.com/method/friends.get',
        params={
            'user_id': user_id,
            'fields': 'nickname', 
            'access_token': token,
            'v': version,
            'count': 5 
           }
        )
    
    items = response.json()['response']['items']

    friend_list = []

    for i in items:
        friend_list.append(i['first_name'] + " " + i['last_name'])
    
    return render(request, 'home.html', locals())

