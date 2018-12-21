import spotipy
import spotipy.oauth2 as oauth2
import requests
from bs4 import BeautifulSoup

client_secret =
client_id =

#you have to fill these in yourself ^



def generate_token():
    """ Generate the token. Please respect these credentials :) """
    credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)
    token = credentials.get_access_token()
    return token


def write_tracks(text_file, tracks):
    with open(text_file, 'w') as file_out:
        while True:
            for item in tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                try:
                    track_url = track['external_urls']['spotify']
                    file_out.write(track_url + '\n')
                except KeyError:
                    print(u'Skipping track {0} by {1} (local only?)'.format(
                            track['name'], track['artists'][0]['name']))
            # 1 page = 50 results
            # check if there are more pages
            if tracks['next']:
                tracks = spotify.next(tracks)
            else:
                break


playlist = input("Write link of spotify playlist ")
playlist_id = (str(playlist).replace('https://open.spotify.com/playlist/', ''))

token = generate_token()
spotify = spotipy.Spotify(auth=token)

# example playlist
username = "joosthoi1"


results = spotify.user_playlist(username, playlist_id,
                                fields='tracks,next,name')
text_file = u'{0}.txt'.format(results['name'], ok='-_()[]{}')
print(u'Writing {0} tracks to {1}'.format(
        results['tracks']['total'], text_file))
tracks = results['tracks']
write_tracks(text_file, tracks)

f = open(text_file, 'r')
myList = []
for line in f:

    data = requests.get(line.rstrip())
    soup = BeautifulSoup(data.text, 'html.parser')


    for meta in soup.find_all('meta', { 'property': 'og:title' }):
        print("%s" % meta)

    meta_string = str(meta).replace('<meta content="','').replace('" property="og:title"/>','')
    print(meta_string)

    text_file_finale = str(text_file).replace('.txt', ' finale.txt')

    finaltext = open(text_file_finale, 'a+')
    finaltext.write("%s\n" % meta_string)
    finaltext.close()

    myList.append(line)
    print(line.rstrip())




f.close()


# sudo apt-get install python3-pip
# pip3 install unicornhat
