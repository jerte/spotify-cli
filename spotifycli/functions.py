import sys
import spotipy
import spotipy.util as util
import json
# command line options, made to be verbose 

# pause playback
def pause(sp, arg_list):
    if len(arg_list) > 1:
        return "bad usage!"
    sp.pause_playback()
    return None

# skip to next track
def next_trak(sp, arg_list):
    if len(arg_list) > 1:
        return "bad usage!"
    sp.next_track()
    return None

# skip to previous track
def previous(sp, arg_list):
    if len(arg_list) > 1:
        return "bad usage!"
    sp.previous_track()
    return None

# get track currently playing
def current(sp, arg_list):
    if len(arg_list) > 1:
        return "bad usage!"
    else:
        cur = sp.currently_playing()['item']
        artists = [i['name'] for i in cur['artists']]
        if cur:
            return '\'' + cur['name'] + '\' by ' + ", ".join(artists)
        else:
            return None

# reshuffles current playback, or turns off shuffle with 'off' option
def shuffle(sp, arg_list):
    if len(arg_list) > 1:
        if arg_list[1]=='off':
            sp.shuffle(state=False)
        else:
            return "bad usage!"
    else:
        sp.shuffle(state=True)
    return None

''' start or resume a user's playback
    options
        (none) -> resume playback
        shuffle -> shuffle through all songs
        track [name] (might ask to confirm artist)
        playlist [name]
        radio [name]
        album [name] (might ask to confirm artist)
'''
def play(sp, arg_list):
    if len(arg_list) > 1:
        print("in progress!")

        '''play_options = { 'shuffle':,
                         'track':,
                         'playlist':,
                         'radio':,
                         'album':}'''
    else:
        sp.start_playback()
    return None

''' list items
    options
        (none) -> lists options to list
        songs -> all saved songs
        playlists -> all playlists
        songs in [album, playlist, radio, saved]
'''
def list_(sp, arg_list):
    if len(arg_list)==1:
        print("Options: songs / playlists / songs in [album, playlist, radio, saved]")
    else:
        if(arg_list[1]=='songs'):
            # songs in [album, playlist, radio, saved]
            if len(arg_list) > 2:
                print('in progress')
            # all songs
            else:
                print('in progress')
        elif(arg_list[1]=='playlists'):
            #all playlists
            return '\n'.join([i['name'] for i in sp.current_user_playlists()['items']])
        else:
            return 'bad usage, options are songs or playlists'
    '''
    if arg_list:
    else:
        print("Options: songs, playlists, songs in [album, playlist, radio, saved]")
    '''
    return None

'''
    add item to location
    options
        (none) usage instructions
        [album, playlist, song] to playlist
        [album, playlist, song] to queue
        
'''
def add(sp, arg_list):
    if len(arg_list) > 1:
        print('placeholder')
    else:
        print('Usage:\nspotifycli add [this / song name / playlist name / album name] to [playlist name / queue]')
    return None

def help_(sp, arg_list):
    return None

def search(sp, query):
    return None
