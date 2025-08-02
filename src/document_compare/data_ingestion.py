import sys
from pathlib import Path
import fitz
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

class DocumentIngestion:
    def __init__(self, base_dir:str="data\\document_compare"):
        self.log = CustomLogger().get_logger(__name__)
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    def delete_existing_files(self):
        """
        Deletes existing files at the specified paths.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error deleting existing files: {e}")
            raise DocumentPortalException("An error occurred while deleting existing files.", sys)   
    
    def save_uploaded_files(self):
        """
        Saves uploaded files to a specific directory.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error saving uploaded files: {e}")
            raise DocumentPortalException("An error occurred while saving uploaded files.", sys)
    
    def read_pdf(self):
        """
        Reads a PDF file and extracts text from each page.
        """
        try:
            pass
        except Exception as e:
            self.log.error(f"Error reading PDF: {e}")
            raise DocumentPortalException("An error occurred while reading the PDF.", sys)
