from rdflib import Graph, Literal
from rdflib.namespace import  Namespace, RDF, XSD


#crystal structure ontology
CSO = Namespace("https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#")
#dislocation ontology
DISO = Namespace("https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#")
#crystalline-defect-ontology
CDO = Namespace("https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystalline-defect-ontology.owl#")
MDO = Namespace("https://w3id.org/mdo/structure/")
CHEBI = Namespace("http://purl.obolibrary.org/obo/")
CHEBIdat = Namespace("http://purl.obolibrary.org/obo/chebi/")

# function to serializing the cif into resource description framework(RDF) using the crystallography ontology
# returning graph object of rdflib
def rdf_serializer(cif_dict, space_group_dict, slip_configs, slip_plane_normals, uri, mat_id, sg_id):
    #Material data URI
    example = Namespace(uri)
    
    lattice = example['{}_lattice'.format(mat_id)]
    crystal_structure = example['{}_crystal_strcture'.format(mat_id)]
    crystal_system = example['{}_crystal_system'.format(mat_id)]
    unit_cell = example['{}_unit_cell'.format(mat_id)]
    occupancy = example['{}_occupancy'.format(mat_id)]
    atom = example['{}_atom'.format(mat_id)]
    lattice_param_length = example['{}_lattice_parameter_length'.format(mat_id)]
    lattice_param_angle = example['{}_lattice_parameter_angle'.format(mat_id)]
    
    ## length data value
    length_a = Literal(cif_dict['_cell_length_a'], datatype=XSD.double) 
    length_b = Literal(cif_dict['_cell_length_b'], datatype=XSD.double)
    length_c = Literal(cif_dict['_cell_length_c'], datatype=XSD.double)
    
    ##angle data value
    angle_alpha = Literal(cif_dict['_cell_angle_alpha'], datatype=XSD.double)  
    angle_beta =  Literal(cif_dict['_cell_angle_beta'], datatype=XSD.double)
    angle_gamma = Literal(cif_dict['_cell_angle_gamma'], datatype=XSD.double)
    
    ## chemical structural formula
    dat_atom = Literal(cif_dict['_chemical_formula_structural'], datatype=XSD.string)
    
    g = Graph()
    g.parse("../../crystalline-defect-ontology.owl", format="xml")
    
    #binding alias for namespace in rdf graph
    g.bind("ex", example)
    g.bind("cdo", CDO)
    g.bind("diso", DISO)
    g.bind("cso", CSO)
    g.bind("mdo", MDO)
    g.bind("chebi", CHEBI)
    
    g.add((crystal_structure, RDF.type, CDO.CrystalStructure))
    g.add((crystal_structure,CSO.hasLattice, lattice))
    g.add((lattice, RDF.type, CSO.Lattice))
    g.add((lattice, CSO.hasCrystalSystem, crystal_system))
    g.add((lattice, CSO.hasUnitCell, unit_cell))
    g.add((unit_cell, RDF.type, CSO.UnitCell))
    g.add((unit_cell, CSO.hasLatticeParameterLength, lattice_param_length))
    g.add((unit_cell, CSO.hasLatticeParameterAngle, lattice_param_angle))
    g.add((lattice_param_length, RDF.type, CSO.LatticeParameterLength))
    g.add((lattice_param_angle, RDF.type, CSO.LatticeParameterAngle))
    g.add((lattice_param_length, CSO.latticeParameterLengthA , length_a))
    g.add((lattice_param_length, CSO.latticeParameterLengthB, length_b))
    g.add((lattice_param_length, CSO.latticeParameterLengthC, length_c))
    g.add((lattice_param_angle, CSO.latticeParameterAngleAlpha, angle_alpha))
    g.add((lattice_param_angle, CSO.latticeParameterAngleBeta, angle_beta))
    g.add((lattice_param_angle, CSO.latticeParameterAngleGamma, angle_gamma))
    
    #Occupancy
    for i in range(len(cif_dict['_atom_site_occupancy'])):
        occupancy=example['{}_occupancy_{}'.format(mat_id, i)]
        atom = example['{}_atom_{}'.format(mat_id,i)]
        site = example['{}_site_{}'.format(mat_id,i)]
        frac_coord = example['{}_frac_coord_{}'.format(mat_id,i)]
        g.add((crystal_structure, MDO.hasOccupancy, example['{}_occupancy_{}'.format(mat_id,i)]))
        g.add((example['{}_occupancy_{}'.format(mat_id,i)], RDF.type, MDO.Occupancy))
        g.add((example['{}_occupancy_{}'.format(mat_id,i)], MDO.hasSpecies, example['{}_species_{}'.format(mat_id,i)]))
        g.add((example['{}_species_{}'.format(mat_id,i)], RDF.type, MDO.Species))
        g.add((example['{}_species_{}'.format(mat_id,i)], MDO.hasElement, atom))
        g.add((atom, RDF.type, CHEBI.CHEBI_33250))
        g.add((atom, CHEBIdat.formula, dat_atom))
        g.add((occupancy, MDO.hasSite, site))
        g.add((site, RDF.type, MDO.Site))
        g.add((site, MDO.hasFractionalCoordinates, frac_coord))
        g.add((frac_coord, RDF.type, MDO.CoordinateVector))
        g.add((frac_coord, MDO.X_axisCoordinate, Literal(cif_dict['_atom_site_fract_x'][i], datatype=XSD.double)))
        g.add((frac_coord, MDO.Y_axisCoordinate, Literal(cif_dict['_atom_site_fract_y'][i], datatype=XSD.double)))
        g.add((frac_coord, MDO.Z_axisCoordinate, Literal(cif_dict['_atom_site_fract_z'][i], datatype=XSD.double))) 
    
    # add data about slip system, slip direction, slip      
    space_group_data = space_group_dict['spacegroup']
    g.add((crystal_system, RDF.type, CSO[space_group_data['crystal_system'].capitalize()]))
    sg_id= sg_id.split('_')[0] # remove spacegroup word
    if (space_group_data['crystal_system'].lower() == 'cubic') and (space_group_data['symbol'][0].lower() == 'f'):
        family_crystal_plane = example['{}_family_crystal_plane'.format(sg_id)]
        family_crystal_direction = example['{}_family_crystal_direction'.format(sg_id)]
        g.add((family_crystal_plane, RDF.type, DISO.FamilyOfCrystalPlane))
        g.add((family_crystal_plane, DISO.familyPlaneMillerIndice, Literal('{111}', datatype=XSD.string)))
        g.add((family_crystal_direction, RDF.type, DISO.FamilyOfCrystalDirection))
        g.add((family_crystal_direction, DISO.familyDirectionMillerIndice, Literal('<110>', datatype=XSD.string)))
    
        for (i, (key, list_item)) in enumerate(slip_configs.items()):
            g.add((crystal_structure, DISO.hasSlipPlane, example['{}_slip_plane_{}'.format(sg_id, i)]))
            g.add((example['{}_slip_plane_{}'.format(sg_id,i)], RDF.type, DISO.SlipPlane))
            g.add((example['{}_slip_plane_{}'.format(sg_id,i)], DISO.planeMillerIndice, Literal(key, datatype=XSD.string)))
            for (j, item) in enumerate(list_item):
                g.add((example['{}_slip_plane_{}_slip_direction_{}'.format(sg_id,i,j)], RDF.type, DISO.SlipDirection))
                g.add((example['{}_slip_plane_{}'.format(sg_id,i)], DISO.hasSlipDirection, example['{}_slip_plane_{}_slip_direction_{}'.format(sg_id,i,j)]))
                g.add((example['{}_slip_plane_{}_slip_direction_{}'.format(sg_id,i,j)], DISO.directionMillerIndice, Literal(item, datatype=XSD.string)))
    
        for (i, (key, list_item)) in enumerate(slip_plane_normals.items()):
            for item in list_item:
                g.add((example['{}_slip_plane_{}'.format(sg_id,i)], DISO.hasNormalVector, example['{}_slip_plane_normal_{}'.format(sg_id,i)]))
                g.add((example['{}_slip_plane_normal_{}'.format(sg_id,i)], RDF.type, DISO.SlipPlaneNormal))
                g.add((example['{}_slip_plane_normal_{}'.format(sg_id,i)], DISO.directionMillerIndice, Literal(item, datatype=XSD.string)))
    
        counter = 0
        for (i, (key, list_item)) in enumerate(slip_configs.items()):
            for (j, item) in enumerate(list_item):
                g.add((crystal_structure, DISO.hasSlipSystem, example['{}_slip_system_{}'.format(sg_id,counter)]))
                g.add((example['{}_slip_system_{}'.format(sg_id,counter)], RDF.type, DISO.SlipSystem))
                g.add((example['{}_slip_system_{}'.format(sg_id,counter)], DISO.hasSlipPlaneNormal, example['{}_slip_plane_normal_{}'.format(sg_id,i)]))
                g.add((example['{}_slip_system_{}'.format(sg_id,counter)], DISO.hasSlipDirection, example['{}_slip_plane_{}_slip_direction_{}'.format(sg_id,i,j)]))
                counter +=1

    return g