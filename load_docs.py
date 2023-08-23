from langchain.document_loaders import DirectoryLoader

def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents
