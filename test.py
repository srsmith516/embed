import os
import openai
import pinecone
from langchain.vectorstores import Pinecone
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from load_docs import load_docs
from split_docs import split_docs
#from find_similar import get_similar_docs
from qa import get_answer

#Load documents
directory = 'content/data'
documents = load_docs(directory)
print(len(documents))

#split docs
docs = split_docs(documents) 
print(len(docs))

#embeddings
embeddings = OpenAIEmbeddings(model_name="ada")
query_result = embeddings.embed_query("Bill Text")
print(len(query_result))

#pinecone initialize
pinecone.init(
        api_key="a8fdb788-f374-411f-9654-1d50da13d8ac",
        environment="us-west1-gcp-free"
        )
index_name = "embed2"
index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

#QA
model_name = "gpt-3.5-turbo"
llm = OpenAI(model_name=model_name)
chain = load_qa_chain(llm, chain_type="stuff")

query = "What does section 1 of SB-10 say?"
answer = get_answer(index,chain,query)
print(answer)

query = "What is SB-10?"
answer = get_answer(index,chain,query)
print(answer)

