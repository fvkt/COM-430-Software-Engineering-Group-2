"""
Pet Rock Genie Application
Version: 2.1.0-Final
Environment: Final Version
COM-430-Software Engineering: Group 2
Instructor: Dr. Brian Holbert
Authors: Cody Bradley / Carlos Silva / Joseph Prignano

Description:
    Final version of the Pet Rock Genie Application.
    This release promotes the validated Test Stage (Version 2.0.0)
    to a Final environment with the same behavior plus minor
    documentation and banner updates for submission.
"""

import random
import logging

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------
logging.basicConfig(
    filename='pet_rock_genie_final.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ------------------------------------------------------------------------------
# Application Constants
# ------------------------------------------------------------------------------
APP_VERSION = "2.1.0-Final"
APP_ENVIRONMENT = "Final Version"

VALID_EXIT_COMMANDS = ["quit", "exit", "bye"]
VALID_ANSWER_TYPES = ["yes", "no", "maybe"]

RESPONSES = {
    "yes": [
        "Yes! ◕ ◡ ◕",
        "The rock says YES!",
        "Absolutely yes! ᕦ(ò_óˇ)ᕤ"
    ],
    "no": [
        "No! ಥ_ಥ",
        "The rock says NO! (◣_◢)",
        "Denied! (╯°□°）╯"
    ],
    "maybe": [
        "Maybe... ( ͡° ͜ʖ ͡°)",
        "Uncertain... MAYBE! ( ͡๏ ͜x ͡๏)",
        "Try again later... ¯\\_(ツ)_/¯"
    ]
}

# ------------------------------------------------------------------------------
# Application Class
# ------------------------------------------------------------------------------
class PetRockGenie:
    """Primary logic for Pet Rock Genie."""

    def __init__(self):
        """Initialize counters and set response dictionary."""
        self.responses = RESPONSES
        self.question_count = 0
        logging.info(
            "Pet Rock Genie initialized - Env=%s, Version=%s",
            APP_ENVIRONMENT,
            APP_VERSION,
        )

    def get_answer(self, question: str) -> str:
        """Return a randomly selected yes/no/maybe answer for the question."""
        answer_type = random.choice(VALID_ANSWER_TYPES)
        answer = random.choice(self.responses[answer_type])
        self.question_count += 1

        logging.info("Question #%d: %s", self.question_count, question)
        logging.info("Answer type: %s | Answer: %s", answer_type, answer)

        return answer

    def run(self) -> None:
        """Main application loop for user interaction."""
        print("\n===============================")
        print("  PET ROCK GENIE — FINAL VERSION")
        print(f"  Version {APP_VERSION}")
        print("===============================\n")

        print("Ask any yes/no question, or type 'quit' to exit.\n")
        logging.info("Application started (Final Environment)")

        while True:
            try:
                question = input("Your question: ").strip()

                # Exit condition
                if question.lower() in VALID_EXIT_COMMANDS:
                    print(
                        f"\n(ง'̀-'́)ง The rock rests after "
                        f"{self.question_count} questions."
                    )
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
                logging.error("Unhandled error: %s", str(e))
                break


# ------------------------------------------------------------------------------
# Entry Point
# ------------------------------------------------------------------------------
def main() -> None:
    genie = PetRockGenie()
    genie.run()


if __name__ == "__main__":
    main()
