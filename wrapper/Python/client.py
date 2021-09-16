import typing
import asyncio
from Classes import *

class Topic:
  def __init__(
    self,
    content: str
  ) -> None:
    self.content=content
    
  def __repr__(
    self
  ) -> str:
    return self.content
  
  def __str__(
    self
  ) -> str:
    return self.content

class Client:
  def __init__(
    self,
    token: str
  ) -> None:
    self.token=token
    
  def get_topic(
    amount: int=1
  ) -> typing.Union(Topic, typing.List(Topic)):
    req = TopicRequest(
      amount=amount,
      token=self.token
    )
    resp = asyncio.get_event_loop().run_until_complete(req.exec())
    
    if "topics" in resp.json():
      topics = []
      index = 0
      for topic in resp.json()["topics"]:
        topics.append(
          Topic(
            resp.json()["topics"][index]
          )
          index+=1
      return topics
        
    return Topic(
      resp.json()["topic"]
    )
  
  def get_topic_by_category(
    category: str,
    amount: int=1
  ) -> typing.Union(Topic, typing.List(Topic)):
    req = TopicRequest(
      categories=category,
      amount=amount,
      token=self.token
    )
    resp = asyncio.get_event_loop().run_until_complete(req.exec())
    
    if "topics" in resp.json():
      topics = []
      index = 0
      for topic in resp.json()["topics"]:
        topics.append(
          Topic(
            resp.json()["topics"][index]
          )
          index+=1
      return topics
        
    return Topic(
      resp.json()["topic"]
    )
    
  def get_topic_by_categories(
    categories: str,
    amount: int=1
  ) -> typing.Union(Topic, typing.List(Topic)):
    req = TopicRequest(
      categories=categories,
      amount=amount,
      token=self.token
    )
    resp = asyncio.get_event_loop().run_until_complete(req.exec())   
    if "topics" in resp.json():
      topics = []
      index = 0
      for topic in resp.json()["topics"]:
        topics.append(
          Topic(
            resp.json()["topics"][index]
          )
          index+=1
      return topics
        
    return Topic(
      resp.json()["topic"]
    )
          
  async def add_topic(
    topic: str,
    category: str
  ) -> bool:
    req = AddTopicRequest(
      topic=topic,
      category=category,
      token=self.token
    )
    try:
      asyncio.get_event_loop().run_until_complete(req.exec()) 
      return True
    except:
      return False
