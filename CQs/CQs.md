## Competence Questions(CQs)
1. Which crystal structure share the same crystal system(e.g. Cubic, hexagonal, etc)?
2. What are the lattice parameters of length given a crystal structure?
3. What are the lattice parameters of angle given a crystal structure?
4. What are the slip systems of a given crystal structure?
5. What are the slip planes of a given crystal structure?
6. What is the family of slip plane given a slip plane in the crystal?
7. What is the  family of slip direction given a slip direction in the crystal?
8. In which slip plane is the dislocation moves on?
9. What is the Burgers vector of the dislocation?
10. What is the Burgers vector magnitude of the dislocation?
11. Given a slip plane of the crystal structure, what is the slip direction?
12. Given a 3-D vector instance (Burgers vector, vector position, etc), what are the vector components?
13. Given a 3-D vector instance ( Burgers vector, vector position, etc), what is the vector magnitude?
14. Given a Basis of a vector in 3-D space, what are the first, second, and third axis vector?
15. Given a 3-D vector instance (Burgers vector, vector position, etc), what is the unit?
16. Given the space group of a crystal structure, what is the bravais lattice centering?
17. Given the crystal structure, what are the corresponding space group and point group?
18. Given the point group of a crystal structure, what is the corresponding crystal system?


## Answer to CQs via SPARQL

CQ1.1: Which crystal structure share the same cubic crystal system?
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

CQ1.2: Which crystal structure share the same hexagonal crystal system?
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
CQs. 2: What are the lattice parameters of length given a crystal structure? 
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

CQs. 3: What are the lattice parameters of angle given a crystal structure?
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

CQs. 4: What are the slip systems of a given crystal structure?
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

CQs. 5: What are the slip planes of a given crystal structure?
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

SELECT  ?crystal_structure ?slip_plane ?slip_plane_miller_indice 
WHERE{
	?crystal_structure a cso:CrystalStructure.
	?crystal_structure diso:hasSlipPlane ?slip_plane.
	?slip_plane diso:planeMillerIndice ?slip_plane_miller_indice .
}
```

CQs. 6: What is the family of slip plane given a slip plane in the crystal?
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

SELECT  ?slip_plane ?slip_plane_miller_indice ?family_of_slip_plane_miller_indice
WHERE{
	?slip_plane a diso:SlipPlane ; 
		diso:planeMillerIndice ?slip_plane_miller_indice ; 
		diso:familyPlaneMillerIndice ?family_of_slip_plane_miller_indice .
	
}
```

CQs. 7: What is the  family of slip direction given a slip direction in the crystal?
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

SELECT  ?slip_direction ?slip_direction_miller_indice ?family_of_slip_direction_miller_indice
WHERE{
	?slip_direction a diso:SlipDirection ; 
		diso:directionMillerIndice ?slip_direction_miller_indice ; 
		diso:familyDirectionMillerIndice ?family_of_slip_direction_miller_indice .
	
}
```

CQs. 8: In which slip plane is the dislocation moves on?
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

SELECT  ?dislocation ?slip_plane ?slip_plane_miller_indice
WHERE{
	?dislocation a diso:Dislocation ; 
		diso:movesOn ?slip_plane . 
	?slip_plane diso:planeMillerIndice ?slip_plane_miller_indice . 
}
```
CQs. 9: What is the Burgers vector of the dislocation?
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

