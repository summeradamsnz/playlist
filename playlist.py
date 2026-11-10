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

    #display the headings
    print(f"\n{'ID':4}  {'Song Title':40} {'Artist':30} {'Song Length':5} ")
    #line to seperate the heading from the data
    print("="*89)
    #print all the data from the song collection
    for i in range (len(song_collection)):
        #convert the song length from seconds to minutes
        min=song_collection[i][2]//60
        sec=song_collection[i][2]%60/100
        num=min+sec
        print(f"{i+1:<4}  {song_collection[i][0]:40} {song_collection[i][1]:36} {num}")

def add_song():
    '''add new song to collection '''

    ask_song=True
    while ask_song == True:

        print("\nADD NEW SONG")
        #ask for the title of the song
        title = check("Song Title: ", "string")
        #ask for the artist of the song
        artist = check("Song Artist: ", "string")
        #ask for the length of the song
        length = check("Song Length(in mins.secs): ", "float", 60)
        #calculate the length from minutes to seconds
        convert_min=length//1*60
        convert_sec=length%1*100
        new_length=convert_min+convert_sec
        #check if song is already in the song_collection
        check_song=True
        for song in song_collection:
            if song[0].lower()==title.lower() and song[1].lower()==artist.lower() and song[2]==new_length:
                check_song=False
        if check_song ==False:
            #informing the user that the song already exists
            print("THIS SONG IS ALREADY IN THE COLLECTION")
        else:
            ask_song=False
            #add song to collection
            song_collection.append([title, artist, new_length])

def remove_song():
    '''remove a song from the collection'''

    print("\nREMOVE A SONG")
    #ask user for the ID of the song they want to delete
    choice= check("Song ID: ", "integer", len(song_collection))
    #delete one of the number to get the correct one from the list (list starts at 0 not 1)
    del_song = choice-1
    #display the song that is being deleted
    print(f"song deleted: {song_collection[del_song][0]}")
    #delete the song
    del song_collection[del_song]

def create_playlist():
    '''create a playlist'''

    #giving the user the conditions for the playlist
    print("A playlist must be at least 30 mins long")
    print("Enter the ID of the song you want to add to your playlist")
    make_playlist=True
    while make_playlist==True:
        #asking for Id of song they want to add to playlist
        pick=check("ID: ", "integer", len(song_collection))
        #delete one of the number to get the correct one from the list (list starts at 0 not 1)
        info=pick-1
        #adding song to playlist
        playlist.append(song_collection[info])
        #setting length of playlist to 0
        length=0
        #adding the length of each song to the length of playlist
        for i in range (len(playlist)):
            length=length+(playlist[i][2])
        #calculating the length from seconds to minutes
        min=length//60
        sec=length%60/100
        num=min+sec
        #displaying how long the playlist is at the moment
        print(f"PLAYLIST LENGTH: {num} mins")
        #checking if the playlist is long enough
        if length>=MIN_LENGTH:
            #giving user the option to add more songs even if the playlist is long enough
            print("playlist is long enough \n1.add more songs \n2.finish")
            #asking for users choice
            continue_option=check(": ", "integer", 2)
            if continue_option==2:
                make_playlist=False
    #getting a name for the playlist
    name=check("Enter a name for the playlist: ", "string")
    #printing the name of the playlist
    print(f"\nPLAYLIST FOR: {name.upper()}")
    #printing the total length of the playlist
    print(f"\nTOTAL PLAYLIST LENGTH: {num}mins")

def display_playlist():
    '''Display all the songs in the playlist in a fomatted list'''

    #display heading for playlist
    print(f"\n{'ID':4}  {'Song Title':40} {'Artist':30} {'Song Length':5} ")
    #displaying line to seperate heading from data
    print("="*90)
    #displaying the data
    for i in range (len(playlist)):
        #converting the length from seconds to minutes
        min=playlist[i][2]//60
        sec=playlist[i][2]%60/100
        num=min+sec
        print(f"{i+1:<4}  {playlist[i][0]:40} {playlist[i][1]:36} {num}")


def check(question, t, m=1000):
    '''error checking for any inputs'''\

    ask=True
    while ask ==True:
        i=input(question)
        #checking the song length (also checks if the seconds does not exceed 60 seconds)
        if t=="float":
            try:
                i=float(i)

                if i<=0 or i%1*100 >=60:
                    print("!!ENTER VALID NUMBER!!")
                else:
                    ask=False
                    return i
            except ValueError:
                print("!!enter a number")
        #checking integers entered and that they are within the correct bounds for the question
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
        #making sure any text entered is not blank
        elif t =="string":
            if i.strip()== "":
                print("enter something")
            else:
                ask=False
                return i
#nested list for the song collection
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
    ["Baby", "Justin Bieber", 214],
    ["Closing Time", "Semisonic", 273]
]
#list for the playlist
playlist = [
]
#setting a minimum length for the playlist(in seconds)
MIN_LENGTH=1800
#run the program
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
        display_playlist()
    elif option == 5:
        run=False
print("Goodbye")




