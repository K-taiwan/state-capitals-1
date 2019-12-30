import random


# an array of state dictionaries
states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
},{
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

# print(states)


#  - Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.

#  - Provide a welcome message to introduce the player to the game.
overview = "This game is simple, we just need to match the right states with the right capital's. Or you can type 'exit' to end the game"
print(overview)
playName = input('Please enter your name: ')
print('Welcome player:', playName)
#  - Initialize new keys in the dictionaries that store the number of times a user gets a capital `correct` and the number of times the answer is `wrong`.
correct = 0
wrong = 0
score = 0
# print(correct)
# print(wrong)

random.shuffle(states)
# print(states)

# print(states[49])
# print('What is the capital of %s'%states[49]['name'])

for i in range(len(states)-1):
    playerAnswer = input('What is the capital of %s: '%states[i]['name'])
    if playerAnswer == 'exit':
        break
    elif playerAnswer.lower() == states[i]['capital'].lower():
        correct += 1
        score += 1
        print('Correct, Your score is %d' %score)
    else:
        score -= 1
        wrong += 1
        print('Incorrect, the capital of %s is %s.' %(states[i]['name'],states[i]['capital']))
        print('Your score is %d'%score)
        print('Total Correct: %d'%correct)
        print('Total Wrong: %d'%wrong)








#  - Through all 50 states, prompt the user to name the capital of the state.
#   - If the answer is correct, display a message saying so, and increment the `correct` key.
#   - If the answer is wrong, display a message saying so, and increment the `wrong` key.
#   - After each prompt, display a message telling the reader how many times the state was answered correctly out of the total number of times answered.

# - Once the user has gone through all 50 states, ask them if they'd like to play again.