### Dislocation Ontology (DISO)

DISO is an ontology that defines the linear defect concepts and relations in crystalline materials. Moreover, Crystal Structure Ontology (CSO) and Crystallographic Defect Ontology (CDO), which ontologies define the concepts of crystal structureand crystalline defect, respectively, are also introduced in this repository. The ontology development processes are described following the well-known practices, e.g., using ontology metadata and reusing existing  ontologies,  e.g.,  MDO,  EMMO,  and  QUDT. To evaluate DISO, we have gathered competency questions (CQs) that will be answered via SPARQL query.

### Project Structure
* [data](/data/)
    * [Dislocation microstructure of nickel material](/data/modelib-microstructure/modelib-nickel-microstructure.ttl)
    This is the simulation data of dislocation microstructure of nickel (Ni) material generated by [MoDELib](https://github.com/giacomo-po/MoDELib)
* [CQs](/CQs/CQs.md) is a collection of the competence questions.
* [RDF genererator](/python-script/)
    * For generating the RDF graph from the given [data](/data/), we use the [RDFLib](https://github.com/RDFLib/rdflib) python library.
    * To generate the nickel crystal structure, the script is in [here](/python-script/MaterialProject/) and `python map_data.py`
    * To generate the dislocation microstructure of nickel material, the script is in [here](/python-script/modelib/) and `python map_data.py`
* [CSO](/crystal-structure-ontology) is a folder containing the details of crystal structure ontology.
* [CDO](/crystallographic-defect-ontology) is  folder containing the details of crystallographic defect ontology.

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
