import os
import getpass
import pinecone

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader

from langchain.document_loaders.csv_loader import CSVLoader

os.environ["5e4a93a9-5fa1-4d85-be0e-af17b1ef9842"] = getpass.getpass("Pinecone API Key:")
os.environ["gcp-starter"] = getpass.getpass("Pinecone Environment:")

os.environ["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"] = getpass.getpass("OpenAI API Key:")

loader = TextLoader("../../modules/state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

csv = CSVLoader(file_path="modules/sql_statements.csv")
csv_data = csv.load()

print(csv_data)

embeddings = OpenAIEmbeddings()

# initialize pinecone
pinecone.init(
    api_key=os.getenv("5e4a93a9-5fa1-4d85-be0e-af17b1ef9842"),
    environment=os.getenv("gcp-starter"),
)

index_name = "report-similarity"

# First, check if our index already exists. If it doesn't, we create it
if index_name not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
      name=index_name,
      metric='cosine',
      dimension=1536  
)
# The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# if you already have an index, you can load it like this
# docsearch = Pinecone.from_existing_index(index_name, embeddings)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query)