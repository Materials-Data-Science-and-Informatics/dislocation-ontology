from rdflib import Graph, Literal
from rdflib.namespace import  Namespace, RDF, XSD
import numpy as np


#crystal structure ontology
CSO = Namespace("https://purls.helmholtz-metadaten.de/cso#")
#dislocation ontology
DISO = Namespace("https://purls.helmholtz-metadaten.de/diso#")
#crystalline-defect-ontology
CDO = Namespace("https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystallographic-defect-ontology.owl#")
MDO = Namespace("https://w3id.org/mdo/structure/")
QUDT = Namespace("http://qudt.org/schema/qudt/")
QUDT_UNIT = Namespace("http://qudt.org/vocab/unit/")
QUDT_QK = Namespace("http://qudt.org/vocab/quantitykind/")


# function to serializing the cif into resource description framework(RDF) using the crystallography ontology
# returning graph object of rdflib
def rdf_serializer(cif_data, space_group_data, node_data, linker_data, loop_data, iri):
    example = Namespace(iri)
    g = Graph()
    # g.parse("../../crystal-structure-ontology.owl", format="xml")
    # g.parse("../../dislocation-ontology.owl", format="xml")
    g.parse("../../crystallographic-defect-ontology.owl", format="xml")

    g.bind("ex", example)
    g.bind("cdo", CDO)
    g.bind("diso", DISO)
    g.bind("cso", CSO)
    g.bind("mdo", MDO)
    g.bind("qudt", QUDT)
    g.bind("unit", QUDT_UNIT)
    g.bind("quantityKind", QUDT_QK)

    unit_of_length = 2.489e-10 # Burgers vector
    space_group_data = space_group_data['spacegroup'] # space group data
    
    # crystal structure data
    crystal = example['crystal']
    Bravais_lattice = example['Bravais_lattice']
    crystal_structure = example['crystal_structure']
    crystal_system = example['crystal_system']
    unit_cell = example['unit_cell']
    lattice_param_length = example['lattice_parameter_length']
    lattice_param_angle = example['lattice_parameter_angle']
    basis = example['coordinate_basis']
    crystal_coordinate_first_axis = example['crystal_coordinate_first_axis']
    crystal_coordinate_second_axis = example['crystal_coordinate_second_axis']
    crystal_coordinate_third_axis = example['crystal_coordinate_third_axis']
    space_group = example['space_group']
    point_group = example['point_group']
    
    ## length data value
    length_a = Literal(cif_data['_cell_length_a'], datatype=XSD.double) 
    length_b = Literal(cif_data['_cell_length_b'], datatype=XSD.double)
    length_c = Literal(cif_data['_cell_length_c'], datatype=XSD.double)
    
    ##angle data value
    angle_alpha = Literal(cif_data['_cell_angle_alpha'], datatype=XSD.double)  
    angle_beta =  Literal(cif_data['_cell_angle_beta'], datatype=XSD.double)
    angle_gamma = Literal(cif_data['_cell_angle_gamma'], datatype=XSD.double)

    # Crystal structure initial graph
    g.add((crystal, RDF.type, CDO.CrystallineMaterial))
    g.add((crystal, CDO.hasCrystalStructure, crystal_structure))
    g.add((crystal_structure, RDF.type, CSO.CrystalStructure))
    g.add((crystal_structure, CSO.hasLattice, Bravais_lattice))
    g.add((crystal_structure, MDO.hasSpaceGroup, space_group))
    g.add((space_group, RDF.type, MDO.SpaceGroup))
    g.add((space_group, MDO.SpaceGroupID, Literal(space_group_data['number'], datatype=XSD.integer)))
    g.add((space_group, MDO.SpaceGroupSymbol, Literal(space_group_data['symbol'], datatype=XSD.string)))
    g.add((space_group, MDO.hasPointGroup, point_group))
    g.add((point_group, RDF.type, MDO.PointGroup))
    g.add((point_group, MDO.PointGroupHMName, Literal(space_group_data['point_group'], datatype=XSD.string)))
    g.add((Bravais_lattice, RDF.type, CSO.BravaisLattice))
    g.add((Bravais_lattice, CSO.centering, Literal(space_group_data['symbol'][0], datatype=XSD.string)))
    g.add((Bravais_lattice, CSO.hasCrystalSystem, crystal_system))
    g.add((crystal_system, RDF.type, CSO[space_group_data['crystal_system'].capitalize()]))
    g.add((point_group, CSO.isPointGroupOf, crystal_system))
    g.add((Bravais_lattice, CSO.hasUnitCell, unit_cell))
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

    # basis of vector
    g.add((basis, RDF.type, MDO.Basis))
    g.add((basis, CSO.hasFirstAxisVector, crystal_coordinate_first_axis))
    g.add((crystal_coordinate_first_axis, RDF.type, MDO.CoordinateVector))
    g.add((crystal_coordinate_first_axis, MDO.X_axisCoordinate, Literal(1.0, datatype=XSD.double)))
    g.add((crystal_coordinate_first_axis, MDO.Y_axisCoordinate, Literal(0.0, datatype=XSD.double)))
    g.add((crystal_coordinate_first_axis, MDO.Z_axisCoordinate, Literal(0.0, datatype=XSD.double)))
    g.add((basis, CSO.hasSecondAxisVector, crystal_coordinate_second_axis))
    g.add((crystal_coordinate_second_axis, RDF.type, MDO.CoordinateVector))
    g.add((crystal_coordinate_second_axis, MDO.X_axisCoordinate, Literal(0.0, datatype=XSD.double)))
    g.add((crystal_coordinate_second_axis, MDO.Y_axisCoordinate, Literal(1.0, datatype=XSD.double)))
    g.add((crystal_coordinate_second_axis, MDO.Z_axisCoordinate, Literal(0.0, datatype=XSD.double)))
    g.add((basis, CSO.hasThirdAxisVector, crystal_coordinate_third_axis))
    g.add((crystal_coordinate_third_axis, RDF.type, MDO.CoordinateVector))
    g.add((crystal_coordinate_third_axis, MDO.X_axisCoordinate, Literal(0.0, datatype=XSD.double)))
    g.add((crystal_coordinate_third_axis, MDO.Y_axisCoordinate, Literal(0.0, datatype=XSD.double)))
    g.add((crystal_coordinate_third_axis, MDO.Z_axisCoordinate, Literal(1.0, datatype=XSD.double)))
    
    # dimensionless unit
    qv_unitless = example['quantity_value_unitless']
    g.add((qv_unitless, RDF.type, QUDT.QuantityValue))
    g.add((qv_unitless, QUDT.unit, QUDT_UNIT['UNITLESS']))

    # unit of length
    qv_m = example['quantity_value_M']
    g.add((qv_m, RDF.type, QUDT.QuantityValue))
    g.add((qv_m, QUDT.unit, QUDT_UNIT['M']))

    # dislocation node data
    for node in node_data:
        id = node['master_id']
        coordinate = node['coordinates']
        # n_v = node['velocity']
        node_individual = example['node_{}'.format(id)]
        node_position_vector = example['node_{}_position_vector'.format(id)]
        node_coordinate = example['node_{}_coordinate'.format(id)]
        # node_velocity = example['node_{}_velocity'.format(id)]
        # node_vector_velocity_components = example['node_{}_vector_velocity_components'.format(id)]

        g.add((node_individual, RDF.type, DISO.Node))
        g.add((node_individual, CSO.hasPositionVector, node_position_vector))
        g.add((node_position_vector, RDF.type, CSO.PositionVector))
        g.add((node_position_vector, CSO.hasVectorComponents, node_coordinate))
        g.add((node_coordinate, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((node_coordinate, QUDT.quantityValue, qv_m))
        g.add((node_coordinate, QUDT.hasQuantityKind, QUDT_QK.Length))
        g.add((node_coordinate, CSO.firstAxisComponent, Literal(coordinate[0]*unit_of_length, datatype=XSD.double)))
        g.add((node_coordinate, CSO.secondAxisComponent, Literal(coordinate[1]*unit_of_length, datatype=XSD.double)))
        g.add((node_coordinate, CSO.thirdAxisComponent, Literal(coordinate[2]*unit_of_length, datatype=XSD.double)))
        g.add((node_coordinate, CSO.hasBasis, basis))

        # g.add((node_individual, DISO.hasNodeVelocity, node_velocity))
        # g.add((node_velocity, RDF.type, DISO.NodeVelocity))
        # g.add((node_velocity, CSO.hasVectorComponents, node_vector_velocity_components))
        # g.add((node_vector_velocity_components, RDF.type, CSO.VectorComponentsOfBasis))
        # g.add((node_vector_velocity_components, QUDT.unit, QUDT_UNIT['M-PER-SEC']))
        # g.add((node_vector_velocity_components, QUDT.quantityKind, QUDT_QK.Velocity))
        # g.add((node_vector_velocity_components, CSO.firstAxisComponent, Literal(n_v[0], datatype=XSD.double)))
        # g.add((node_vector_velocity_components, CSO.secondAxisComponent, Literal(n_v[1], datatype=XSD.double)))
        # g.add((node_vector_velocity_components, CSO.thirdAxisComponent, Literal(n_v[2], datatype=XSD.double)))
        # g.add((node_vector_velocity_components, CSO.hasBasis, basis))
        

    slip_system_list = []
    counter_slip_system = 0 
    
    # dislocation loop data
    for loop in loop_data:
        id = loop['id']
        slip_direction_loop = loop['burgers_vector']
        plane_normal = loop['plane_normal']
        plane_origin = loop['plane_origin']
        slip_area = loop['slip_area']

        dislocation_loop = example['loop_{}'.format(id)]
        Burgers_vector = example['loop_{}_Burgers_vector'.format(id)]
        vector_components_Burgers_vector = example['loop_{}_vector_components_Burgers_vector'.format(id)]
        slip_plane = example['loop_{}_slip_plane'.format(id)]
        slip_direction = example['loop_{}_slip_direction'.format(id)]
        vector_components_slip_direction = example['loop_{}_vector_components_slip_direction'.format(id)]
        slip_plane_normal = example['loop_{}_slip_plane_normal'.format(id)]
        vector_components_of_slip_plane_normal = example['loop_{}_vector_components_of_slip_plane_normal'.format(id)]
        slip_plane_origin = example['loop_{}_slip_plane_origin'.format(id)]
        vector_components_slip_plane_origin = example['loop_{}_vector_components_origin'.format(id)]
        line = example['line_{}'.format(id)]
        discretized_line = example['loop_{}_discretized_line'.format(id)]
        pn, denum_pn  = plane_normal, min([abs(i) for i in plane_normal if i != 0])
        sd, denum_sd = slip_direction_loop, min([abs(i) for i in slip_direction_loop if i != 0])

        g.add((crystal, CDO.hasCrystallographicDefect, dislocation_loop))
        g.add((dislocation_loop, RDF.type, DISO.Dislocation))
        g.add((dislocation_loop, DISO.hasBurgersVector, Burgers_vector))
        g.add((dislocation_loop, DISO.movesOn, slip_plane))
        g.add((crystal_structure, DISO.hasSlipPlane, slip_plane))
        g.add((slip_plane, RDF.type, DISO.SlipPlane))
        g.add((slip_plane, DISO.hasSlipPlaneNormal, slip_plane_normal))
        plane_miller_indice = '({}{}{})'.format(int(pn[0]/denum_pn), int(pn[1]/denum_pn), int(pn[2]/denum_pn))
        family_plane_miller_indice = '{111}' # for cubic crystal system
        g.add((slip_plane, DISO.planeMillerIndice, Literal(plane_miller_indice, datatype=XSD.string)))
        g.add((slip_plane, DISO.familyPlaneMillerIndice, Literal(family_plane_miller_indice, datatype=XSD.string)))
        g.add((slip_plane, DISO.hasSlipDirection, slip_direction))
        g.add((slip_direction, RDF.type, DISO.SlipDirection))
        g.add((slip_direction, CSO.hasVectorComponents, vector_components_slip_direction))
        direction_miller_indice = '[{}{}{}]'.format(int(sd[0]/denum_sd), int(sd[1]/denum_sd), int(sd[2]/denum_sd))
        family_slip_direction_miller_indice = '<110>' # for cubic crystal system
        g.add((slip_direction, DISO.directionMillerIndice, Literal(direction_miller_indice, datatype=XSD.string)))
        g.add((slip_direction, DISO.familyDirectionMillerIndice, Literal(family_slip_direction_miller_indice, datatype=XSD.string)))
        g.add((vector_components_slip_direction, QUDT.quantityValue, qv_unitless))
        g.add((vector_components_slip_direction, QUDT.hasQuantityKind, QUDT_QK.Dimensionless))
        slip_direction_magnitude = np.linalg.norm(np.asanyarray(sd))
        g.add((slip_direction, CSO.vectorMagnitude, Literal(slip_direction_magnitude, datatype=XSD.double)))
        g.add((vector_components_slip_direction, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((vector_components_slip_direction, CSO.firstAxisComponent, Literal(sd[0], datatype=XSD.double)))
        g.add((vector_components_slip_direction, CSO.secondAxisComponent, Literal(sd[1], datatype=XSD.double)))
        g.add((vector_components_slip_direction, CSO.thirdAxisComponent, Literal(sd[2], datatype=XSD.double)))
        g.add((vector_components_slip_direction, CSO.hasBasis, basis))
        g.add((slip_plane_normal, RDF.type, DISO.SlipPlaneNormal))
        slip_plane_direction_miller_indice = '[{}{}{}]'.format(int(pn[0]/denum_pn), int(pn[1]/denum_pn), int(pn[2]/denum_pn))
        g.add((slip_plane_normal, DISO.directionMillerIndice, Literal(slip_plane_direction_miller_indice, datatype=XSD.string)))
        g.add((slip_plane_normal, CSO.hasVectorComponents, vector_components_of_slip_plane_normal))
        g.add((vector_components_of_slip_plane_normal, QUDT.quantityValue, qv_unitless))
        g.add((vector_components_of_slip_plane_normal, QUDT.hasQuantityKind, QUDT_QK.Dimensionless))
        g.add((vector_components_of_slip_plane_normal, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((vector_components_of_slip_plane_normal, CSO.firstAxisComponent, Literal(plane_normal[0], datatype=XSD.double)))
        g.add((vector_components_of_slip_plane_normal, CSO.secondAxisComponent, Literal(plane_normal[1], datatype=XSD.double)))
        g.add((vector_components_of_slip_plane_normal, CSO.thirdAxisComponent, Literal(plane_normal[2], datatype=XSD.double)))
        g.add((vector_components_of_slip_plane_normal, CSO.hasBasis, basis))
        g.add((slip_plane, DISO.hasOrigin, slip_plane_origin))
        g.add((slip_plane_origin, RDF.type, DISO.Origin))
        g.add((slip_plane_origin, CSO.hasVectorComponents, vector_components_slip_plane_origin))
        g.add((vector_components_slip_plane_origin, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((vector_components_slip_plane_origin, CSO.firstAxisComponent, Literal(plane_origin[0] * unit_of_length, datatype=XSD.double)))
        g.add((vector_components_slip_plane_origin, CSO.secondAxisComponent, Literal(plane_origin[1] * unit_of_length, datatype=XSD.double)))
        g.add((vector_components_slip_plane_origin, CSO.thirdAxisComponent, Literal(plane_origin[2] * unit_of_length, datatype=XSD.double)))
        g.add((vector_components_slip_plane_origin, CSO.hasBasis, basis))
        g.add((dislocation_loop, DISO.hasMathematicalRepresentation, line))
        g.add((line, RDF.type, DISO.Line))
        g.add((line, DISO.hasNumericalRepresentation, discretized_line))
        g.add((discretized_line, RDF.type, DISO.DiscretizedLine))
        g.add((discretized_line, DISO.slipArea, Literal(slip_area, datatype=XSD.double)))
        g.add((Burgers_vector, RDF.type, DISO.BurgersVector))
        g.add((Burgers_vector, CSO.hasVectorComponents, vector_components_Burgers_vector))
        g.add((vector_components_Burgers_vector, QUDT.quantityValue, qv_m))
        g.add((vector_components_Burgers_vector, QUDT.hasQuantityKind, QUDT_QK.Length))
        Burgers_vector_magnitude = unit_of_length
        g.add((Burgers_vector, CSO.vectorMagnitude, Literal(Burgers_vector_magnitude, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((vector_components_Burgers_vector, CSO.firstAxisComponent, Literal(slip_direction_loop[0] * unit_of_length, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, CSO.secondAxisComponent, Literal(slip_direction_loop[1]  * unit_of_length, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, CSO.thirdAxisComponent, Literal(slip_direction_loop[2] * unit_of_length, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, CSO.hasBasis, basis))

        # slip system data 
        _slip_system = '{}_{}'.format(slip_plane_direction_miller_indice, direction_miller_indice)
        if _slip_system not in slip_system_list:
            active_slip_system = example['active_slip_system_{}'.format(counter_slip_system)]
            g.add((crystal_structure, DISO.hasSlipSystem, active_slip_system))
            g.add((active_slip_system, RDF.type, DISO.SlipSystem))
            g.add((active_slip_system, DISO.hasSlipPlaneNormal, slip_plane_normal))
            g.add((active_slip_system, DISO.hasSlipDirection, slip_direction))
            slip_system_list.append(_slip_system)
            counter_slip_system +=1

    # segment/linker data
    for i, linker in enumerate(linker_data):
        segment = example['linker_{}'.format(i)]
        start_node_id = linker['start_node_id']
        end_node_id = linker['end_node_id']
        loop_id = linker['loop_id']
        g.add((segment, RDF.type, DISO.Segment))
        g.add((segment, DISO.hasStartNode, example['node_{}'.format(start_node_id)]))
        g.add((segment, DISO.hasEndNode, example['node_{}'.format(end_node_id)]))
        g.add((segment, DISO.isSegmentOf, example['loop_{}_discretized_line'.format(loop_id)]))
        
    return g