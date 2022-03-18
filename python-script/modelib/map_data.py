import h5py
from rdflib import Graph, URIRef
from rdf_serializer import rdf_serializer


# Load data 
def main():
    G = Graph()
    file_path = "../../data/modelib-microstructure/model_ddd_data.h5"
    data = h5py.File(file_path, "r")
    node_data_50 = data['00000050']['node data']
    linker_data_50 = data['00000050']['linker data']
    loop_data_50 = data['00000050']['loop data']
    IRI = 'http://example.org/dislocation-microstructure/'
    # IRI = URIRef('http://example.org/dislocation-microstructure')
    G = rdf_serializer(node_data_50, linker_data_50, loop_data_50, IRI)
    G.serialize(destination='../../data/modelib-microstructure/dislocation-microstructure.ttl', format='turtle')

if __name__ == "__main__":
    main()