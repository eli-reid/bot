from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.middleware.csrf import get_token
from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from .Twitch.oauth import twitchOauth

TOA = twitchOauth("l2fn9r2aceogfbjebk6ufcapa8s92q","m9i6zzis2mdkfwu6u7aibuo4acumak","moderator:read:chatters+moderation:read")

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