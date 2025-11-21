# COM-430-OL01 Software-Engineering: Group-2
Carlos Silva / Cody Bradley / Joseph Prignano
Group 2 Team Dev - Pet Rock Genie


# Pet Rock Genie Application

## Project Overview
A simple, interactive command-line application that answers yes/no questions like a mystical pet rock oracle.

## Specifications Met
- **Functionality**: Provides yes/no/maybe answers to user questions
- **User Interface**: Command-line interface with clear prompts
- **Logging**: Tracks all questions and answers
- **Error Handling**: Graceful handling of invalid inputs and interruptions
- **Reusability**: Object-oriented design with modular components

## Key Components
1. **PetRockGenie Class**: Main application logic
2. **Response System**: Categorized answers (yes/no/maybe)
3. **Logging System**: Activity tracking and debugging
4. **Error Handling**: User input validation

## Installation & Deployment

### Prerequisites
- Python 3.7 or higher

### Test Environment Setup
```bash
# Clone repository
git clone <repository-url>
cd pet-rock-genie

# Create test environment
python -m venv test-env
source test-env/bin/activate  # On Windows: test-env\Scripts\activate

# Run application
python pet_rock_genie.py
