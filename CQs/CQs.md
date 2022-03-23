## Competence Questions(CQs)
1. Which crystal structure share the same crystal system(e.g. Cubic, hexagonal, etc)?
2. What are the lattice parameters of length given a crystal structure?
3. What are the lattice parameters of angle given a crystal structure?
4. Given a crystal structure, what are the slip systems of it?
5. Given a crystal structure, what are the slip planes of it?
6. Given a slip plane of the crystal structure, what is the slip direction?
7. Given a 3-D vector instance (velocity, Burgers vector, vector position, etc), what are the vector components?
8. Given a 3-D vector instance (velocity, Burgers vector, vector position, etc), what is the vector magnitude?
9. Given a Basis of a vector in 3-D space, what are the first, second, and third axis vector?
10. Given a 3-D vector instance (velocity, Burgers vector, vector position, etc), what is the unit?


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
CQs 7:

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

CQs 8: 

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

CQs 9a: first axis basis
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

CQs 9b: second axis basis
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

CQs 9c: third axis basis
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

CQs 10: unit of Burgers vector 
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
		cso:hasVectorComponents ?VectorComponents ;
		qudt:hasQuantityKind ?quantity_kind ;
		qudt:quantityValue ?qv.
	?qv qudt:unit ?unit.
}

```