SELECT ?dislocation ?firstAxisComponent ?secondAxisComponent ?thirdAxisComponent  WHERE{
	?dislocation a diso:Dislocation . 
	?dislocation diso:hasBurgersVector ?Burgers_vector.
	?Burgers_vector	cso:hasVectorComponents ?VectorComponentsOfBasis .
	?VectorComponentsOfBasis cso:firstAxisComponent ?firstAxisComponent;
		cso:secondAxisComponent ?secondAxisComponent;
		cso:thirdAxisComponent ?thirdAxisComponent .
}
```
CQs. 10: What is the Burgers vector magnitude of the dislocation?
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
SELECT ?dislocation ?Burgers_vector_magnitude  WHERE{
	?dislocation a diso:Dislocation . 
	?dislocation diso:hasBurgersVector ?Burgers_vector.
	?Burgers_vector cso:vectorMagnitude ?Burgers_vector_magnitude .
}
```
CQs 11: Given a slip plane of the crystal structure, what is the slip direction?
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
CQs 12: Given a 3-D vector instance (Burgers vector, vector position, etc), what are the vector components?

```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?Burgers_vector ?firstAxisComponent ?secondAxisComponent ?thirdAxisComponent WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponents ?VectorComponentsOfBasis .
	?VectorComponentsOfBasis cso:firstAxisComponent ?firstAxisComponent;
		cso:secondAxisComponent ?secondAxisComponent;
		cso:thirdAxisComponent ?thirdAxisComponent .
}
```

CQs 13: Given a 3-D vector instance ( Burgers vector, vector position, etc), what is the vector magnitude?

```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?Burgers_vector ?vectorMagnitude WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:vectorMagnitude ?vectorMagnitude .
}
```

CQs 14a: first axis basis
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?Burgers_vector ?first_axis_basis_e_x ?first_axis_basis_e_y ?first_axis_basis_e_z WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponents ?VectorComponents . 
	?VectorComponents cso:hasBasis ?Basis .
	?Basis cso:hasFirstAxisVector ?CoordinateVector .
	?CoordinateVector mdo:X_axisCoordinate ?first_axis_basis_e_x;
		mdo:Y_axisCoordinate ?first_axis_basis_e_y;
		mdo:Z_axisCoordinate ?first_axis_basis_e_z . 
}
```

CQs 14b: second axis basis
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?Burgers_vector ?second_axis_basis_e_x ?second_axis_basis_e_y ?second_axis_basis_e_z WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponents ?VectorComponents . 
	?VectorComponents cso:hasBasis ?Basis .
	?Basis cso:hasSecondAxisVector ?CoordinateVector .
	?CoordinateVector mdo:X_axisCoordinate ?second_axis_basis_e_x;
		mdo:Y_axisCoordinate ?second_axis_basis_e_y;
		mdo:Z_axisCoordinate ?second_axis_basis_e_z . 
}
```

CQs 14c: third axis basis
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?Burgers_vector ?third_axis_basis_e_x ?third_axis_basis_e_y ?third_axis_basis_e_z WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponents ?VectorComponents . 
	?VectorComponents cso:hasBasis ?Basis .
	?Basis cso:hasThirdAxisVector ?CoordinateVector .
	?CoordinateVector mdo:X_axisCoordinate ?third_axis_basis_e_x;
		mdo:Y_axisCoordinate ?third_axis_basis_e_y;
		mdo:Z_axisCoordinate ?third_axis_basis_e_z . 
}
```

CQs 15: Given a 3-D vector instance (Burgers vector, vector position, etc), what is the unit?
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?Burgers_vector ?unit ?quantity_kind WHERE{
	?Burgers_vector a diso:BurgersVector;
		cso:hasVectorComponents ?VectorComponents .
	?VectorComponents qudt:hasQuantityKind ?quantity_kind ;
		qudt:quantityValue ?qv.
	?qv qudt:unit ?unit.
}
```

CQs 16: Given the space group of a crystal structure, what is the bravais lattice centering?
```
PREFIX diso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#>
PREFIX cso: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#> 
PREFIX cdo: <https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#>   
PREFIX qudt: <http://qudt.org/schema/qudt/>
PREFIX mdo: <https://w3id.org/mdo/structure/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT  ?crystal_structure ?centering WHERE{
	?crystal_structure a cso:CrystalStructure;
		cso:hasLattice ?bravais_lattice;
	?bravais_lattice cso:centering ?centering
}
```