from openai import OpenAI
import os
from difflib import get_close_matches
import json
import re

api_key = os.getenv('OPENAI_API_KEY')
organisation = os.getenv('ORGANISATION')
client = OpenAI(organization=organisation, api_key=api_key)


def construct_sparql_query(user_query):

    with open('../data/ontology_description.txt', 'r') as file:
        ontology_description = file.read()
    task = """
        Task:
        You are an assistant trained to generate SPARQL queries based on the given ontology and user prompts. Use the ontology description to understand the structure and generate accurate queries. Assume the ontology is loaded in a database.
        only return the sparql query.
        """

    prompt = f"""
    Ontology Description:
    {ontology_description}

    {task}

    User Query:
    {user_query}
    """

    response = client.chat.completions.create(
        model="o1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    choice_str = response.choices[0].message.content
    
    return choice_str

def construct_sparql_queries(user_query):

    with open('../data/ontology_description.txt', 'r') as file:
        ontology_description = file.read()

    task = """
        Task:
        You are an assistant trained to generate SPARQL queries based on the given ontology and user prompts. Use the ontology description to understand the structure and generate accurate queries. Assume the ontology is loaded in a database.
        only return the sparql query.
        """

    prompt = f"""
    Ontology Description:
    {ontology_description}

    {task}

    User Query:
    {user_query}
    """

    response = client.chat.completions.create(
        model="o1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        n=3
    )

    choice_list = [choice.message.content[9:-3] for choice in response.choices]
    
    return choice_list