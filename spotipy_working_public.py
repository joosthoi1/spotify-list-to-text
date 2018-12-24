import spotipy
import spotipy.oauth2 as oauth2
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


client_secret = input("input your client id, find out more at: https://developer.spotify.com/documentation/general/guides/authorization-guide/ \n")
client_id =  input("input your client id, find out more at: https://developer.spotify.com/documentation/general/guides/authorization-guide/ \n")
#you have to fill these in yourself ^ (not anymore)
chromedriverdir = input("where do you have your chromedriver.exe (should be in the project's file) e.g. C:/Users/user/Desktop/chromedriver.exe\n")

driver = webdriver.Chrome(executable_path=chromedriverdir)



def generate_token():
    """ Generate the token. Please respect these credentials :) """
    credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)
    token = credentials.get_access_token()
    return token

def write_tracks(text_file, tracks):
    with open(location + text_file, 'w') as file_out:
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
location = input("where do you want the text file? e.g.: C:/Users/user/Desktop/ (leave empty to generate in script folder) ")

token = generate_token()
spotify = spotipy.Spotify(auth=token)

# example playlist
username = "hello"


results = spotify.user_playlist(username, playlist_id,
                                fields='tracks,next,name')
text_file = u'{0}.txt'.format(results['name'], ok='-_()[]{}')
print(u'Writing {0} tracks to {1}'.format(
        results['tracks']['total'], text_file))
tracks = results['tracks']
write_tracks(text_file, tracks)



f = open(location + text_file, 'r')
myList = []
for line in f:

    data = requests.get(line.rstrip())
    soup = BeautifulSoup(data.text, 'html.parser')


    for meta in soup.find_all('meta', { 'property': 'og:title' }):
        print("%s" % meta)

    meta_string = str(meta).replace('<meta content="','').replace('" property="og:title"/>','')
    print(meta_string)

    song = "%s\n" % meta_string
    songlink = 'https://chorus.fightthe.pw/search?query=name%3D"' + song + '"'
    print(songlink)

    try:
        driver.get(songlink)
        time.sleep(1)
        elem1 = driver.find_element_by_partial_link_text('Download ')
        elem1.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        print(str(driver.current_url))
        download = str(driver.current_url).replace('/view', '&export=download').replace('/edit', '&export=download').replace('file/d/', 'uc?id=')
        driver.get(download)
        print(download)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except Exception:
        badsong = open(location + 'badsongs.txt', 'a+')
        badsong.write(meta_string)
        badsong.close()
        pass

    text_file_finale = str(text_file).replace('.txt', ' finale.txt')

    finaltext = open(location + text_file_finale, 'a+')
    finaltext.write("%s\n" % meta_string)
    finaltext.close()

    myList.append(line)
    print(line.rstrip())




f.close()
