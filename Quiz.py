import random

# Dictionary of states and their capitals
states_and_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Gujarat': 'Gandhinagar',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Jharkhand': 'Ranchi',
    'Karnataka': 'Bengaluru',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Maharashtra': 'Mumbai',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Odisha': 'Bhubaneswar',
    'Punjab': 'Chandigarh',
    'Rajasthan': 'Jaipur',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'West Bengal': 'Kolkata'
}

# Shuffle the states for the quiz
states = list(states_and_capitals.keys())
random.shuffle(states)

# Function to conduct the quiz
def conduct_quiz():
    score = 0
    for state in states:
        print(f"Identify the capital of {state}: ")
        answer = input("Your answer: ")
        if answer.strip().lower() == states_and_capitals[state].strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {states_and_capitals[state]}.\n")

    print(f"Quiz finished! Your total score is {score}/{len(states)}")

# Start the quiz
conduct_quiz()
