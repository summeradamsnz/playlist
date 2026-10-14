'''This program alows the user to create a playlist from a pre made collection of songs.'''
def menu():
    '''display options for user'''

    print("1. View all songs")
    print("2. Add new song to collection")
    print("3. Remove song from collection")
    print("4. Create Playlist")
    print("5. Quit")

def display_collection():
    '''Display all the songs in the collection in a fomatted list'''
    print(f"{'ID':4} {'Song Title':30} {'Artist':30} {'Song Length':5} ")
    print("="*79)
    for i in range (len(song_collection)):
        print(f"{i+1 } {song_collection[i][0]:30} {song_collection[i][1]:36} {song_collection[i][2]:5}")










song_collection = [
    ["Shake it off", "Taylor Swift", 3.39],
    ["Bones", "Imagine Dragons", 2.45],
    ["September", "Earth, Wind & Fire", 3.35],
    ["Everybody talks", "Neon trees", 2.57],
    ["Timber", "Pitbull, Kesha", 3.20],
    ["Tik Tok", "Kesha", 3.20],
    ["Stereo Hearts", "Gym Class Heroes, Adam Levine", 3.31],
    ["Ridin'Solo", "Jason Derulo", 3.36],
    ["Airplanes", "B.o.B, Hayley Williams", 3.00],
    ["Since U Been Gone", "Kelly Clarkson", 3.09],
    ["Part Of Me", "katy Perry", 3.36],
    ["Royals", "Lorde", 3.10],
    ["Drive By", "Train", 3.16],
    ["Riptide", "Vance Joy", 3.24],
    ["Counting Stars", "OneRepublic", 4.17],
    ["Rude", "MAGIC!", 3.45],
    ["stitches", "Shawn Mendes", 3.27],
    ["Am I Wrong", "Nico & Vinz", 4.06],
    ["Pompeii", "Bastille", 3.34],
    ["Shut Up and Dance", "WALK THE MOON", 3.19],
    ["She Looks So Perfect", "5 Seconds of Summer", 3.22],
    ["What Makes You Beautiful", "One Direction", 3.20],
    ["There's Nothing Holdin'Me Back", "Shawn Mendes", 3.19],
    ["Classic", "MKTO", 2.55],
    ["Magic", "B.o.B, Rivers Cuomo", 3.16],
    ["Last Friday Night", "Katy Perry", 3.51],
    ["Starships", "Nicki Minaj", 3.31],
    ["Shake it", "Metro Station", 3.00],
    ["Good As Hell", "Lizzo", 2.39],
    ["Ophelia", "The Lumineers", 2.40],
    ["One Less Lonely Girl", "Justin Bieber", 3.49],
    ["Complicated", "Avril Lavigne", 4.05],
    ["Pon De Replay", "Rhianna", 4.07],
    ["Say My Name", "Destiny's Child", 4.31],
    ["Crazy In Love", "Beyonce, JAY-Z", 3.56],
    ["I Kissed A Girl", "Katy Perry", 3.00],
    ["Poker Face", "Lady Gaga", 3.57],
    ["Toxic", "Britney Spears", 3.19],
    ["I Gotta Feeling", "Black Eyed Peas", 4.49],
    ["Unwritten", "Natasha Badingfield", 4.19],
    ["A Thousand Miles", "Vanessa Carlton", 3.57],
    ["So What", "P!nk", 3.35],
    ["Firework", "Katy Perry", 3.48],
    ["Dynamite", "Taio Cruz", 3.24],
    ["Pocket of Sunshine", "Natasha Bedingfield", 3.23],
    ["Life is a Highway", "Rascal Flatts", 4.36],
    ["Party In The U.S.A", "Miley Cyrus", 3.22],
    ["Before He Cheats", "Carrie Underwood", 3.20],
    ["Mr.Brightside", "The Killers", 3.42],
    ["Baby", "Justin Bieber", 3.34]

]
display_collection()
