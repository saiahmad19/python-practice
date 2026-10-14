import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer, util

SHOW_STEPS = True

load_dotenv()
my_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=my_key)

text = "Python variables store data. Functions return values. Classes bundle data and behavior. Loops repeat actions. Dictionaries store key-value pairs."


def chunk_by_sentence(text):
    sentences = text.split(".")
    chunks = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            chunks.append(sentence)
    return chunks


result = chunk_by_sentence(text)
if SHOW_STEPS:
    print("PAGES:", result)

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(result)
if SHOW_STEPS:
    print("PAGE COORDINATES SHAPE:", embeddings.shape)


def ask(question):
    question_embedding = model.encode(question)
    if SHOW_STEPS:
        print("QUESTION COORDINATE SHAPE:", question_embedding.shape)

    scores = util.cos_sim(question_embedding, embeddings)
    if SHOW_STEPS:
        print("SCORES (one per page):", scores)

    best_index = scores.argmax()
    if SHOW_STEPS:
        print("WINNING PAGE:", result[best_index])

    prompt = f"""Use the information below to answer the question. If it contains the answer, base your answer on it. If it doesn't, start with "That's not in my notes," then give a short answer from your own knowledge.

Information: {result[best_index]}

Question: {question}"""
    if SHOW_STEPS:
        print("NOTE SENT TO LLM:\n" + prompt)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


while True:
    question = input("\nyou: ")
    if question.lower() == "quit":
        print("Goodbye")
        break
    print("\nbot:", ask(question))