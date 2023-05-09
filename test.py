import requests
number_words=10
url = f"https://random-word-api.herokuapp.com/word?number={number_words}"
response = requests.get(url)
sentence_word = response.json()
text_sentence = ' '.join(sentence_word)
print(text_sentence)