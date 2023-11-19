import chromadb
from chromadb.utils import embedding_functions


def get_collection():
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                    api_key="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",
                    model_name="text-embedding-ada-002"
                )
        #chroma_client = chromadb.Client()
    chroma_client = chromadb.PersistentClient(path="/Users/D-Win/OneDrive/Uni/Semester 5/BA/prototyp/modules")

    collection = chroma_client.get_or_create_collection(
        name="example_distance",
        metadata={"hnsw:space": "cosine"},
        embedding_function=openai_ef
        )
    return collection
    
collection = get_collection()


collection.add(
    documents=["Once upon a time in a faraway land, there lived a brave knight who embarked on a quest to find a legendary dragon. He journeyed through enchanted forests, climbed towering mountains, and crossed vast deserts. Along the way, he encountered various magical creatures and faced numerous challenges. His courage and determination were unyielding as he pursued his noble mission.", "The latest advancements in quantum computing have revolutionized data processing capabilities. Quantum computers leverage the principles of quantum mechanics to perform operations on data at unprecedented speeds. This technological breakthrough holds immense potential for solving complex problems in fields like cryptography, materials science, and artificial intelligence. Researchers are continuously exploring the scalability and practical applications of these quantum systems."],
    ids=["id1", "id2"],
)


#query the collection and print the results 
results = collection.query(
    
    query_texts=["The latest advancements in quantum computing have revolutionized data processing capabilities. Quantum computers leverage the principles of quantum mechanics to perform operations on data at unprecedented speeds. This technological breakthrough holds immense potential for solving complex problems in fields like cryptography, materials science, and artificial intelligence. Researchers are continuously exploring the scalability and practical applications of these quantum systems."],
    #query_embeddings=[],
    n_results=2
    #,    include= ["distances"]
)

print(results)