import h5py
from rdflib import Graph
import json
from rdf_serializer import rdf_serializer


# Load data 
def main():
    G = Graph()
    path_microstructure = "../../data/modelib-microstructure/modelib-nickel-microstructure.h5"
    path_nickel_cif = "../../crystal-structure-ontology/data/MaterialProject/Nickel/json/Ni_mp-23_conventional_standard.json"
    path_nickel_space_group = "../../crystal-structure-ontology/data/MaterialProject/Nickel/spacegroup/mp-23_spacegroup.json"
    data = h5py.File(path_microstructure, "r")
    node_data_50 = data['00000050']['node data']
    linker_data_50 = data['00000050']['linker data']
    loop_data_50 = data['00000050']['loop data']
    IRI = 'http://example.org/dislocation-microstructure/'

    with open(path_nickel_cif) as data1, open(path_nickel_space_group) as data2: 
        json_nickel_data = json.load(data1)
        json_nickel_sg = json.load(data2)

    G = rdf_serializer(json_nickel_data, json_nickel_sg, node_data_50, linker_data_50, loop_data_50, IRI)
    G.serialize(destination='../../data/modelib-microstructure/modelib-nickel-microstructure.ttl', format='turtle')

if __name__ == "__main__":
    main()