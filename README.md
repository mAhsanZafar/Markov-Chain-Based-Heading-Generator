This script processes a dataset of headlines and generates new headlines based on a probabilistic transition matrix. It also includes an interactive sentence-building feature. Here's how it works:

1. Data Processing:
Reads a CSV file (abcnews-date-text.csv) containing news headlines.
Extracts and cleans the headlines.
2. Transition Matrix Construction:
Builds a transition matrix, which maps each word in the headlines to possible next words along with their probabilities.
3. Headline Generation:
Randomly selects a starting word.
Uses the transition matrix to generate a headline by probabilistically choosing the next word.
4. Interactive Sentence Builder:
Allows users to build sentences one word at a time.
Suggests the most probable next words based on previous input.
Users can complete a sentence by typing . or exit by typing exit.
Main Functions:
build_transition_matrix(headings) → Constructs a word transition probability matrix.
generate_heading(transition_matrix, start_word=None, max_length=10) → Generates a random headline.
suggest_next_word(transition_matrix, sentence, num_suggestions=5) → Suggests the next word based on input.
interactive_sentence_builder(transition_matrix) → Runs an interactive session where the user builds a sentence word by word.
main(file_path) → Loads data, builds the transition matrix, generates a headline, and starts the interactive session.
Usage:
Run the script with python script.py.
It will generate a sample headline.
It will then start an interactive mode where users can build sentences with word suggestions.
This script is useful for text prediction, AI-assisted writing, and natural language processing (NLP) experiments. 🚀
