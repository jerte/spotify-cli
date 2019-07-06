import sys
import spotipy
import spotipy.util as util
from functions import *

func_dict = {'pause':pause, 'next':next_trak, 'previous':previous,
        'play':play, 'current':current}

scope = 'user-read-currently-playing user-modify-playback-state'

write_username = False

try:
    # username is only data kept right now, this will change
    with open('app_data.txt', 'r+') as f:
        username = f.readline()
        if username[0:5]=="user=":
            username = username[5:-1]

except FileNotFoundError:
    if len(sys.argv) > 1:
        username = sys.argv[1]
        write_username = True
    else:
        print('no username!')
        sys.exit(0)

token = util.prompt_for_user_token(username, scope,
        client_id='30ef960eff5741d0abb4cc9a8590a90f',
        client_secret='2924697078f2489caa831756d878fa54',
        redirect_uri='http://localhost:777/callback/')
    
if token:
    sp = spotipy.Spotify(auth=token)
    #sp.trace = False
    if write_username:
        with open('app_data.txt', 'w') as f:
            f.write("user="+username)

    if len(sys.argv) > 1:
        
        if not write_username:
            if len(sys.argv) > 2:
                result = func_dict[sys.argv[1]](sp, sys.argv[2:]) 
            else:
                result = func_dict[sys.argv[1]](sp, '')
        else:
            if len(sys.argv) > 3:
                result = func_dict[sys.argv[2]](sp, sys.argv[3:])
            elif len(sys.argv) > 2:
                result = func_dict[sys.argv[2]](sp, '')
            else:
                result = None
        
        if result:
            print(result)
        
    else:
        print('no function!')
    
else:
    print(f"Can't get token for {username}")


