from Listen import Listen
from Speak import Speak

from dotenv import load_dotenv
import openai

openai.api_key = "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"

load_dotenv()
completion = openai.Completion()

chat_log_template = '''You : Hello i was developed by B75 TEAM, who are you?
Maya : Iam Maya. How can I help you today?
'''

def QuestionAnswer(question, chat_log=None):
    FileOpenAi = open('DataBase\\ApiKeys\\openai.txt','r')
    chat_log_template = FileOpenAi.read()
    FileOpenAi.close()

    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You : {question}\nMaya :'
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,temperature=0,
        top_p=1, frequency_penalty=0, presence_penalty=0,
        max_tokens=100)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nQuestion: {question} \nMaya : {answer}"
    filelog = open("Database")
    return answer

while True:
    Query = Listen()
    reply = Reply(Query)
    Speak(reply)
