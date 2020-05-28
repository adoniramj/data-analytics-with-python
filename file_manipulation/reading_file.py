import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'poem.txt')

file_data = open(my_file, "r").read()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

word_list = file_data.split()
word_count = {}

for word in word_list:
  word_lowercase = word.lower()
  if word_lowercase not in punctuations and word_lowercase not in uninteresting_words:
    if word_lowercase not in word_count:
      word_count[word_lowercase] = 0
    word_count[word_lowercase] += 1

print(word_count)
  