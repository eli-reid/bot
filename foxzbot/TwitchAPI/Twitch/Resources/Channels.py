"""
Get Channel Information

request

curl -X GET 'https://api.twitch.tv/helix/channels?broadcaster_id=141981764' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz'


response
{
  "data": [
    {
      "broadcaster_id": "141981764",
      "broadcaster_login": "twitchdev",
      "broadcaster_name": "TwitchDev",
      "broadcaster_language": "en",
      "game_id": "509670",
      "game_name": "Science & Technology",
      "title": "TwitchDev Monthly Update // May 6, 2021",
      "delay": 0,
      "tags": ["DevsInTheKnow"]
    }
  ]
}

"""
from . import Utils
from . import Scope 
from typing import Optional

class ChannelInformationRequest(Utils.RequestBaseClass):
    requestType = "GET"
    scope = None
    requirements = ["app access token","user access token"]
    endPoint = "/channels"
    def __init__(self, broadcaster_ids: list[str]) -> None:
        self.broadcaster_ids: list[str] = broadcaster_ids
        super().__init__()




"""
Modify Channel Information

scope:  channel:manage:broadcast 

request
curl -X PATCH 'https://api.twitch.tv/helix/channels?broadcaster_id=41245072' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \
-H 'Content-Type: application/json' \
--data-raw '{"game_id":"33214", "title":"there are helicopters in the game? REASON TO PLAY FORTNITE found", "broadcaster_language":"en", "tags":["LevelingUp"]}'

response 
204 success
400 bad request data
401 Unauthorized
500 Internal server error

"""

"""
Get Channel Editors

Scope: channel:read:editors

request:
curl -X GET 'https://api.twitch.tv/helix/channels/editors?broadcaster_id=141981764' \
-H 'Authorization: Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx' \
-H 'Client-Id: wbmytr93xzw8zbg0p1izqyzzc5mbiz' \

response:

{
  "data": [
    {
      "user_id": "182891647",
      "user_name": "mauerbac",
      "created_at": "2019-02-15T21:19:50.380833Z"
    },
    {
      "user_id": "135093069",
      "user_name": "BlueLava",
      "created_at": "2018-03-07T16:28:29.872937Z"
    }
  ]
}

"""

"""
Get Followed Channels - BETA

Scope: user:read:follows

request: Gets the list of broadcasters that the specified user follows.

curl -X GET 'https://api.twitch.tv/helix/channels/followed?user_id=123456' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response
{
  "total": 8
  "data": [
    {
      "broadcaster_id": "11111",
      "broadcaster_login": "userloginname",
      "broadcaster_name": "UserDisplayName",
      "followed_at": "2022-05-24T22:22:08Z",
    },
    ...
  ],
  "pagination": {
    "cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6NX19"
  }
}


request: Checks whether the specified user follows the specified broadcaster.

curl -X GET 'https://api.twitch.tv/helix/channels/followers?user_id=123456&broadcaster_id=654321' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response:

{
  "total": 8
  "data": [
    {
      "broadcaster_id": "654321",
      "broadcaster_login": "basketweaver101",
      "broadcaster_name": "BasketWeaver101",
      "followed_at": "2022-05-24T22:22:08Z",
    }
  ],
  "pagination": {}
}

"""


"""
Get Channel Followers - BETA

scope: moderator:read:followers

requirements --
The ID in the broadcaster_id query parameter must match the user ID in the access token or the user must be a moderator for the specified broadcaster. If a scope is not provided, only the total follower account will be included in the response.

request: - Gets the list of users that follow the specified broadcaster.

curl -X GET 'https://api.twitch.tv/helix/channels/followers?broadcaster_id=123456' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response:

{
  "total": 8
  "data": [
    {
      "user_id": "11111",
      "user_name": "UserDisplayName",
      "user_login": "userloginname",
      "followed_at": "2022-05-24T22:22:08Z",
    },
    ...
  ],
  "pagination": {
    "cursor": "eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6NX19"
  }
}

request: - Checks whether the specified user follows the specified broadcaster.

curl -X GET 'https://api.twitch.tv/helix/channels/followers?broadcaster_id=123456&user_id=654321' \
-H 'Authorization: Bearer kpvy3cjboyptmiacwr0c19hotn5s' \
-H 'Client-Id: hof5gwx0su6owfn0nyan9c87zr6t'

response: - The data field is an empty array, which means the user doesn't follow the specified broadcaster.

{
  "total": 8
  "data": [],
  "pagination": {}
}
"""
