import openai
import configparser

openai.api_key = configparser.api_key

openai.ChatCompletion.create(model="GPT-3.5-turbo",
                            menssages=[{"role": "user", "content": "¿Cual es la mision de OpenAI?"}])