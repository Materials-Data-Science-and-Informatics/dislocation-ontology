from rdflib import Graph, Literal
from rdflib.namespace import  Namespace, RDF, XSD
import numpy as np


#crystal structure ontology
CSO = Namespace("https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/crystal-structure-ontology.owl#")
#dislocation ontology
DISO = Namespace("https://raw.githubusercontent.com/Materials-Data-Science-and-Informatics/dislocation-ontology/master/dislocation-ontology.owl#")
#crystalline-defect-ontology
MDO = Namespace("https://w3id.org/mdo/structure/")
QUDT = Namespace("http://qudt.org/schema/qudt/")
QUDT_UNIT = Namespace("http://qudt.org/vocab/unit/")
QUDT_QK = Namespace("http://qudt.org/vocab/quantitykind/")


# function to serializing the cif into resource description framework(RDF) using the crystallography ontology
# returning graph object of rdflib
def rdf_serializer(node_data, linker_data, loop_data, iri):
    
    example = Namespace(iri)
    g = Graph()
    g.parse("../../crystal-structure-ontology.owl", format="xml")
    g.parse("../../dislocation-ontology.owl", format="xml")

    g.bind("ex", example)
    g.bind("diso", DISO)
    g.bind("cso", CSO)
    g.bind("mdo", MDO)
    g.bind("qudt", QUDT)
    g.bind("unit", QUDT_UNIT)
    g.bind("quantityKind", QUDT_QK)

    basis = example['coordinate_basis']
    crystal_coordinate_first_axis = example['crystal_coordinate_first_axis']
    crystal_coordinate_second_axis = example['crystal_coordinate_second_axis']
    crystal_coordinate_third_axis = example['crystal_coordinate_third_axis']
    unit = example['Unit']
    
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
        # still not quite sure what is the unit in modelib for node position
        # g.add((node_coordinate, QUDT.quantityValue, qv_m))
        # g.add((node_coordinate, QUDT.hasQuantityKind, QUDT_QK.Length))
        g.add((node_coordinate, CSO.firstAxisComponent, Literal(coordinate[0], datatype=XSD.double)))
        g.add((node_coordinate, CSO.secondAxisComponent, Literal(coordinate[1], datatype=XSD.double)))
        g.add((node_coordinate, CSO.thirdAxisComponent, Literal(coordinate[2], datatype=XSD.double)))
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
        
    # dimensionless unit
    qv_unitless = example['quantity_value_unitless']
    g.add((qv_unitless, RDF.type, QUDT.QuantityValue))
    g.add((qv_unitless, QUDT.unit, QUDT_UNIT['UNITLESS']))

    # unit of length
    qv_m = example['quantity_value_M']
    g.add((qv_m, RDF.type, QUDT.QuantityValue))
    g.add((qv_m, QUDT.unit, QUDT_UNIT['M']))
    
    for loop in loop_data:
        id = loop['id']
        Burgers_vec = loop['burgers_vector']
        plane_normal = loop['plane_normal']
        plane_origin = loop['plane_origin']
        slip_area = loop['slip_area']

        loop = example['loop_{}'.format(id)]
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
        bv, denum_bv = Burgers_vec, min([abs(i) for i in Burgers_vec if i != 0])
        g.add((loop, RDF.type, DISO.Dislocation))
        g.add((loop, DISO.hasBurgersVector, Burgers_vector))
        g.add((loop, DISO.movesOn, slip_plane))
        g.add((slip_plane, RDF.type, DISO.SlipPlane))
        g.add((slip_plane, DISO.hasSlipPlaneNormal, slip_plane_normal))
        plane_miller_indice = '({}{}{})'.format(int(pn[0]/denum_pn), int(pn[1]/denum_pn), int(pn[2]/denum_pn))
        g.add((slip_plane, DISO.planeMillerIndice, Literal(plane_miller_indice, datatype=XSD.string)))
        g.add((slip_plane, DISO.hasSlipDirection, slip_direction))
        g.add((slip_direction, RDF.type, DISO.slip_direction))
        g.add((slip_direction, CSO.hasVectorComponents, vector_components_slip_direction))
        direction_miller_indice = '[{}{}{}]'.format(int(bv[0]/denum_bv), int(bv[1]/denum_bv), int(bv[2]/denum_bv))
        g.add((slip_direction, DISO.directionMillerIndice, Literal(direction_miller_indice, datatype=XSD.string)))
        g.add((vector_components_slip_direction, QUDT.quantityValue, qv_unitless))
        g.add((vector_components_slip_direction, QUDT.hasQuantityKind, QUDT_QK.Dimensionless))
        slip_direction_magnitude = np.linalg.norm(np.asanyarray(bv))
        g.add((slip_direction, CSO.vectorMagnitude, Literal(slip_direction_magnitude, datatype=XSD.double)))
        g.add((vector_components_slip_direction, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((vector_components_slip_direction, CSO.firstAxisComponent, Literal(bv[0], datatype=XSD.double)))
        g.add((vector_components_slip_direction, CSO.secondAxisComponent, Literal(bv[1], datatype=XSD.double)))
        g.add((vector_components_slip_direction, CSO.thirdAxisComponent, Literal(bv[2], datatype=XSD.double)))
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
        g.add((vector_components_slip_plane_origin, CSO.firstAxisComponent, Literal(plane_origin[0], datatype=XSD.double)))
        g.add((vector_components_slip_plane_origin, CSO.secondAxisComponent, Literal(plane_origin[1], datatype=XSD.double)))
        g.add((vector_components_slip_plane_origin, CSO.thirdAxisComponent, Literal(plane_origin[2], datatype=XSD.double)))
        g.add((vector_components_slip_plane_origin, CSO.hasBasis, basis))
        g.add((loop, DISO.hasMathematicalRepresentation, line))
        g.add((line, RDF.type, DISO.Line))
        g.add((line, DISO.hasNumericalRepresentation, discretized_line))
        g.add((discretized_line, RDF.type, DISO.DiscretizedLine))
        g.add((discretized_line, DISO.slipArea, Literal(slip_area, datatype=XSD.double)))
        g.add((Burgers_vector, RDF.type, DISO.BurgersVector))
        g.add((Burgers_vector, CSO.hasVectorComponents, vector_components_Burgers_vector))
        g.add((vector_components_Burgers_vector, QUDT.quantityValue, qv_m))
        g.add((Burgers_vector, QUDT.hasQuantityKind, QUDT_QK.Length))
        Burgers_vector_magnitude = np.linalg.norm(3.3e-10 * np.asanyarray(bv))
        g.add((Burgers_vector, CSO.vectorMagnitude, Literal(Burgers_vector_magnitude, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, RDF.type, CSO.VectorComponentsOfBasis))
        g.add((vector_components_Burgers_vector, CSO.firstAxisComponent, Literal(Burgers_vec[0] * 3.3e-10, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, CSO.secondAxisComponent, Literal(Burgers_vec[1]  * 3.3e-10, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, CSO.thirdAxisComponent, Literal(Burgers_vec[2] * 3.3e-10, datatype=XSD.double)))
        g.add((vector_components_Burgers_vector, CSO.hasBasis, basis))

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