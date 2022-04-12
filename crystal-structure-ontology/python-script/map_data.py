import json
import os
from rdflib import Graph
from rdf_serializer import rdf_serializer
from pathlib import Path

# slip plane and slip direction data for face-centered cubic
slip_configs={'(11-1)':['[101]', '[1-10]', '[011]'], 
                  '(111)':['[1-10]', '[10-1]', '[0-11]'],
                  '(1-11)':['[10-1]', '[110]', '[011]'],
                  '(1-1-1)':['[110]', '[101]', '[0-11]'],
                 }
# slip plane normals for face-centered cubic
slip_plane_normals = {'(11-1)': ['[11-1]',] ,
                           '(111)': ['[111]']  ,
                           '(1-11)':['[1-11]']  ,
                          '(1-1-1)':['[1-1-1]'], 
                         }
# Load data 
def main():
    G = Graph()
    for path1, path2 in zip(Path("../data/MaterialProject/Nickel/json/").iterdir(), Path("../data/MaterialProject/Nickel/spacegroup/").iterdir()):
        if (path1.is_file()) and(path2.is_file()):
            base_1 = os.path.basename(path1)
            mat_id = os.path.splitext(base_1)[0]
            base_2 = os.path.basename(path2)
            sg_id = os.path.splitext(base_2)[0]
            example_uri = "http://www.example.org/{}/".format(mat_id)
            with open(path1) as data1, open(path2) as data2: 
                json_nickel_data = json.load(data1)
                json_nickel_sg = json.load(data2)
                g = rdf_serializer(json_nickel_data, json_nickel_sg, slip_configs, slip_plane_normals, example_uri, mat_id, sg_id)
                G = G+g

    G.serialize(destination='../data/MaterialProject/Nickel/overall.ttl', format='turtle')

if __name__ == "__main__":
    main()