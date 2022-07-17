from enum import unique
import requests

def getAccessToken():
    auth_url = 'https://accounts.spotify.com/api/token'
    clientID = "204d99eaea4044d08a4d5c06444cb58a"
    clientSecret = "ac11837bbd6e410da35bcbd3a1b05a7c"

    data = {
        'grant_type': 'client_credentials',
        'client_id': clientID,
        'client_secret': clientSecret,
    }

    auth_response = requests.post(auth_url, data = data)
    access_token = auth_response.json().get('access_token')
    return access_token

def getUserPlaylists(userID):
    baseURL = "https://api.spotify.com/v1/"
    endpoint = "users/" + userID + "/playlists?limit=5"

    headers = {
        'Authorization': 'Bearer {}'.format(getAccessToken())
    }

    playList_URL = baseURL + endpoint
    response = requests.get(playList_URL, headers = headers)

    ids = []

    for i in range(len(response.json().get('items'))):
        ids.append(response.json().get('items')[i].get('id'))
    
    return ids

def getUserSongs(playID):
    baseURL = "https://api.spotify.com/v1/"
    endpoint = "playlists/" + playID + "/tracks"

    headers = {
        'Authorization': 'Bearer {}'.format(getAccessToken())
    }

    songURL = baseURL + endpoint
    response = requests.get(songURL, headers = headers)

    songs = []

    for i in range(len(response.json().get('items'))):
        songs.append(response.json().get('items')[i].get('track').get('name'))

    return songs

# x = requests.get('https://api.spotify.com/v1/users/lq752or3h753l1eym1llu4v14/playlists')
# print(getAccessToken())

def get:
    "ySL_3VVusXDXnSmVH5U4wNq2hE9dQWVXrA6rVwuwSAFHMDXFVYbUActeERV_zpBZ"

    "jSYJSwghDhXJjSJK__J1WrB5oDiygSq-A2MV7zdzxCgJF0y6NAfOd7U3mzzMZzo1YL2pGePy38VX8Y-IpTQGcg"

if __name__ == "__main__":
    userID = "lq752or3h753l1eym1llu4v14"
    playlists = getUserPlaylists(userID)
    songs = list(map(getUserSongs, getUserPlaylists(userID)))
    #uniqueSongs = set(songs)
    print(songs)