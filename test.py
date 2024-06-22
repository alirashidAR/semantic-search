from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    {
        "date": "2022-01-01",
        "entry" :" Today was a good day. I went to the park and played with my friends. We had a picnic and played games. I had a lot of fun."
    },
    {
        "date": "2022-01-02",
        "entry" :" Today was a bad day. I got into a fight with my friend and we are not talking to each other. I am sad and lonely."
    },
    {
        "date": "2022-01-03",
        "entry" :" Today was a boring day. I stayed home and watched TV all day. I was bored and did not have anything to do."
    }
]

client = QdrantClient(
    url="https://7b87ab8a-b1f0-4f2e-a542-6cbc12bb7d5d.us-east4-0.gcp.cloud.qdrant.io/",
    api_key="2_nmpJff_-6T0DYMwnr0h5KpnnJ9Sl8QwwLN7F0dSlPYAhoppVrOxw"
)

client.recreate_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

client.upload_points(
    collection_name="my_books",
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["entry"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)

hits = client.search(
    collection_name="my_books",
    query_vector=encoder.encode("sad day").tolist(),
    limit=1,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)