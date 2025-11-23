"""
Pet Rock Genie Application
Version: 1.0.0
Environment: Test
COM-430-Software Engineering: Group 2
Instructor: Dr Brian Holbert
Authors: carlos.silva02@email.saintleo.edu / joseph.prignano@email.saintleo.edu / cody.bradley02@email.saintleo.edu
Description: A simple yes/no/maybe question answering application
"""

import random
import datetime
import logging

# Configure logging
logging.basicConfig(
    filename='pet_rock_genie.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PetRockGenie:
    """Main application class for Pet Rock Genie"""
    
    def __init__(self):
        """Initialize the Pet Rock Genie with response options"""
        self.responses = {
            'yes': [
                "Yes! ◕ ◡ ◕",
                "The rock says YES!",
                "Definitely yes! permission granted ᕦ(ò_óˇ)ᕤ"
            ],
            'no': [
                "No! ಥ_ಥ",
                "The rock says NO! negative Ghost Rider! (◣_◢)",
                "Absolutely not! (╯°□°）╯"
            ],
            'maybe': [
                "Maybe... ( ͡° ͜ʖ ͡°)",
                "The rock is uncertain... MAYBE! ( ͡๏ ͜x ͡๏)",
                "Ask again later... maybe? ¯\_(ツ)_/¯"
            ]
        }
        self.question_count = 0
        logging.info("Pet Rock Genie initialized")
    
    def get_answer(self, question):
        """
        Generate a random answer to a question
        Args:
            question (str): The user's question
        Returns:
            str: Random yes/no/maybe answer
        """
        answer_type = random.choice(['yes', 'no', 'maybe'])
        answer = random.choice(self.responses[answer_type])
        self.question_count += 1
        
        logging.info(f"Question #{self.question_count}: {question}")
        logging.info(f"Answer: {answer}")
        
        return answer
    
    def run(self):
        """Main application loop"""
        print("(ง'̀-'́)ง Welcome to the Pet Rock Genie! (ง'̀-'́)ง")
        print("Ask me the mighty rock genie (ง'̀-'́)ง any yes/no question, or type 'quit' to exit.\n")
        logging.info("Application started")
        
        while True:
            try:
                question = input("Your question: ").strip()
                
                if question.lower() in ['quit', 'exit', 'bye']:
                    print(f"(ง'̀-'́)ง The rock rests. You asked {self.question_count} questions. Goodbye! (ง'̀-'́)ง")
                    logging.info(f"Application closed. Total questions: {self.question_count}")
                    break
                
                if not question:
                    print("The rock needs a question to ponder! (ง'̀-'́)ง\n")
                    continue
                
                if not question.endswith('?'):
                    print("(Tip: Questions usually end with '?')")
                
                print(f"(ง'̀-'́)ง *the rock vibrates mysteriously* (ง'̀-'́)ง")
                answer = self.get_answer(question)
                print(f"Answer: {answer}\n")
                
            except KeyboardInterrupt:
                print("\n(ง'̀-'́)ง The rock has been interrupted! Goodbye! (ง'̀-'́)ง")
                logging.warning("Application interrupted by user")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                logging.error(f"Error occurred: {str(e)}")

def main():
    """Entry point for the application"""
    genie = PetRockGenie()
    genie.run()

if __name__ == "__main__":
    main()