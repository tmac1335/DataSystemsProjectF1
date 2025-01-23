test_data = {
  "tests": [
    {
      "query": "Retrieve all buildings and their labels.",
      "sparql": """
        SELECT ?building ?label
        WHERE {
          ?building rdf:type <https://test.org/dsp_groupf1/def#Object> .
          ?building skos:prefLabel ?label .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Find all doors in Building B1.",
      "sparql": """
        SELECT ?door
        WHERE {
          <https://test.org/dsp_groupf1/def#SP_Building_B1_Doors> <https://test.org/dsp_groupf1/def#hasDoor> ?door .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Retrieve the wattage of all lightbulbs.",
      "sparql": """
        SELECT ?lightbulb ?wattage
        WHERE {
          ?lightbulb rdf:type <https://test.org/dsp_groupf1/def#Lightbulb> .
          ?lightbulb <https://test.org/dsp_groupf1/def#wattage> ?wattage .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Get all lighting systems and their parts.",
      "sparql": """
        SELECT ?lightingSystem ?lightingPart
        WHERE {
          ?lightingSystem rdf:type <https://test.org/dsp_groupf1/def#LightingSystemUnion> .
          ?lightingSystem <https://test.org/dsp_groupf1/def#hasLightingPart> ?lightingPart .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Find the model of all doors in Floor 3 B.",
      "sparql": """
        SELECT ?door ?model
        WHERE {
          ?door rdf:type <https://test.org/dsp_groupf1/def#Door> .
          <https://test.org/dsp_groupf1/def#SP_Building_B3_Doors> <https://test.org/dsp_groupf1/def#hasDoor> ?door .
          ?door <https://test.org/dsp_groupf1/def#DoorModel> ?model .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Retrieve all subclasses of Building A.",
      "sparql": """
        SELECT ?subclass
        WHERE {
          ?subclass rdfs:subClassOf <https://test.org/dsp_groupf1/def#SP_Building_A> .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Find the label of Building E.",
      "sparql": """
        SELECT ?label
        WHERE {
          <https://test.org/dsp_groupf1/def#SP_Building_E> skos:prefLabel ?label .
        }
      """,
      "expected_output": []
    },
    {
      "query": "List all doors and their models.",
      "sparql": """
        SELECT ?door ?model
        WHERE {
          ?door rdf:type <https://test.org/dsp_groupf1/def#Door> .
          ?door <https://test.org/dsp_groupf1/def#DoorModel> ?model .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Get all lighting systems in Building A.",
      "sparql": """
        SELECT ?lightingSystem
        WHERE {
          ?lightingSystem rdfs:subClassOf <https://test.org/dsp_groupf1/def#SP_Building_A> .
          ?lightingSystem rdf:type <https://test.org/dsp_groupf1/def#LightingSystemUnion> .
        }
      """,
      "expected_output": []
    },
    {
      "query": "Find all floors in Building B.",
      "sparql": """
        SELECT ?floor
        WHERE {
          ?floor rdfs:subClassOf <https://test.org/dsp_groupf1/def#SP_Building_B> .
        }
      """,
      "expected_output": []
    }
  ]
}
