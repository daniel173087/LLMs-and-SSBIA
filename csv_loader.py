from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="sql_statements.csv")
data = loader.load()
print(data)