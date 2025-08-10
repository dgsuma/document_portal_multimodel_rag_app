import sys
import os
from operator import itemgetter
from typing import List, Optional
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType

class ConversationalRAG:
    def __init__(self):
        pass
    
    def load_retiever_from_faiss(self):
        pass
    
    def invoke(self):
        pass
    
    def _load_llm(self):
        pass
    
    
    ''' 3 type of OOP methods: class, instance and static methods. static methods can be called without an instance 
    it can't access instance variables or methods. root or reusable functionality we can kept here '''
    @staticmethod
    def _format_docs(docs):
        pass
    
    def _build_lcel_chain(self):
        pass
    
    
    