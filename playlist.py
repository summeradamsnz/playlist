'''This program alows the user to create a playlist from a pre made collection of songs.'''
def menu():
    '''display options for user'''

    print("\n1. View all songs")
    print("2. Add new song to collection")
    print("3. Remove song from collection")
    print("4. Create Playlist")
    print("5. Quit")

def display_collection():
    '''Display all the songs in the collection in a formatted list'''

    print(f"\n{'ID':4} {'Song Title':40} {'Artist':30} {'Song Length':5} ")
    print("="*83)
    for i in range (len(song_collection)):
        min=song_collection[i][2]//60
        sec=song_collection[i][2]%60/100
        num=min+sec
        print(f"{i+1}.     {song_collection[i][0]:40} {song_collection[i][1]:36} {num}")

def add_song():
    '''add new song to collection '''
    ask_song=True
    while ask_song == True:

        print("\nADD NEW SONG")
        title = check("Song Title: ", "string")
        artist = check("Song Artist: ", "string")
        length = check("Song Length(in mins): ", "float")
        convert_min=length//1*60
        convert_sec=length%1*100
        new_length=convert_min+convert_sec
        if ([title, artist, new_length]) in song_collection:
            print("THIS SONG IS ALREADY IN THE COLLECTION")
        else:
            ask_song=False
            song_collection.append([title, artist, new_length])

def remove_song():
    '''remove a song from the collection'''
    print("\nREMOVE A SONG")
    choice= check("Song ID: ", "integer", len(song_collection))
    del_song = choice-1
    del song_collection[del_song]

def create_playlist():
    '''create a playlist'''

    print("A playlist must have at least 10 songs")
    print("Enter the ID of the song you want to add to your playlist")
    make_playlist=True
    while make_playlist==True:

        pick=check("ID: ", "integer", len(song_collection)+1)
        info=pick-1
        playlist.append(song_collection[info])
        length=0
        for i in range (len(playlist)):
            length=length+(playlist[i][2])
        min=length//60
        sec=length%60/100
        num=min+sec
        print(f"PLAYLIST LENGTH: {num} mins")
        if length==30:
            print("playlist is long enough \n1.add more songs \n2.finish")
            continue_option=check("ID: ", "integer", 2)
            if continue_option==2:
                make_playlist=False
    name=check("Enter a name for the playlist: ", "string")
    print(f"\nPLAYLIST FOR: {name.upper()}")

def display_playlist():
    '''Display all the songs in the playlist in a fomatted list'''

    print(f"\n{'ID':4} {'Song Title':40} {'Artist':30} {'Song Length':5} ")
    print("="*90)
    for i in range (len(playlist)):
        min=playlist[i][2]//60
        sec=playlist[i][2]%60/100
        num=min+sec
        print(f"{i+1 }    {playlist[i][0]:40} {playlist[i][1]:36} {num}")

def check(question, t, m=1000):
    '''error checking for any inputs'''

    ask=True
    while ask ==True:
        i=input(question)
        if t=="float":
            try:
                i=float(i)
                if i<1 or i>m:
                    print("!!ENTER VALID NUMBER!!")
                else:
                    ask=False
                    return i
            except ValueError:
                print("!!enter a number")
        elif t == "integer":
            try:
                i=int(i)
                if i<1 or i>m:
                    print("!!ENTER VALID NUMBER!!")
                else:
                    ask=False
                    return i
            except ValueError:
                print("!!enter a number")
        elif t =="string":
            if i.strip()== "":
                print("enter something")
            else:
                ask=False
                return i

song_collection = [
    ["Shake it off", "Taylor Swift", 219],
    ["Bones", "Imagine Dragons", 165],
    ["September", "Earth, Wind & Fire", 215],
    ["Everybody talks", "Neon trees", 177],
    ["Timber", "Pitbull, Kesha", 184],
    ["Tik Tok", "Kesha", 200],
    ["Stereo Hearts", "Gym Class Heroes, Adam Levine", 210],
    ["Ridin'Solo", "Jason Derulo", 216],
    ["Airplanes", "B.o.B, Hayley Williams", 180],
    ["Since U Been Gone", "Kelly Clarkson", 189],
    ["Part Of Me", "katy Perry", 216],
    ["Royals", "Lorde", 190],
    ["Drive By", "Train", 196],
    ["Riptide", "Vance Joy", 104],
    ["Counting Stars", "OneRepublic", 257],
    ["Rude", "MAGIC!", 225],
    ["stitches", "Shawn Mendes", 207],
    ["Am I Wrong", "Nico & Vinz", 246],
    ["Pompeii", "Bastille", 574],
    ["Shut Up and Dance", "WALK THE MOON", 199],
    ["She Looks So Perfect", "5 Seconds of Summer", 202],
    ["What Makes You Beautiful", "One Direction", 200],
    ["There's Nothing Holdin'Me Back", "Shawn Mendes", 199],
    ["Classic", "MKTO", 175],
    ["Magic", "B.o.B, Rivers Cuomo", 196],
    ["Last Friday Night", "Katy Perry", 231],
    ["Starships", "Nicki Minaj", 211],
    ["Shake it", "Metro Station", 180],
    ["Good As Hell", "Lizzo", 159],
    ["Ophelia", "The Lumineers", 160],
    ["One Less Lonely Girl", "Justin Bieber", 229],
    ["Complicated", "Avril Lavigne", 245],
    ["Pon De Replay", "Rhianna", 247],
    ["Say My Name", "Destiny's Child", 271],
    ["Crazy In Love", "Beyonce, JAY-Z", 236],
    ["I Kissed A Girl", "Katy Perry", 180],
    ["Poker Face", "Lady Gaga", 237],
    ["Toxic", "Britney Spears", 199],
    ["I Gotta Feeling", "Black Eyed Peas", 289],
    ["Unwritten", "Natasha Badingfield", 259],
    ["A Thousand Miles", "Vanessa Carlton", 237],
    ["So What", "P!nk", 215],
    ["Firework", "Katy Perry", 228],
    ["Dynamite", "Taio Cruz", 204],
    ["Pocket of Sunshine", "Natasha Bedingfield", 203],
    ["Life is a Highway", "Rascal Flatts", 276],
    ["Party In The U.S.A", "Miley Cyrus", 202],
    ["Before He Cheats", "Carrie Underwood", 200],
    ["Mr.Brightside", "The Killers", 222],
    ["Baby", "Justin Bieber", 214]
]

playlist = [
]
length=0
run=True
while run == True:
    menu()
    option = check("ENTER NUMBER: ", "integer", 5)
    if option == 1:
        display_collection()
    elif option== 2:
        add_song()
    elif option == 3:
        remove_song()
    elif option == 4:
        create_playlist()
        playlist_length()
        display_playlist()
    elif option == 5:
        run=False
print("Goodbye")




