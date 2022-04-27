### Crystal Structure Ontology

Crystal Structure Ontology (CSO) is an ontology developed to represent crystallographic information needed to describe the dislocation. In CSO, several MDO classes are reused to describe the crystal coordinate system, motif/base in a crystal structure, point groups, and space groups. 
The standard coordinate system is defined by `MDO:Basis` and `MDO:CoordinateVector` classes that CSO reuses. 
The motif/base is an arrangement of chemical species in the crystal structure reuses `MDO:Occupancy`, `MDO:Site`, and `MDO:Species`. 
Subsequently, to define the point groups and space groups of a crystal structure, `MDO:PointGroup` and `MDO:SpaceGroup` are reused. Lastly, to define the unit quantity of a property in CSO, the `QUDT:Quantity`, `QUDT:QuantityKind`, and `QUDT:QuantityValue` classes are reused.
![CSO-classes-2](https://user-images.githubusercontent.com/71790028/165483629-0f66d3a9-cde7-4a35-a7b5-17d35429df02.png)


### Project Structure
* [data](/crystal-structure-ontology/data/)
    * [Nickel crystal structure](/crystal-structure-ontology/data/MaterialProject/Nickel/overall.ttl) 
    The Nickel data is collected from [Materials Project](https://materialsproject.org) 
* [CQs](/crystal-structure-ontology/CQs.md) is a collection of the competence questions.
* [RDF genererator](/crystal-structure-ontology/python-script/)
    * For generating the RDF graph from the given [data](/crystal-structure-ontology/data/), we use the [RDFLib](https://github.com/RDFLib/rdflib) python library.
    * To generate the nickel crystal structure, the script is in [here](/crystal-structure-ontology/python-script/) and execute with `python map_data.py`

### Acknowledgments
* European Research Council through the ERC Grant Agreement No. 759419 MuDiLingo (”A Multiscale Dislocation Language for Data-Driven Materials Science”)
* Helmholtz Metadata Collaboration (HMC) within the Hub Information at the Forschungszentrum Jülich.


### Citation 
please cite the following paper if you used any part of this work. 

`@inproceedings{ihsan2021steps,
title={Steps towards a Dislocation Ontology for Crystalline Materials},
author={Ahmad Zainul Ihsan and Danilo Dessì and Mehwish Alam and Harald Sack and Stefan Sandfeld},
booktitle={Second International Workshop on Semantic Digital Twins },
year={2021},
url={http://ceur-ws.org/Vol-2887/paper4.pdf}}`
