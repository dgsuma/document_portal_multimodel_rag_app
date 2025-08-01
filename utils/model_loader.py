import os
import sys
from dotenv import load_dotenv
from utils.config_loader import load_config

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
#from langchain_openai import ChatOpenAI
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
log = CustomLogger().get_logger(__name__)

class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    
    def __init__(self):
        """Initializes the ModelLoader class.
        """
        pass
    
    def _validate_env(self):
        """
        Validates the environment variables required for the model loading.
        Ensure API keys exist.
        """
        pass
    
    def load_embeddings(self):
        """
        Loads the embedding model based on the configuration.
        Returns:
            An instance of the embedding model.
        """
        pass
        
    def load_llm(self):
        """
        Load and return the LLM model.
        """
        """Load LLM dynamically based on provider in config."""
        
        pass  