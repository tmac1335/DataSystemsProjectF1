
TESTS = [
    {
        "query": "Retrieve the model of the lightbulb in the lighting system of Building G.",
        "sparql": """
            SELECT ?model
            WHERE {
              <https://test.org/dsp_groupf1/def#SP_Building_G_LightingSystem>
                <https://test.org/dsp_groupf1/def#hasPart>
                ?lightbulb .
              ?lightbulb <https://test.org/dsp_groupf1/def#model> ?model .
            }
        """,
        "expected_output": [
            "model",
            "Phillips 123A"
        ]
    },
    {
        "query": "Retrieve the wattage of the lightbulb in the lighting system of Building F.",
        "sparql": """
            SELECT ?wattage
            WHERE {
              <https://test.org/dsp_groupf1/def#SP_Building_F_LightingSystem>
                <https://test.org/dsp_groupf1/def#hasPart>
                ?lightbulb .
              ?lightbulb <https://test.org/dsp_groupf1/def#wattage> ?wattage .
            }
        """,
        "expected_output": [
            "wattage",
            "12.5"
        ]
    },
    {
        "query": "Retrieve all lightbulbs and their models.",
        "sparql": """
            SELECT ?lightbulb ?model
            WHERE {
              ?lightbulb a <https://test.org/dsp_groupf1/def#Lightbulb> ;
                         <https://test.org/dsp_groupf1/def#model> ?model .
            }
        """,
        "expected_output": [
            ["lightbulb", "model"],
            ["https://test.org/dsp_groupf1/def#Lightbulb_building_G", "Phillips 123A"],
            ["https://test.org/dsp_groupf1/def#Lightbulb_building_F", "IKEA NOT GOOD"]
        ]
    },
    {
        "query": "Retrieve all buildings and their lighting systems.",
        "sparql": """
            SELECT ?building ?lightingSystem
            WHERE {
              ?lightingSystem a <https://test.org/dsp_groupf1/def#SP_Building_F_LightingSystem> ;
                              rdfs:subClassOf ?building .
            }
        """,
        "expected_output": [
            ["building", "lightingSystem"],
            ["https://test.org/dsp_groupf1/def#SP_Building_F", "https://test.org/dsp_groupf1/def#SP_Building_F_LightingSystem"],
            ["https://test.org/dsp_groupf1/def#SP_Building_G", "https://test.org/dsp_groupf1/def#SP_Building_G_LightingSystem"]
        ]
    },
    {
        "query": "Retrieve all floors in Building A.",
        "sparql": """
            SELECT ?floor
            WHERE {
              ?floor rdfs:subClassOf <https://test.org/dsp_groupf1/def#SP_Building_A> .
            }
        """,
        "expected_output": [
            "floor",
            "https://test.org/dsp_groupf1/def#Floor1_A",
            "https://test.org/dsp_groupf1/def#Floor2_A",
            "https://test.org/dsp_groupf1/def#Floor3_A"
        ]
    },
    {
        "query": "Retrieve all classes that are subclasses of Science Park 904 campus.",
        "sparql": """
            SELECT ?subclass
            WHERE {
              ?subclass rdfs:subClassOf <https://test.org/dsp_groupf1/def#SP904> .
            }
        """,
        "expected_output": [
            "subclass",
            "https://test.org/dsp_groupf1/def#SP_Building_A",
            "https://test.org/dsp_groupf1/def#SP_Building_B",
            "https://test.org/dsp_groupf1/def#SP_Building_C",
            "https://test.org/dsp_groupf1/def#SP_Building_D",
            "https://test.org/dsp_groupf1/def#SP_Building_E",
            "https://test.org/dsp_groupf1/def#SP_Building_F",
            "https://test.org/dsp_groupf1/def#SP_Building_G"
        ]
    },
    {
        "query": "Retrieve the prefLabel of all classes.",
        "sparql": """
            SELECT ?class ?label
            WHERE {
              ?class a owl:Class ;
                     skos:prefLabel ?label .
            }
        """,
        "expected_output": [
            ["class", "label"],
            ["https://test.org/dsp_groupf1/def#Object", "Object"],
            ["https://test.org/dsp_groupf1/def#SP904", "Science Park 904 campus"],
            ["https://test.org/dsp_groupf1/def#SP_Building_A", "Building A"],
            ["https://test.org/dsp_groupf1/def#SP_Building_B", "Building B"],
            ["https://test.org/dsp_groupf1/def#SP_Building_C", "Building C"],
            ["https://test.org/dsp_groupf1/def#SP_Building_D", "Building D"],
            ["https://test.org/dsp_groupf1/def#SP_Building_E", "Building E"],
            ["https://test.org/dsp_groupf1/def#SP_Building_F", "Building F"],
            ["https://test.org/dsp_groupf1/def#SP_Building_G", "Building G"]
        ]
    },
    {
        "query": "Retrieve the prefLabel and model of all lightbulbs.",
        "sparql": """
            SELECT ?label ?model
            WHERE {
              ?lightbulb a <https://test.org/dsp_groupf1/def#Lightbulb> ;
                         skos:prefLabel ?label ;
                         <https://test.org/dsp_groupf1/def#model> ?model .
            }
        """,
        "expected_output": [
            ["label", "model"],
            ["Lightbulb_building_G", "Phillips 123A"],
            ["Lightbulb_building_F", "IKEA NOT GOOD"]
        ]
    }
]