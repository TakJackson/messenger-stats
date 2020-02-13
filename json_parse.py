import matplotlib.pyplot as plot
from collections import Counter
from re import findall
import string
import numpy
import json

users = []
messages = []

class User:
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.message_count = 0
    
    def countMessages(self):
        self.message_count = len(self.messages)

class Message:
    def __init__(self, content, timestamp):
        self.content = content
        self.timestamp = timestamp

def word_count(phrase):
    return Counter(findall(r'\S+', phrase.lower()))

with open("message_1.json", 'r') as json_file:
    data = json.load(json_file)
    for participant in data['participants']:
        users.append(User(participant['name']))

    for message in data['messages']:
        for user in users:
            if (message['sender_name'] == user.name and 'content' in message):
                user.messages.append(Message(message['content'], message['timestamp_ms']))
                messages.append(Message(message['content'], message['timestamp_ms']))

master_string = ""
for message in messages:
    master_string += message.content + " "

word_count_dict = word_count(master_string)

common_words = ["i", "to", "the", "a", "u", "we", "for", "is", "it", "you", "can", "so", "and", "at", "what", "i'm", "go", "in", "not", "do", "me", "just", "be", "on", "that", "if", "my", "but", "are", "have", "get", "of", "up", "this", "there", "then", "like", "well", "or", "it's", "will", "your", "i'll", "was", "as", "that's", "with" ]

for message in users[1].messages:
    print(message.content)

