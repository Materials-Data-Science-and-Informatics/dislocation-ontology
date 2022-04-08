## Competence Questions(CQs)

1. Which crystal structure share the same crystal system(e.g. Cubic, hexagonal, etc)?
2. What are the lattice parameters of length given a crystal structure?
3. What are the lattice parameters of angle given a crystal structure?
4. Given the space group of a crystal structure, what is the bravais lattice centering?
5. Given the crystal structure, what are the corresponding space group and point group?
6. Given the point group of a crystal structure, what is the corresponding crystal system?


## Answer to CQs via SPARQL

CQ1.1: Which crystal structure share the same cubic crystal system?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?crystalstructure ?crystal_system WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasCrystalSystem ?crystal_system.
	?crystal_system a cso:Cubic .
}
```

CQ1.2: Which crystal structure share the same hexagonal crystal system?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?crystalstructure ?crystal_system WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasCrystalSystem ?crystal_system.
	?crystal_system a cso:Hexagonal .
}
```
CQs. 2: What are the lattice parameters of length given a crystal structure? 
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?crystalstructure ?length_a ?length_b ?length_c WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasUnitCell ?unitcell .
	?unitcell cso:hasLatticeParameterLength ?latticeParameterLength.  
	?latticeParameterLength cso:latticeParameterLengthA ?length_a;
		cso:latticeParameterLengthB ?length_b;
		cso:latticeParameterLengthC ?length_c.
}
```

CQs. 3: What are the lattice parameters of angle given a crystal structure?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?crystalstructure ?angle_alpha ?angle_beta ?angle_gamma WHERE{
	?crystalstructure a cso:CrystalStructure ; cso:hasLattice ?lattice .
	?lattice cso:hasUnitCell ?unitcell .
	?unitcell cso:hasLatticeParameterAngle ?latticeParameterAngle.
	?latticeParameterAngle cso:latticeParameterAngleAlpha ?angle_alpha;  
		cso:latticeParameterAngleBeta ?angle_beta;
		cso:latticeParameterAngleGamma ?angle_gamma.
}
```

CQs 4: Given the space group of a crystal structure, what is the bravais lattice centering?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>   
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?crystal_structure ?centering WHERE{
	?crystal_structure a cso:CrystalStructure;
		cso:hasLattice ?bravais_lattice . 
	?bravais_lattice cso:centering ?centering . 
}
```

CQs 5: Given the crystal structure, what are the corresponding space group and point group?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>   
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?crystal_structure ?space_group ?point_group WHERE{
	?crystal_structure a cso:CrystalStructure;
		mdo:hasSpaceGroup ?sg.
	?sg mdo:hasPointGroup ?pg ;
	 	mdo:SpaceGroupSymbol ?space_group . 
	?pg mdo:PointGroupHMName ?point_group .
}
```

CQs 6a : Given the point group of a crystal structure, what is the corresponding crystal system, e.g. Cubic?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>   
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?point_group ?crystal_system WHERE{
	?pg a mdo:PointGroup;
	mdo:PointGroupHMName ?point_group ;
		cso:isPointGroupOf ?crystal_system.
	?crystal_system rdf:type cso:Cubic.
}
```

CQs 6b : Given the point group of a crystal structure, what is the corresponding crystal system, e.g. Hexagonal?
```
PREFIX diso: <https://purls.helmholtz-metadaten.de/diso#>
PREFIX cso: <https://purls.helmholtz-metadaten.de/cso#> 
PREFIX cdo: <https://purls.helmholtz-metadaten.de/cdo#>   
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?point_group ?crystal_system WHERE{
	?pg a mdo:PointGroup;
	mdo:PointGroupHMName ?point_group ;
		cso:isPointGroupOf ?crystal_system.
	?crystal_system rdf:type cso:Hexagonal.
}
```