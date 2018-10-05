# to run : python spotify_handler.py andrew.hartman60

import sys
import spotipy
import spotipy.util as util
import pprint
import json

# scope = 'user-library-read'
scope = 'playlist-modify-public'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username,scope,client_id='b88344a4fee44f7288144df4dd543165',client_secret='e4db5ec2567f46f68d0d2ce5f120572a',redirect_uri='http://localhost/')


playlist_id = ''

if token:
    sp = spotipy.Spotify(auth=token)
 	
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == 'XM CHILL MX':
            print(playlist)
            playlist_id = playlist['id']



    print playlist_id

    result = sp.search(q='Sons Of Maria', type='artist')
    # pprint.pprint(result)
    print json.dumps(result)

    print result['artists']['items'][0]['name']
    print result['artists']['items'][0]['id']


    top_tracks = sp.artist_top_tracks(result['artists']['items'][0]['id'])
    # print json.dumps(top_tracks)

    track_id = ''
    for track in top_tracks['tracks']:
        print track['name']
        if 'Break Through' in track['name']:
            track_id = track['id']
            print 'FOUND IT'

    added_track = sp.user_playlist_add_tracks(username, playlist_id, [track['id']])
    print added_track


else:
    print "Can't get token for", username









