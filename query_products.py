import chromadb
client = chromadb.PersistentClient(path="db")
collection = client.get_collection("langchain")
print(collection.count())
#collection.peek()

from langchain.embeddings import HuggingFaceInstructEmbeddings
EMBEDDING_MODEL_NAME = "hkunlp/instructor-large"
device_type = "cpu"
embeddings = HuggingFaceInstructEmbeddings(
    model_name=EMBEDDING_MODEL_NAME,
    model_kwargs={"device": device_type},
)


#QUERY_TEXT = "organic honey"
QUERY_TEXT = input("Enter query text: ")
#NO_OF_RESULTS = 10
NO_OF_RESULTS = int(input("No of results: "))
query_embedding = embeddings.embed_query(QUERY_TEXT)
result = collection.query(
    query_embeddings = [query_embedding],
    n_results = NO_OF_RESULTS
)


for doc in result["documents"][0]:
    print(doc)
    print('\n')

print("Distances:")
for doc in result["distances"][0]:
    print("\t{}".format(doc))



