### Dislocation Ontology
This repository shows the initial development of dislocation ontology. This study is submitted to Second International Workshop On Semantic Digital Twins (SeDiT 2021), June 6th, 2021.

In this work, first steps towards formalizing the knowledge of dislocations together with the relevant details concerning the crystallography are introduced. Emphasis is put on representing the dislocation geometry, utilizing semantic formalization using an ontology. We start by designing and modeling a formal definition of crystalline materials in terms of the underlying crystallography including slip plane and slip direction. The former is the plane to which the motion of the dislocation is generally constrained, the latter is the direction along which plastic deformation takes place. Those should be explicitly described along with the idealization of dislocation as a mathematical line and other required details of crystalline materials.

### Project Structure
* `data`
    * `MaterialProject/Nickel` 
    The Nickel data is collected from [Materials Project](https://materialsproject.org)
    * Slip system data of FCC Nickel is taken from [the Crystallography and Crystal Defects book](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119961468)
* `CQs` is a folder for storing the collection of the competence questions.

### Acknowledgments
* European Research Council through the ERC Grant Agreement No. 759419 MuDiLingo (”A Multiscale Dislocation Language for Data-Driven Materials Science”)
* Helmholtz Metadata Collaboration (HMC) within the Hub Information at the Forschungszentrum Jülich.


### Citation 
please cite the following paper if you used any part of this work. 

`@inproceedings{
ihsan2021steps,
title={Steps towards a Dislocation Ontology for Crystalline Materials},
author={Ahmad Zainul Ihsan and Danilo Dessì and Mehwish Alam and Harald Sack and Stefan Sandfeld},
booktitle={Second International Workshop on Semantic Digital Twins },
year={2021},
url={http://ceur-ws.org/Vol-2887/paper4.pdf}
}`
