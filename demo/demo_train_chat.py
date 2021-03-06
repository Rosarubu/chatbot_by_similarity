from chatbot import chatbot
import pickle
from chatbot import load_data

texts = load_data(type='chat')

chatbot_try = chatbot()
chatbot_try.train(texts=texts[:], mode='chat')
with open('./model_chat.pkl', mode='wb') as f:
    pickle.dump(chatbot_try, f)
