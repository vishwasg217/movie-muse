from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import TextLoader
from langchain import PromptTemplate
from dotenv import dotenv_values
import os

config = dotenv_values(".env")
OPEN_AI_API = config["OPEN_AI_API"]
ACTIVELOOP_TOKEN = config["ACTIVELOOP_TOKEN"]

def load_data(path: str) -> list:
    pass