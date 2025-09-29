import chromadb
from sentence_transformers import SentenceTransformer
import os

class RAGPipeline:
    def __init__(self, model_name: str = 'BAAI/bge-small-en-v1.5'):
        self.embedding_model = SentenceTransformer(model_name)
        self.chroma_client = chromadb.HttpClient(
            host=os.getenv("CHROMA_HOST", "localhost"),
            port=os.getenv("CHROMA_PORT", 8000)
        )
        self.collection = self.chroma_client.get_or_create_collection(name="brand_voice")

    def ingest_document(self, doc_id: str, text: str, metadata: dict):
        """Encodes and stores a document in the vector database."""
        embedding = self.embedding_model.encode(text, normalize_embeddings=True).tolist()
        self.collection.add(
            embeddings=[embedding],
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )
        print(f"Ingested document with ID: {doc_id}")

    def retrieve(self, query: str, n_results: int = 3) -> list[str]:
        """Retrieves relevant document chunks for a given query."""
        query_embedding = self.embedding_model.encode(query, normalize_embeddings=True).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results.get('documents', [[]])[0]