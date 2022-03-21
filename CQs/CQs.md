## Competence Questions(CQs)
1. Which crystal structure share the same crystal system(e.g. Cubic, hexagonal, etc)?
2. What are the lattice parameters of length given a crystal structure?
3. What are the lattice parameters of angle given a crystal structure?
4. Given a crystal structure, what are the slip systems of it?
5. Given a crystal structure, what are the slip planes of it?
6. Given a slip plane of the crystal structure, what is the slip direction?

## Answer to CQs via SPARQL

CQ1.1 Cubic crystal system:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
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

CQ1.2 Hexagonal crystal system:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
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
CQs. 2 Lattice parameter lengths:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
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

CQs. 3 Lattice parameter angles:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
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

CQs. 4:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?crystalstructure ?slip_system ?slip_plane_normal_val ?slip_direction_val WHERE{
	?crystalstructure a cso:CrystalStructure ; 
		diso:hasSlipSystem ?slip_system . 
	?slip_system diso:hasSlipPlaneNormal ?slip_plane_normal ; 
		diso:hasSlipDirection ?slip_direction.
	?slip_plane_normal diso:directionMillerIndice ?slip_plane_normal_val. 
	?slip_direction diso:directionMillerIndice ?slip_direction_val.
}
```

CQs. 5:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?crystal_structure ?slip_plane_val 
WHERE{
	?crystal_structure a cso:CrystalStructure.
	?crystal_structure diso:hasSlipPlane ?slip_plane.
	?slip_plane diso:planeMillerIndice ?slip_plane_val.
}
```
CQs 6 Slip direction of (111) plane:
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>  
PREFIX chebi: <http://purl.obolibrary.org/obo/> 
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX ns1: <http://purl.obolibrary.org/obo/chebi/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?slip_plane ?slip_direction_val WHERE{
	?slip_plane a diso:SlipPlane.
	?slip_plane diso:planeMillerIndice "(111)"^^xsd:string;
		diso:hasSlipDirection ?slip_direction. 
	?slip_direction diso:directionMillerIndice ?slip_direction_val.
}
```
