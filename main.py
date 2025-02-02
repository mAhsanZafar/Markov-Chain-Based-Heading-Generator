import pandas as pd
import random
from collections import defaultdict

def build_transition_matrix(headings):
    transition_matrix = defaultdict(lambda: defaultdict(int))
    for heading in headings:
        words = heading.split()
        for i in range(len(words) - 1):
            transition_matrix[words[i]][words[i + 1]] += 1
    
    # Convert counts to probabilities
    for current_word, next_words in transition_matrix.items():
        total = sum(next_words.values())
        transition_matrix[current_word] = {word: count / total for word, count in next_words.items()}
    
    return transition_matrix

def generate_heading(transition_matrix, start_word=None, max_length=10):
    if start_word is None:
        start_word = random.choice(list(transition_matrix.keys()))
    
    heading = [start_word]
    while len(heading) < max_length:
        current_word = heading[-1]
        if current_word not in transition_matrix or not transition_matrix[current_word]:
            break
        next_words = list(transition_matrix[current_word].keys())
        probabilities = list(transition_matrix[current_word].values())
        next_word = random.choices(next_words, probabilities)[0]
        heading.append(next_word)
    
    return " ".join(heading)

def suggest_next_word(transition_matrix, sentence, num_suggestions=5):
    words = sentence.split()
    if not words:
        return []
    last_word = words[-1]
    if last_word not in transition_matrix:
        return []
    
    next_word_probabilities = transition_matrix[last_word]
    suggestions = sorted(next_word_probabilities, key=next_word_probabilities.get, reverse=True)
    return suggestions[:num_suggestions]

def interactive_sentence_builder(transition_matrix):
    print("Type words one by one. Type '.' to finish a sentence or 'exit' to quit.")
    
    while True:
        sentence = []
        while True:
            word = input("Enter a word: ")
            if word == "exit":
                return
            elif word == ".":
                print("Final Sentence:", " ".join(sentence))
                break
            
            sentence.append(word)
            suggestions = suggest_next_word(transition_matrix, " ".join(sentence))
            if suggestions:
                print("Next word suggestions:", ", ".join(suggestions))

def main(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    headings = df['headline_text'].dropna().astype(str).tolist()
    
    # Build transition matrix
    transition_matrix = build_transition_matrix(headings)
    
    # Generate a heading
    generated_heading = generate_heading(transition_matrix)
    print("Generated Heading:", generated_heading)
    
    # Start interactive sentence builder
    interactive_sentence_builder(transition_matrix)

if __name__ == "__main__":
    file_path = "abcnews-date-text.csv"
    main(file_path)
