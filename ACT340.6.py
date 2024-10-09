# Problem 1

# Use the following states and capitals to create dictionary objects.

# Los Angeles, California

# Albany, New York

# Honolulu, Hawaii

# Juneau, Alaska

# Austin, Texas

# Create a Dictionary object with the {} bracket notation where the States are the Keys and the Capitals are the values.
# Create a Dictionary object with built-in dict() function where the States are the Keys and the Capitals are the values.
# Use the type() method to check the object type of each object
# Print each object to see all the key:value pairs in the dictionary

states = {'California': 'Los Angeles', 'NewYork': 'Albany', 'Hawaii': 'Honolulu', 'Alaska': 'Juneau', 'Texas': 'Austin'}
print(type(states))
print(states)

# Problem 2

# Use a dictionary object from Problem 1 to complete the following:

# Retrieve the value for the key 'California'
# Add the State: Capital pair for Florida to the dictionary
# Update the capital of California to 'Sacremento'
# Delete Alaska from the Dictionary

# Sample dictionary from Problem 1
state_capitals = {
    'California': 'Sacramento',
    'Alaska': 'Juneau',
    'Texas': 'Austin',
    'New York': 'Albany'
}

# 1. Retrieve the value for the key 'California'
california_capital = state_capitals.get('California')
print(f"Capital of California: {california_capital}")

# 2. Add the State: Capital pair for Florida to the dictionary
state_capitals['Florida'] = 'Tallahassee'

# 3. Update the capital of California to 'Sacramento'
state_capitals['California'] = 'Sacramento'  

# 4. Delete Alaska from the Dictionary
del state_capitals['Alaska']

# Problem 3

# Use the dictionary methods and for loop examples above to complete the following task:

# Create a dictionary object called 'playlist' with a minimum of 6 key:value pairs.
# Each Key in the dictionary should be an artist name
# Each Value should be a corresponding song by that artist
# Use a for loop to create a print statement that prints all the artists in the playlist
# Use a for loop to create a print statment that prints all the songs in the playlist
# Use a for loop to create a print statement that says: "(Song Name) by (Artist) is in the current playlist."
# Remove the last Key:Value pair from the Dictionary
# Add the song "Anti-Hero" by Taylor Swift to your playlist.
# Overwrite one of your songs to have REMIX in front of the song title
# Define & call a function that will print all the artists and songs from the object you pass into it.

# Step 1: Create a dictionary called 'playlist'
playlist = {
    "Ed Sheeran": "Shape of You",
    "Dua Lipa": "Levitating",
    "The Weeknd": "Blinding Lights",
    "Billie Eilish": "Bad Guy",
    "Drake": "God's Plan",
    "Ariana Grande": "Thank U, Next"
}

# Step 2: Print all the artists in the playlist
print("Artists in the playlist:")
for artist in playlist.keys():
    print(artist)

# Step 3: Print all the songs in the playlist
print("\nSongs in the playlist:")
for song in playlist.values():
    print(song)

# Step 4: Print statement for each song and artist
print("\nSongs and their artists in the playlist:")
for artist, song in playlist.items():
    print(f"{song} by {artist} is in the current playlist.")

# Step 5: Remove the last Key:Value pair from the dictionary
last_artist = list(playlist.keys())[-1]
del playlist[last_artist]

# Step 6: Add the song "Anti-Hero" by Taylor Swift
playlist["Taylor Swift"] = "Anti-Hero"

# Step 7: Overwrite one of the songs to have REMIX in front of the song title
playlist["Dua Lipa"] = "REMIX - Levitating"

# Step 8: Define & call a function that prints all the artists and songs
def print_playlist(pl):
    print("\nCurrent Playlist:")
    for artist, song in pl.items():
        print(f"{artist}: {song}")

# Call the function
print_playlist(playlist)


# Print the updated dictionary
print(state_capitals)
