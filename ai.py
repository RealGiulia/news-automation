""" File to manage OpenAI requests"""

import openai
from logger import Logger

from openai import OpenAI


class GPT_API:

    def __init__(self):
        self.key =  ""
        self.messages  =[{"role": "system", "content": "You are a very helpful asistant."}]
        self.client = OpenAI(
                    api_key=self.key,
                    organization='org-DfKXf25pohoOqmtBzc6HPi5G'
                    )
        self.logger = Logger()

    
    def get_chat_opinion(self, msg:str):
        try:
            self.messages.append(msg)
            response = self.client.chat.completions.create(messages=self.messages, model="gpt-3.5-turbo", temperature=1,max_tokens=200)
            answer = response.choices[0]["message"]["content"]
            return answer
        except Exception as error:
            self.logger.register_exception("Could not make question to CHAT gpt. Error %s occured."% error)
