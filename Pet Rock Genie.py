"""
Pet Rock Genie Application
Version: 2.1.0-Final Version
Environment: Final Version
COM-430-Software Engineering: Group 2
Instructor: Dr. Brian Holbert
Authors: Cody Bradley / Carlos Silva / Joseph Prignano
Description:
    This is the final version of the Pet Rock Genie Application, we made sure
    the code was optimal and the version was upgraded to final prior to submission.
"""

import random
import logging

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------
logging.basicConfig(
    filename='pet_rock_genie_v2.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ------------------------------------------------------------------------------
# Application Constants
# ------------------------------------------------------------------------------
VALID_EXIT_COMMANDS = ['quit', 'exit', 'bye']
VALID_ANSWER_TYPES = ['yes', 'no', 'maybe']

RESPONSES = {
    'yes': [
        "Yes! ◕ ◡ ◕",
        "The rock says YES!",
        "Absolutely yes! ᕦ(ò_óˇ)ᕤ"
    ],
    'no': [
        "No! ಥ_ಥ",
        "The rock says NO! (◣_◢)",
        "Denied! (╯°□°）╯"
    ],
    'maybe': [
        "Maybe... ( ͡° ͜ʖ ͡°)",
        "Uncertain... MAYBE! ( ͡๏ ͜x ͡๏)",
        "Try again later... ¯\\_(ツ)_/¯"
    ]
}

# ------------------------------------------------------------------------------
# Application Class
# ------------------------------------------------------------------------------
class PetRockGenie:
    """Primary logic for Pet Rock Genie"""

    def __init__(self):
        """Initialize counters and set response dictionary"""
        self.responses = RESPONSES
        self.question_count = 0
        logging.info("Version 2 Pet Rock Genie initialized")

    def get_answer(self, question):
        """Return a randomly selected yes/no/maybe answer"""
        answer_type = random.choice(VALID_ANSWER_TYPES)
        answer = random.choice(self.responses[answer_type])
        self.question_count += 1

        # Log question and answer
        logging.info(f"Question #{self.question_count}: {question}")
        logging.info(f"Answer: {answer}")

        return answer

    def run(self):
        """Main application loop for user interaction"""
        print("\n===============================")
        print("  PET ROCK GENIE — FINAL VERSION")
        print("  Version 2.1.0")
        print("===============================\n")

        print("Ask any yes/no question, or type 'quit' to exit.\n")
        logging.info("Application started (Version 2 Test Stage)")

        while True:
            try:
                question = input("Your question: ").strip()

                # Exit condition
                if question.lower() in VALID_EXIT_COMMANDS:
                    print(f"\n(ง'̀-'́)ง The rock rests after {self.question_count} questions.")
                    logging.info("Application closed by user.")
                    break

                # Empty input handling
                if not question:
                    print("Please enter a question for the rock!\n")
                    continue

                # Suggest proper question format
                if not question.endswith("?"):
                    print("(Tip: Questions usually end with '?')")

                print("(ง'̀-'́)ง The rock considers your question... (ง'̀-'́)ง")
                answer = self.get_answer(question)
                print(f"Answer: {answer}\n")

            except KeyboardInterrupt:
                print("\n\n(ง'̀-'́)ง The rock has been interrupted! Goodbye!\n")
                logging.warning("Application interrupted via keyboard.")
                break

            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                logging.error(f"Unhandled error: {str(e)}")
                break

# ------------------------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------------------------
def main():
    genie = PetRockGenie()
    genie.run()

if __name__ == "__main__":
    main()
