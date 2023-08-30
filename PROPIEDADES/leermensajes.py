from telethon import TelegramClient
import configparser
import pandas as pd
import openai

config = configparser.ConfigParser()
config.read("configuracion.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_key = config['ChatGPT']['api_key']
client = TelegramClient('Emiliano', api_id, api_hash)

openai.api_key = api_key

messages=[{"role": "user", "content": "¿Cual es la mision de OpenAI?"}]
def mi_filtro(events):
    return events.message.text.startswith('https')

async def main():
    await client.start()
    entity = await client.get_entity("@OctavioTato")
    #print(entity)
    menssages = await client.get_messages("@OctavioTato")
    #print(menssages)
    #await client.send_message('@OctavioTato',"Como te encuentras este dia de hoy viernes 16 de junio")
    chat_id = "@OctavioTato"
    informacion = []
    mi_lista= []
    async for message in client.iter_messages(chat_id):
        if message.text:
            texto = message.text
            informacion.append(texto)
        if message.text.startswith('https'):
            #print(message.text)
            mi_lista.append(message.text)
            #print(mi_lista)
    #print(informacion)
    df = pd.DataFrame({'Informacion': informacion})
    excel_file = "Propiedades.xlsx"
    df.to_excel(excel_file, index=False)
    answered = True
    while answered:
        messagesChat = []
        for informacion in informacion:
            if 'https' not in informacion:
                pregunta = "Dame el codigo postal de esta dirreccion, si no la tines responde con no:" + informacion
                messagesChat.append({"role": "user", "content": pregunta})
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-16k-0613", messages=messagesChat)
                reply = chat.choices[0].message.content
                print(f"Respuesta de ChatGPT: {reply}")
        answered = False

#async def eliminar_mensaje():
    #chat_id = "@OctavioTato"
    #async for message in client.iter_messages(chat_id, search='Esto lo hago desde Pythooon'):
        #print(message)
        #await client.delete_messages(chat_id, message)

client.loop.run_until_complete(main())
#client.loop.run_until_complete(eliminar_mensaje())

