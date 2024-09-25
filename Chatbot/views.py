from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config



def homePage(request):
    print("YOU ARE HERE")
    return render(request, 'chatbot.html')

# Import modules
import openai
import os
import sys

#import class from modules
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from rest_framework import status

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
# class ChatBotAPI(APIView):
#     def post(self, request):

#         os.environ["OPENAI_API_KEY"] = ""

#         query = request.data.get('question')
#         if len(sys.argv) > 1:
#             query = sys.argv[1]
#         # question = request.data.get('question')
#         # if not question:
#         #     return Response({"error": "No question provided"}, status=status.HTTP_400_BAD_REQUEST)

#         loader = DirectoryLoader(os.path.join(BASE_DIR, 'Chatbot/mydata/'))
#         documents = loader.load()

#         text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#         texts = text_splitter.split_documents(documents)

#         embeddings = OpenAIEmbeddings()
#         docsearch = Chroma.from_documents(texts, embeddings)

#         qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())

#         chain = ConversationalRetrievalChain.from_llm(
#             llm=ChatOpenAI(model="gpt-3.5-turbo"),
#             retriever=docsearch.as_retriever(search_kwargs={"k": 1}),
        # )

        # chat_history = []
        # while True:
        #     if not query:
        #         query = input("Prompt: ")
        #     if query in ['quit', 'q', 'exit']:
        #         sys.exit()
        #     result = chain({"question": query, "chat_history": chat_history})
        #     print(result['answer'])

        #     chat_history.append((query, result['answer']))
        #     query = None

        # return Response("Success")
    
# class ChatBotAPI(APIView):
#     def post(self, request):
#         question = request.data.get('question')
#         return Response("Success")

class ChatBotAPI(APIView):
    def post(self, request):
        OPENAI_API_KEY = config('OPENAI_API_KEY') 
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

        question = request.data.get('question')
        if not question:
            return Response({"error": "No question provided"}, status=status.HTTP_400_BAD_REQUEST)

        loader = DirectoryLoader(os.path.join(BASE_DIR, 'Chatbot/mydata/'))
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()
        docsearch = Chroma.from_documents(texts, embeddings)

        qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())

        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model="gpt-3.5-turbo"),
            retriever=docsearch.as_retriever(search_kwargs={"k": 1}),
        )

        chat_history = request.data.get('chat_history', [])
        
        result = chain({"question": question, "chat_history": chat_history})
        
        chat_history.append((question, result['answer']))

        return Response({"answer": result['answer'], "chat_history": chat_history}, status=status.HTTP_200_OK)