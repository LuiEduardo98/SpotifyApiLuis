from os import name
import requests
import base64, json
from secrets import *

# curl -X "POST" -H "Authorization: Basic ZjM4ZjAw...WY0MzE=" -d grant_type=client_credentials https://accounts.spotify.com/api/token

authUrl = "https://accounts.spotify.com/api/token"
authHeader = {}
authData = {}

#Base 64 ASCII

def getAccessToken(clientID, clientSecret):
    message =  f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    #print(base64_message)

    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = "client_credentials"

    res = requests.post(authUrl, headers=authHeader, data=authData)

    responseObject = res.json()
    #print(json.dumps(responseObject, indent=2))

    accessToken = responseObject['access_token']

    return accessToken

def getPlaylistTracks(token, playlistID):
    playlistEndPoint = f"https://api.spotify.com/v1/playlists/{playlistID}"
    
    getHeader = {
        "Authorization": "Bearer " + token
    }
    
    res = requests.get(playlistEndPoint, headers=getHeader)
    
    playlistObject = res.json()
    
    return playlistObject

#API Request

token = getAccessToken(clientID, clientSecret)
playlistID = "7JibL9dQPNGmVXxl1s41nO?si=00efa65f45f84618"

tracklist = getPlaylistTracks(token, playlistID)

for t in tracklist['tracks']['items']:
    print('----------------------')
    for a in t['track']['artists']:    
        print(a['name'])
        
    songName = t['track']['name']
    print(songName)