from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.middleware.csrf import get_token
from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.conf import settings
from .Twitch.Resources.Bits import BitsLeaderboardResponse, CheermotesItem, CheermotesResponse
from .Twitch.oauth import twitchOauth
from .Twitch.TwitchAPI import twitchAPI,TwitchApiUnauthorizedException
from .Twitch.Resources import Scope
import json

TOA = twitchOauth("l2fn9r2aceogfbjebk6ufcapa8s92q","m9i6zzis2mdkfwu6u7aibuo4acumak",
        scope=f"{Scope.Moderator.Read.Chatters}+\
                {Scope.Moderation.Read}")

@method_decorator(login_required, "get")
class APIOauth(View):
    template_name = "oauth.html"

    def get(self, request, *args, **kwargs):
        token = get_token(request)
        url =TOA.getCodeURL(token)
        return HttpResponseRedirect(url)

class GetCodeView(View):
   async def get(self, request: HttpRequest, *args, **kwargs):
        data = request.GET
        code = data.get("code")
        state = data.get("state")
        jsondata =await TOA.getToken(code)
        token = jsondata.get('access_token')
        refresh_token = jsondata.get('refresh_token')
        if state == TOA._csrf:
            return HttpResponse(f"appoved:{jsondata}"  )
        else:
            return HttpResponse("failed")

class makeApiCall(View):
    async def get(self, request: HttpRequest, *args, **kwargs):
        TAPI= twitchAPI(settings.FOXZBOT_CLIENT_ID,"Ghjshjcdjhsgcdosgco","","")
        try:
            look: CheermotesResponse = await TAPI.GetCheermotes()
        except TwitchApiUnauthorizedException as err:
            print(err)
            return HttpResponse(f"<pre>{err}</pre>")
        
        
        return HttpResponse(f"<pre>{json.dumps(look.raw, indent=4, separators=(',', ': '))}</pre>")
    
