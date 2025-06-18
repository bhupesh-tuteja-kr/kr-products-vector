from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings
#from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import telegram

# Load and process the text
#loader = CSVLoader('products_export_xs.csv')
#documents = loader.load()

EMBEDDING_MODEL_NAME = "hkunlp/instructor-large"
device_type = "cpu"
#embeddings = HuggingFaceInstructEmbeddings(
#    model_name=EMBEDDING_MODEL_NAME,
#    model_kwargs={"device": device_type},
#)

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk

from chromadb.config import Settings
PERSIST_DIRECTORY = 'db'
CHROMA_SETTINGS = Settings(
    anonymized_telemetry=False,
    is_persistent=True,
)

import pandas as pd
CHUNK_SIZE = 10
for chunk in pd.read_csv('products_export_xs.csv', chunksize=CHUNK_SIZE):
    chunk_as_list = chunk.to_string().split('\n')[1:]
    chunk_size = len(chunk_as_list)
    print(chunk_size)
    documents = telegram.text_to_docs(chunk_as_list)
    if chunk_size > CHUNK_SIZE:
        print(documents)

#    vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=PERSIST_DIRECTORY, client_settings=CHROMA_SETTINGS)
#    vectordb = None

