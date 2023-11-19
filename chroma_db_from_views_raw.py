import chromadb
from chromadb.utils import embedding_functions
import pickle


def get_collection():
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                    api_key="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",
                    model_name="text-embedding-ada-002"
                )
        #chroma_client = chromadb.Client()
    chroma_client = chromadb.PersistentClient(path="/Users/D-Win/OneDrive/Uni/Semester 5/BA/prototyp/modules")
    #chroma_client.delete_collection('report_embedding_automated')

    collection = chroma_client.get_or_create_collection(
        name="report_embedding_automated",
        metadata={"hnsw:space": "cosine"},
        embedding_function=openai_ef
        )
    return collection
    
collection = get_collection()

# Load the list from the file


def fill_vector_database():
    with open('views_raw.pkl', 'rb') as f:
        views_raw = pickle.load(f)
    for index, view in enumerate(views_raw):
        # print(f"Iteration: {index}")  # Prints the current iteration number
        #print(f"View (type: {type(view)}): {view}")
        collection.add(
            documents=[view],
            metadatas=[{"view_content": views_raw[index]}],
            ids=[f"id{index}"]
        )

def query_collection(text):
    #query the collection and print the results 
    results = collection.query(
    
        query_texts=[text],
        #query_embeddings=[],
        n_results=6
        ,    include= ["metadatas"]
    )

    print(results)