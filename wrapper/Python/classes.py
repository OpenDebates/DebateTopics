import typing
import aiohttp
import asyncio

class BaseRequest:
  def __init__(
    self,
    url: str,
    json: dict
  ) -> None:
    self.request=url
    self.json=json
    
  def exec(self) -> bool:
    async with aiohttp.ClientSession() as session:
      async with session.post(self.request, json=self.json) as response:
        return Response(data)

class AddTopicRequest(BaseRequest):
  def __init__(
    self,
    topic: str,
    category: str="misc",
    token: str
  ) -> None:
    self.request="https://www.debatebot.de/add_topic"
    self.json = {
      "topic": topic,
      "category": category,
      "token": token
    }
    super().__init__(
      "https://www.debatebot.de/add_topic",
      {
        "topic": topic,
        "category": category,
        "token": token
      }
    )
    
class TopicRequest(BaseRequest):
  def __init__(
    self,
    categories: typing.Union(typing.List(str), str)=None,
    amount: int=1,
    authorization_token: str
  ) -> None:
    if categories == None:
      self.request = "https://www.debatebot.de/get_topic"
      self.json = {
        "token": token,
        "amount": amount
      }
      super().__init__(
        "https://www.debatebot.de/get_topic",
        {
          "token": token,
          "amount": amount
        }
      )
    if isinstance(categories, str):
      self.request = "https://www.debatebot.de/get_topic/category"
      self.json = {
        "category": categories,
        "token": token,
        "amount": amount
      }
      super().__init(
        "https://www.debatebot.de/get_topic/category",
        {
          "category": categories,
          "token": token,
          "amount": amount
        }
      )
    elif isinstance(category, typing.List(str)):
      self.request="https://www.debatebot.de/get_topic/categories"
      self.json = {
        "categories": categories,
        "token": token,
        "amount": amount
      }
      super().__init(
        "https://www.debatebot.de/get_topic/categories",
        {
          "categories": categories,
          "token": token,
          "amount": amount
        }
      )
      
class Response:
  def __init__(
    self,
    data
  ) -> None:
    self.data=data
