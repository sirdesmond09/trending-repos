from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
import requests
# Create your views here.

    
@api_view(['GET'])
def trending(request):
    
    last_30_days = timezone.now() - timezone.timedelta(days=30)

    response = requests.get(f'https://api.github.com/search/repositories?q=created:>{last_30_days.date()}&sort=stars&order=desc')

    items = response.json()['items']

    data = {}

    for item in items:
        language = item['language']

        if language in data.keys():
            data[language]['no_of_repos'] +=1
            data[language]['repos'].append(item)

        else:
            data[language]= {'no_of_repos': 1}
            data[language]['repos']= [item]


    response_data = {
        'response_code' : status.HTTP_200_OK,
        'message' : 'success',
        'data' : data
        
    }
    return Response(response_data, status=status.HTTP_200_OK)