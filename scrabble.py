#scrabble.py
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# combine letters and points list. Note that the keys and values for letters_to_points used is also named 'letters' and 'points'
letters_to_points = {letters:points for letters, points in zip(letters, points)}

# add " " with 0 points
letters_to_points[" "] = 0
print(letters_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter,0)
  return point_total

#test - score should be 15
brownie_points = score_word("BROWNIE")

# indicate the words the players used
player_to_words = {"player1":["BLUE","TENNIS","EXIT"], "wordNerd":["EARTH","EYES","MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

#iterate through the words used by players to compute the points
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points = score_word(word)
  #assign the player into the respective points
  player_to_points[player] = player_points

print(player_to_points)