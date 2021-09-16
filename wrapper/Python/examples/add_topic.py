import debate_topics
from debate_topics import Client

client = Client("token here")

topic = prompt("What topic would you like to add?\n")
if client.add_topic(topic):
  print("Successfully added topic")
else:
  print("This topic is already in the API.")
  
#given that the topic is original, the expected output is:

#Successfully added topic
