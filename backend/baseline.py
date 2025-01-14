from openai import OpenAI
import os
from difflib import get_close_matches
import json
import re
from data import ENTITY_TYPES, RELATIONSHIP_TYPES

api_key = os.getenv('OPENAI_API_KEY')
organisation = os.getenv('ORGANISATION')
client = OpenAI(organization=organisation, api_key=api_key)


def construct_sparql_query(nl_query):

    prompt = f"""
    Create a Sparql query from a natural language query:
    "{nl_query}"
    The Entity and Relationship types are given, coming from the linked database. Semantically match the entities and relationships in the query to the ones in the database also apply any filters necessary. Only output the given query.
    - `Here is a list of entities and relationships in the database, so use those to find the closest related ones`: entitites: "{ENTITY_TYPES}", relationships: "{RELATIONSHIP_TYPES}
    "
    """

    response = client.chat.completions.create(
        model="o1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    choice_str = response.choices[0].message.content
    
    return choice_str
