import pandas
# Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
#output_list = [value for letter in word for (key, value) in phonetic_dict.items() if key == letter]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)