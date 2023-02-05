from Listen import Listen
from Speak import Speak


FileOpenAi = open('DataBase\\ApiKeys\\openai.txt','r')
apikey = FileOpenAi.read()
FileOpenAi.close()

from dotenv import load_dotenv
import openai

openai.api_key = "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"

load_dotenv()
completion = openai.Completion()

chat_log_template = '''You : Hello i was developed by B75 TEAM, who are you?
Maya : Iam Maya. How can I help you today?
'''

def Reply(question, chat_log=None):
    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You : {question}\nMaya :'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nYou'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

while True:
    Query = Listen()
    reply = Reply(Query)
    Speak(reply)
