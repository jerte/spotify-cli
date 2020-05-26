#!/usr/bin/env python

import sys
import os
from .functions import *
import spotipy
import spotipy.util as util


# function to run cli
def run_cli(username, write_username):
    # command line options
    func_dict = {'pause':pause, 'next':next_trak, 'previous':previous,
            'play':play, 'current':current, 'shuffle':shuffle, 'list':list_}

    client_id = '30ef960eff5741d0abb4cc9a8590a90f'
    client_secret='2924697078f2489caa831756d878fa54'
    redirect_uri = "http://localhost:7777/callback/"
    scope = 'user-read-currently-playing user-modify-playback-state'
 
    token = util.prompt_for_user_token(username,scope,
                    client_id,client_secret,redirect_uri)
    if token:
        if write_username:
            file_path = os.path.dirname(os.path.abspath(__file__)) + '/data/username.txt'
            with open(file_path, 'w+') as f:
                f.write("user="+username)
        else:
            if len(sys.argv) > 1:
                sp = spotipy.Spotify(auth=token)
                try:
                    result = func_dict[sys.argv[1]](sp, sys.argv[1:])
                    if result:
                        print(result)
                except KeyError:
                    print('function \''+ sys.argv[1] + '\' not found')
                    sys.exit(0)
            else:
                print('no function provided')
    else:
        print('No token')

def main():
    try:
        file_path = os.path.dirname(os.path.abspath(__file__)) + '/data/username.txt'

        with open(file_path, 'r+') as f:
            username = f.readline()
            if username[0:5]=="user=":
                username = username[5:-1]

            run_cli(username, write_username=False)

    except FileNotFoundError:
        if len(sys.argv) > 1:
            username = sys.argv[1]

            run_cli(username, write_username=True)
        else:
            username = input('Enter username: ')
            
            run_cli(username, write_username=True)


if __name__ == "__main__":
    main()
    
