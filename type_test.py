"""
This program measures the typing speed of a user using the time module.
"""

import time
import random

# tests = [
#     ["As I sit in my room late at night, staring at the computer screen, I decide it would be a good idea to create this text. There isn't much meaning to it, other than to get some simple practice. A lot of the texts that have been created are rather short, and don't give a good representation of actual typing speed and accuracy. They lack the length to gauge where your strengths and weaknesses are when typing."],
#     ["It was always the Monday mornings. It never seemed to happen on Tuesday morning, Wednesday morning, or any other morning during the week. But it happened every Monday morning like clockwork. He mentally prepared himself to once again deal with what was about to happen, but this time he also placed a knife in his pocket just in case."],
#     ["She patiently waited for his number to be called. She had no desire to be there, but her mom had insisted that she go. She's resisted at first, but over time she realized it was simply easier to appease her and go. Mom tended to be that way. She would keep insisting until you wore down and did what she wanted. So, here she sat, patiently waiting for her number to be called."]
# ]

tests = [
    ['As', 'I', 'sit', 'in', 'my', 'room', 'late', 'at', 'night,', 'staring', 'at', 'the', 'computer', 'screen,', 'I', 'decide', 'it', 'would', 'be', 'a', 'good', 'idea', 'to', 'create', 'this', 'text.', 'There', "isn't", 'much', 'meaning', 
'to', 'it,', 'other', 'than', 'to', 'get', 'some', 'simple', 'practice.', 'A', 'lot', 'of', 'the', 'texts', 'that', 'have', 'been', 'created', 'are', 'rather', 'short,', 'and', "don't", 'give', 'a', 'good', 'representation', 'of', 'actual', 'typing', 'speed', 'and', 'accuracy.', 'They', 'lack', 'the', 'length', 'to', 'gauge', 'where', 'your', 'strengths', 'and', 'weaknesses', 'are', 'when', 'typing.'],
    
    ['It', 'was', 'always', 'the', 'Monday', 'mornings.', 'It', 'never', 'seemed', 'to', 'happen', 'on', 'Tuesday', 'morning,', 'Wednesday', 'morning,', 'or', 'any', 'other', 'morning', 'during', 'the', 'week.', 'But', 'it', 'happened', 'every', 'Monday', 'morning', 'like', 'clockwork.', 'He', 'mentally', 'prepared', 'himself', 'to', 'once', 'again', 'deal', 'with', 'what', 'was', 'about', 'to', 'happen,', 'but', 'this', 'time', 'he', 'also', 'placed', 'a', 'knife', 'in', 'his', 'pocket', 'just', 'in', 'case.'],
    
    ['She', 'patiently', 'waited', 'for', 'his', 'number', 'to', 'be', 'called.', 'She', 'had', 'no', 'desire', 'to', 'be', 'there,', 'but', 'her', 'mom', 'had', 'insisted', 'that', 'she', 'go.', "She's", 'resisted', 'at', 'first,', 'but', 'over', 'time', 'she', 'realized', 'it', 'was', 'simply', 'easier', 'to', 'appease', 'her', 'and', 'go.', 'Mom', 'tended', 'to', 'be', 'that', 'way.', 'She', 'would', 'keep', 'insisting', 'until', 'you', 'wore', 'down', 'and', 'did', 'what', 'she', 'wanted.', 'So,', 'here', 'she', 'sat,', 'patiently', 'waiting', 'for', 'her', 'number', 'to', 'be', 'called.']
]

# I used this code to turn the tests into lists of words.

def convert(lst):
    return ' '.join(lst).split()

# print("Test 0:", convert(tests[0]))
# print("Test 1:", convert(tests[1]))
# print("Test 2:", convert(tests[2]))

def convert_str(str):
    li = list(str.split(" "))
    return li

test = tests[random.randint(0, 2)]

print("\nWelcome to the typing test! The prompt for you to type is below. Good luck!")
print()
# Display the test the user needs to type.
for word in test:
    print(word, end=' ')


print("\n")
# Wait until the user presses enter to know they're ready to start the test.
input("Press enter when you're ready to begin typing... and press enter when you're finished typing.\n")
print("Type!!!")

# Start the timer.
start = time.time()

user_test_list = input()

# Stop the timer.
stop = time.time()

user_test_string = "".join(user_test_list)

perfect = len(test)
total = len(test)
errors = 0

user_test = convert_str(user_test_list)

for i in range(len(test)):
    try:
        if test[i] != user_test[i]:
            perfect -= 1
            errors += 1
    except:
        perfect -= 1

elapsed = stop - start
elapsed_minutes = (stop - start) // 60
seconds_left = elapsed % 60

if elapsed >= 60:
    print(f"\n\nTime: {elapsed_minutes:.0f} minutes and {seconds_left:.0f} seconds")
else:
    print(f"\n\nTime: {elapsed:.0f} second(s)")

accuracy = perfect / total * 100

net_wpm = ((len(user_test_string) / 5) - errors) / elapsed_minutes


print(f"\nYour corrected speed was {net_wpm:.2f} WPM with an accuracy of {accuracy:.2f}%\n")