import chromadb


class VectorStore:
    def __init__(self):
        # New client creation method
        self.client = chromadb.PersistentClient(path="./chroma_db")
        
        # Create collection for products
        self.collection = self.client.get_or_create_collection(
            name="product_embeddings"
        )
    
    def clear_collection(self):
        """Clear all products from vector store"""
        try:
            self.client.delete_collection(name="product_embeddings")
            self.collection = self.client.create_collection(name="product_embeddings")
            print("✓ Cleared vector store")
        except Exception as e:
            print(f"Note: {e}")
    
    def add_products(self, products):
        """Add products to vector store"""
        print(f"Adding {len(products)} products to vector store...")
        
        ids = [str(p["id"]) for p in products]
        documents = [
            f"{p['name']} {p['category']} {p['description']}" 
            for p in products
        ]
        metadatas = [
            {
                "category": p["category"],
                "brand": p["brand"],
                "price": float(p["price"]),  # ChromaDB expects float value
                "rating": float(p["rating"])
            } 
            for p in products
        ]
        
        # Create chunks for batch processing (to avoid ChromaDB limit)
        batch_size = 25  # Smaller batches for faster visual progress
        total_batches = (len(ids) + batch_size - 1) // batch_size
        
        for i in range(0, len(ids), batch_size):
            batch_num = (i // batch_size) + 1
            batch_ids = ids[i:i + batch_size]
            batch_documents = documents[i:i + batch_size]
            batch_metadatas = metadatas[i:i + batch_size]
            
            self.collection.add(
                ids=batch_ids,
                documents=batch_documents,
                metadatas=batch_metadatas
            )
            print(f"  ⏳ Batch {batch_num}/{total_batches} - Added {len(batch_ids)} products (Total: {min(i + batch_size, len(ids))}/{len(ids)})")
        
        print(f"✓ Successfully added all {len(products)} products to vector store!")
    
    def search_similar_products(self, query, n_results=5):
        """Search similar products"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return {
            "ids": results["ids"][0],
            "documents": results["documents"][0],
            "metadatas": results["metadatas"][0],
            "distances": results["distances"][0] if "distances" in results else None
        }