import sys
import os
from functions import *
import spotipy
import spotipy.util as util

# command line options
func_dict = {'pause':pause, 'next':next_trak, 'previous':previous,
        'play':play, 'current':current}
client_id = '30ef960eff5741d0abb4cc9a8590a90f'
client_secret='2924697078f2489caa831756d878fa54'
redirect_uri = "http://localhost:7777/callback/"
scope = 'user-read-currently-playing user-modify-playback-state'

# function to run cli
def run_cli(username, write_username):
        token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)
        if token:
            if write_username:
                with open('app_data.txt', 'w') as f:
                    f.write("user="+username)
            else:
                if len(sys.argv) > 1:
                    sp = spotipy.Spotify(auth=token)
                    try:
                        result = fuct_dict[sys.argv[1]](sp, sys.argv[1:])
                        if result:
                            print(result)
                    except KeyError:
                        print('function \''+ sys.argv[1] + '\' not found')
                        sys.exit(0)
                else:
                    print('no function provided')

# get username, from file or passed cli option, then run cli
if __name__ == "__main__":
    try:
        with open('app_data.txt', 'r+') as f:
            username = f.readline()
            if username[0:5]=="user=":
                username = username[5:-1]

            run_cli(username, write_username=False)

    except FileNotFoundError:
        if len(sys.argv) > 1:
            username = sys.argv[1]

            run_cli(username, write_username=True)
        else:
            print('Sign in by passing Spotify username as option')
            sys.exit(0)
