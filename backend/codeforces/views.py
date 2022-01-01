from django.http import response
import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
import jwt, datetime

# Create your views here.

class AddUserView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!Please Login to see the scoreboard')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!Please Login to see the scoreboard')
        
        user = User.objects.filter(id=payload['id']).first()
        user.cf_handle = request.data['cf_handle']
        user.save()
        response = Response(status=status.HTTP_200_OK)
        return response

class CFUsersView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!Please Login to see the scoreboard')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!Please Login to see the scoreboard')
        cfuserInfoApiURL = 'https://codeforces.com/api/user.info?handles='
        user_handles = User.objects.values('cf_handle')
        for handle in user_handles:
            cfuserInfoApiURL += handle['cf_handle']+';'
        cfuserInfoApiURL = cfuserInfoApiURL[:-1]
        r = requests.get(cfuserInfoApiURL)
        response = Response(r.json(), status=status.HTTP_200_OK)
        return response
