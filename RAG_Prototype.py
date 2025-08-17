import os
from dotenv import load_dotenv
load_dotenv()

# document loader
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
#db import
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore

#Took path of pdf
pdf_path =Path(__file__).parent/ "nodejs.pdf"

#Loaded the pdf
loader=PyPDFLoader(pdf_path)
docs= loader.load()

#Text- Splitter
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
#Used the splitter to split the docs
split_docs=text_splitter.split_documents(documents=docs)

#Embedder
embedder = OpenAIEmbeddings(
    model="text-embedding-3-large",
    # By removing the api_key line, the library will now [api_key="OPENAI_API_KEY"]
    # automatically find the OPENAI_API_KEY from your .env file.
)

# vector_store=QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333/",
#     collection_name="langchain_RAG",
#     embedding=embedder
# )
# #fedding the data into the vector store
# vector_store.add_documents(documents=split_docs)

print("Injestion Done")

#retrtiver
retriver= vector_store=QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333/",
    collection_name="langchain_RAG",
    embedding=embedder
)

# relevant_chunks=retriver.similarity_search(
#     query="What is FS Module?"
# )

# SYSTEM_PROMPT=f"""
# You are a helpful AI Assistant who responds based on the available context.

# Context:
# {relevant_chunks}
# """

# print("Relevant Chunks ", relevant_chunks)

# #chat
# llm = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
# )

# messages = [
#         SYSTEM_PROMPT,
#     ("human", "I am a curious folk."),
# ]
# ai_msg = llm.invoke(messages)
# ai_msg


# ==============================================================================

#Initiate the chat model once, outside the loop

llm= ChatOpenAI(
    model='gpt-4o',
    temperature=0
)

#Start a loop that will run forever until you type 'exit'

while True:

    #1. GET User Q
    user_q=input("\nAsk a question about your PDF (or type 'exit' to quit): ")

    if user_q.lower()=='exit':
        break

    #2. Retrieve relevant chunks based on user's questions
    relevant_chunks=retriver.similarity_search(
        query=user_q
    )

    #3 Create the SYSTEM PROMPT with the retrived contect
    SYSTEM_PROMPT=f"""
    You are a helpful AI Assistant who responds based on the available context.

    Context:
    {relevant_chunks}
    """

    #4. Create the message list for the LLM
    messages=[
        ("system", SYSTEM_PROMPT),
        ("human", user_q)
    ]

    #5. Call the model and get the response 
    print("Sending context and question to the AI...")
    ai_message=llm.invoke(messages)

    #6. PRINT the final answer for the user
    #access the .content attribute to get the clean text
    print("\nAssistant:")
    print(ai_message.content)