import qdrant_client
from qdrant_client.models import Filter, FieldCondition, MatchValue


client = qdrant_client.QdrantClient(url="http://localhost:6333")

search_result = client.search(
    collection_name="test_collection",
    query_vector=[0.2, 0.01, 0.9, 0.7],
    query_filter=Filter(
        must=[FieldCondition(key="city", match=MatchValue(value="London"))]
    ),
    with_payload=True,
    limit=3,
)

print(search_result)