class inputReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_text(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()

        except FileNotFoundError:
            return None

#Feature1
class WordCounter:
    def count(self, text:str):
        words = text.split()
        return len(words)

#Feature2
class CharacterCounter:
    def count(self, text:str):
        return len(text)

#Feature3
class SentenceCounter:
    def count(self, text:str):
        sentence_count = 0
        for char in text:
            if char in ".!?":
                sentence_count += 1
        return sentence_count

class OutputWriter:
    def display_results(self, word_count: int, character_count: int, sentence_count: int):
        print("\n===== TEXT ANALYSIS RESULTS =====")
        print(f"Word Count      :{word_count}")
        print(f"Character Count :{character_count}")
        print(f"Sentence Count  :{sentence_count}")

def main():
    file_path = input("Enter text file path: ")
    reader = inputReader(file_path)
    text = reader.read_text()

    if text is None:
        print("Error: File not found.")
        return

    word_counter = WordCounter()
    character_counter = CharacterCounter()
    sentence_counter = SentenceCounter()

    word_count = word_counter.count(text)
    character_count = character_counter.count(text)
    sentence_count = sentence_counter.count(text)

    writer = OutputWriter()
    writer.display_results(word_count, character_count, sentence_count)

if __name__ =="__main__":
    main()
