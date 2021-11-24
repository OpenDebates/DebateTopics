import typing
import secrets
import json
from random import *

# NOTE: Before the API is actually released, tokens will be stored in a secure database, hashed, and salted.

def validate_token(
  args: typing.List(
    typing.Union(
      str,
      int
    )
  ) = []
) -> bool:
  
  with open("tokens.json", "r+") as f:
    tokens = json.load(f)
  
  if len(args) == 0:
    return False
  else if "token" not in args:
    return False
  else if args["token"] not in tokens:
    return False
  
  else:
    return True
  

  
def create_token() -> str:
  with open("tokens.json", "r+") as f:
    tokens=json.load(f)
  
  while True:
    new_token = secrets.urlsafe(randint(32, 40))
    if new_token in tokens:
      continue
    
    else:
      token=new_token
      break
  tokens[token] = "1"
  with open("tokens.json", "w+") as f:
    json.dump(tokens, f)
  return token
