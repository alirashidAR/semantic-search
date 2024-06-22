import qdrant_client

client = qdrant_client.QdrantClient(url="http://localhost:6333")

search_result = client.search(
    collection_name="test_collection", query_vector=[0.2, 0.1, 0.9, 0.7], limit=3
)

print(search_result)