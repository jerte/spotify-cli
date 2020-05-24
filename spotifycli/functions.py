import sys
import spotipy
import spotipy.util as util
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
        return sp.currently_playing()

# reshuffles current playback
def shuffle(sp, arg_list):
    if len(arg_list) > 1:
        return "bad usage!"
    else:
        sp.shuffle(state=False)
        sp.shuffle(state=True)
        sp.next_track()
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

        play_options = { 'shuffle':,
                         'track':,
                         'playlist':,
                         'radio':,
                         'album':}
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
def list(sp, arg_list):
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
