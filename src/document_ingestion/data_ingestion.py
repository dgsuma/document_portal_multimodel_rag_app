from __future__ import annotations
import os
import sys
import json
import uuid
import hashlib
import shutil
from pathlib import Path
from datetime import datetime, timezone
from typing import Iterable, List, Optional, Dict, Any

import fitz  # PyMuPDF
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_community.vectorstores import FAISS

from utils.model_loader import ModelLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

from utils.file_io import _session_id, save_uploaded_files
from utils.document_ops import load_documents, concat_for_analysis, concat_for_comparison

class FaissManager:
    def __init__(self, index_dir: Path, model_loader: Optional[ModelLoader] = None):
        pass
    
    def _exists(self)-> bool:
        pass
    
    @staticmethod
    def _fingerprint(text: str, md: Dict[str, Any]) -> str:
        """ no duplicate entries allowed inside the faiss database """
        pass
    
    def _save_meta(self):
        pass
    
    def add_documents(self,docs: List[Document]):
        """ Add documents to the FAISS index """
        pass
    
    def load_or_create(self,texts:Optional[List[str]]=None, metadatas: Optional[List[dict]] = None):
        """ Load or create a FAISS index """
        pass

class ChatIngestor:
    pass

class DocHandler:
    def __init__(self):
        pass
    def save_pdf(self, uploaded_file) -> str:
        pass
    def read_pdf(self, pdf_path: str) -> str:
        pass

class DocumentComparator:
    def __init__(self):
        pass
    def save_uploaded_files(self, reference_file, actual_file):
        pass
    def read_pdf(self, pdf_path: Path) -> str:
        pass
    def combine_documents(self) -> str:
        pass
    def clean_old_sessions(self, keep_latest: int = 3):
        pass