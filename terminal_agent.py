#!/usr/bin/env python3
from typing import Optional

class ThoughtfulAIAgent:
    def __init__(self):
        # Load predefined responses
        self.knowledge_base = {
            "questions": [
                {
                    "question": "What does the eligibility verification agent (EVA) do?",
                    "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
                },
                {
                    "question": "What does the claims processing agent (CAM) do?",
                    "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
                },
                {
                    "question": "How does the payment posting agent (PHIL) work?",
                    "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
                },
                {
                    "question": "Tell me about Thoughtful AI's Agents.",
                    "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
                },
                {
                    "question": "What are the benefits of using Thoughtful AI's agents?",
                    "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
                }
            ]
        }

    def find_best_match(self, user_question: str) -> Optional[str]:
        """
        Find the best matching answer for the user's question.
        """
        user_question = user_question.lower().strip()
        
        # Simple matching algorithm
        best_match = None
        highest_score = 0
        
        for qa_pair in self.knowledge_base["questions"]:
            # Simple word overlap score
            question = qa_pair["question"].lower()
            words_in_user_q = set(user_question.split())
            words_in_stored_q = set(question.split())
            
            # Calculate word overlap
            common_words = words_in_user_q.intersection(words_in_stored_q)
            if not common_words:
                continue
                
            # Simple scoring based on word overlap percentage
            score = len(common_words) / len(words_in_stored_q)
            
            if score > highest_score:
                highest_score = score
                best_match = qa_pair["answer"]
        
        # Return the best match if the score is above a threshold
        if highest_score > 0.3:
            return best_match
        return None

    def generate_response(self, user_input: str) -> str:
        """Generate a response based on the user input"""
        if not user_input.strip():
            return "Please ask a question about Thoughtful AI's agents."
        
        # Try to find a matching predefined answer
        matching_answer = self.find_best_match(user_input)
        
        if matching_answer:
            return matching_answer
        else:
            # Generic fallback response for questions we don't have predefined answers for
            return "I don't have specific information about that. I can help with questions about Thoughtful AI's agents like EVA, CAM, and PHIL. Would you like to know more about these agents?"

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