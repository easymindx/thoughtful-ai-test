from vector_store import VectorStore
from blogs import BLOGS

from langchain_core.documents import Document

from langchain.text_splitter import RecursiveCharacterTextSplitter

from generator import Generator

class ThoughtfulAIAgent:
    def __init__(self):
        self.vector_store = VectorStore()
        self.generator = Generator(self.vector_store)
        self._ingest_blogs(BLOGS)


    def _ingest_blogs(self, blogs):
        spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        
        for blog in blogs:
            chunks = spliter.split_text(blog["content"])
            self.vector_store.add_documents([
                Document(
                    page_content=chunk,
                    metadata={},
                )
                for chunk in chunks
            ])
        
    def generate_response(self, user_input: str) -> str:
        return self.generator.generate_answer(user_input)


def run_terminal_chat():
    agent = ThoughtfulAIAgent()
    
    print("="*60)
    print("Welcome to Thoughtful AI Support Agent (Terminal Version)")
    print("Ask me questions about Thoughtful AI's agents like EVA, CAM, and PHIL.")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    print("="*60)
    
    print("\nThoughtful AI: Hello! I'm the Thoughtful AI support agent. How can I help you today?")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nThoughtful AI: Thank you for using Thoughtful AI Support. Goodbye!")
            break
        
        response = agent.generate_response(user_input)
        print(f"\nThoughtful AI: {response}")

if __name__ == "__main__":
    run_terminal_chat() 