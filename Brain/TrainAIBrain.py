#api key
fileOpen = open("Data\\Api.txt","r")
API = fileOpen.read()
fileOpen.close()

#importing
import openai
from dotenv import load_dotenv

#coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    Filelog = open("Database\\chat_log.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nMaya : '
    response = completion.create(  #GET FROM ai
        model = "text-davinci-002",  #calling model
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip() #get response from model
    #chat_log_template_update = chat_log_template + f"\nYou : {question} \nMaya : {answer}"
    #Filelog = open("Database\\chat_log.txt","w")   #chatlogupdate
    #Filelog.write(chat_log_template_update)
    #Filelog.close()
    return answer

#reply = ReplyBrain("How old are you?")
#print(reply)

#print(ReplyBrain("Who is your master?")) #Train maya

#while True:
    #kk = input("Enter: ")
    #print(ReplyBrain(kk))

