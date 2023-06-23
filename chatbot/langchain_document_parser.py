from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

class LangchainDocumentParser:
    def __init__(self, path):
        self.loader = PyPDFLoader(path)
        self.splitter = CharacterTextSplitter(chunk_size=300, separator = '.\n')

    def parse_document(self):
        pages = self.loader.load_and_split()
        texts = self.splitter.split_documents(pages)
        return texts