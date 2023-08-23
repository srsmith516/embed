from find_similar import get_similar_docs

def get_answer(index,chain,query):
    similar_docs = get_similar_docs(index,query)
    answer = chain.run(input_documents=similar_docs, question=query)
    return answer
