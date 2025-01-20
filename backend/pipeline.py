from rdflib import Graph, Namespace, RDF, RDFS, OWL

def extract_ontology_description(turtle_file):
    g = Graph()
    g.parse(turtle_file, format="turtle")

    # Define namespaces
    OWL_NS = Namespace("http://www.w3.org/2002/07/owl#")
    XSD_NS = Namespace("http://www.w3.org/2001/XMLSchema#")

    # Extract Classes
    classes = set(g.subjects(RDF.type, OWL_NS.Class))

    # Extract Object and Datatype Properties
    object_properties = set(g.subjects(RDF.type, OWL_NS.ObjectProperty))
    datatype_properties = set(g.subjects(RDF.type, OWL_NS.DatatypeProperty))

    # Extract example triples
    example_triples = []
    for s, p, o in g:
        example_triples.append(f"{s.n3(g.namespace_manager)} {p.n3(g.namespace_manager)} {o.n3(g.namespace_manager)}.")

    # Create a human-readable description
    description = []

    # Classes
    description.append("Classes:")
    if classes:
        for cls in classes:
            label = g.value(cls, RDFS.label) or g.value(cls, Namespace("http://www.w3.org/2004/02/skos/core#prefLabel"))
            description.append(f"- {cls.n3(g.namespace_manager)} ({label if label else 'No label'})")
    else:
        description.append("- None found")

    # Properties
    description.append("\nObject Properties:")
    if object_properties:
        for prop in object_properties:
            domain = list(g.objects(prop, RDFS.domain))
            range_ = list(g.objects(prop, RDFS.range))
            domain_str = ", ".join(d.n3(g.namespace_manager) for d in domain) if domain else "Unknown"
            range_str = ", ".join(r.n3(g.namespace_manager) for r in range_) if range_ else "Unknown"
            label = g.value(prop, Namespace("http://www.w3.org/2004/02/skos/core#prefLabel"))
            description.append(f"- {prop.n3(g.namespace_manager)} (label: {label if label else 'No label'}, domain: {domain_str}, range: {range_str})")
    else:
        description.append("- None found")

    description.append("\nDatatype Properties:")
    if datatype_properties:
        for prop in datatype_properties:
            domain = list(g.objects(prop, RDFS.domain))
            range_ = list(g.objects(prop, RDFS.range))
            domain_str = ", ".join(d.n3(g.namespace_manager) for d in domain) if domain else "Unknown"
            range_str = ", ".join(r.n3(g.namespace_manager) for r in range_) if range_ else "Unknown"
            label = g.value(prop, Namespace("http://www.w3.org/2004/02/skos/core#prefLabel"))
            description.append(f"- {prop.n3(g.namespace_manager)} (label: {label if label else 'No label'}, domain: {domain_str}, range: {range_str})")
    else:
        description.append("- None found")

    description.append("\nExample Triples:")
    if example_triples:
        description.extend(f"- {triple}" for triple in example_triples[:10])  
    else:
        description.append("- None found")

    return "\n".join(description)
