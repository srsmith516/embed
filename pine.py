pinecoe.init(
        api_key="pinecone api key",
        environment="env"
        )
index_name = "langchain-demo"
index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
