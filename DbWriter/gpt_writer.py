import string
import openai
from configparser import ConfigParser


class GptWriterEngine():
    
    def __init__(self, config: ConfigParser):
        self.__api_key = config('GPT', 'ApiKey')

    def summarize(self, text, length=256):
        openai.api_key = self.__api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.__clean_text(text),
            max_tokens=length,
            temperature=0.7,
            top_p=1,
            best_of=1,
            frequency_penalty=0,
            presence_penalty=0)
        return response['choices'][0]['text']