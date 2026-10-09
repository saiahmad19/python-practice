text = "Python variables store data. Functions return values. Classes bundle data and behavior. Loops repeat actions. Dictionaries store key-value pairs."


def chunk_by_sentence(text):
    sentences = text.split(".")
    chunks = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            chunks.append(sentence)
    return chunks

words = text.split()
result = chunk_by_sentence(text)
print(result)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(result)

print(embeddings.shape)

question_embedding = model.encode("what does a loop do?")
print(question_embedding.shape)