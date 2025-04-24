from vector_store import VectorStore
from langchain_openai import ChatOpenAI


# Instantiate the OpenAI chat model
chat_model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

class Generator:
  
  def __init__(self, vector_store: VectorStore):
    self.vector_store = vector_store


  def generate_answer(self, user_question: str) -> str:
    # Retrieve relevant documents from the vector store
    relevant_docs = self.vector_store.similarity_search(user_question, k=3)
    
    
    # Enhance the question with retrieved documents
    prompt = f"""
    You are a helpful assistant. You are given a question and some relevant documents.
    Don't guess anything that is not in the documents. If you don't know the answer, try to use your knowledge to answer the question.
    Question: {user_question}
    
    Relevant documents:
    {relevant_docs}
    
    
    """
    
    # Generate the answer using the enhanced question
    answer = chat_model.invoke(
        [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Return the generated answer
    
    return answer.content
