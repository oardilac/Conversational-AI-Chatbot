import pandas as pd
import openai
from openai.embeddings_utils import get_embedding, cosine_similarity

def generate_embeddings(input_data, engine="text-embedding-ada-002"):
    if isinstance(input_data, str):
        return get_embedding(input_data, engine=engine)
    elif isinstance(input_data, list):
        result = {}
        for i in input_data:
            result[i] = get_embedding(i, engine=engine)
        return result
    elif isinstance(input_data, pd.DataFrame):
        input_data['Embedding'] = input_data['texto'].apply(lambda x: get_embedding(x, engine=engine))
        return input_data
    else:
        raise TypeError("Unsupported input_data type. Must be a string, list, or DataFrame.")

def search_embedding(query, data, n_results=5):
    query_embed = get_embedding(query, engine="text-embedding-ada-002")
    data["Similarity"] = data['Embedding'].apply(lambda x: cosine_similarity(x, query_embed))
    data = data.sort_values("Similarity", ascending=False)
    return data.iloc[:n_results][["text", "Similarity"]]

def load_embeddings_data(path):
    embeddings_df = pd.read_csv(path)
    return embeddings_df