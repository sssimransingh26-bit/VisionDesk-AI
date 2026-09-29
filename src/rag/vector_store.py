import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")


def create_vector_store(chunks):
    """
    Convert chunks into embeddings and store them in ChromaDB.
    """

    collection = client.get_or_create_collection(
        name="knowledge_base"
    )

    embeddings = model.encode(chunks).tolist()

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return collection


def search_documents(query, n_results=3):
    """
    Search the vector database using semantic similarity.
    """

    collection = client.get_collection(
        name="knowledge_base"
    )

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results


if __name__ == "__main__":
    from src.rag.documents import process_file

    # Process safety manual
    chunks = process_file("data/safety_manual.pdf")

    # Store chunks in ChromaDB
    collection = create_vector_store(chunks)

    print("Vector store created successfully!")
    print("Number of chunks:", len(chunks))

    # Test semantic search
    results = search_documents("Is a safety helmet required?")

    print("\nSearch Results:")

    for document in results["documents"][0]:
        print("\n---")
        print(document)