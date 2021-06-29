from .base import CRUDOperationsBase
from ..core.types import EdgeElement, VertexElement
from gremlin_python.process.graph_traversal import __
import logging

logger = logging.getLogger(__name__)


class EdgeOperations(CRUDOperationsBase):

    def get_or_create(self, label=None, properties=None):
        """

        :param label:
        :param namespace:
        :param properties: {"id": 123213 }
        :return:
        """

        edges = self.read_many(label=label,  query=properties)
        if edges.__len__() > 0:
            return edges[0]
        else:
            return self.create(label=label,  properties=properties)

    def create(self, label=None, properties=None, inv=None, outv=None):
        """

        :param label:
        :param namespace:
        :param properties:
        :param inv: str or VertexElement
        :param outv: str or VertexElement
        :return:
        """
        logger.debug("Creating Edge with label {label}, namespace and properties {properties}".format(
            label=label,
            
            properties=properties)
        )

        properties = {} if properties is None else properties

        _ = self.gremlin_client.g.V(inv).addE(label) \
            .to(__.V(outv))
        for property_key, property_value in properties.items():
            _.property(property_key, property_value)
        edg = _.elementMap().next()
        return EdgeElement(edg, serializer=self.serializer)

    def update(self, edg_id, properties=None):
        logger.debug("Updating vertex  {edg_id} with properties {properties}".format(edg_id=edg_id,
                                                                                     properties=properties, ))
        edge = self.filter_edge(edge_id=edg_id)
        properties = {} if properties is None else properties
        if edge:
            for k, v in properties.items():
                edge.property(k, v)
            _edge = edge.elementMap().next()
            return EdgeElement(_edge, serializer=self.serializer)
        return None

    def _read_one(self, edge_id):
        logger.debug("Finding edge with id {edge_id}".format(
            edge_id=edge_id))
        filtered_data = self.filter_edge(edge_id=edge_id)
        try:
            _ = filtered_data.elementMap().next()
            if _:
                return EdgeElement(_, serializer=self.serializer)
        except Exception as e:
            pass
        return None

    def _read_many(self, label=None, query=None, limit=10, skip=0):
        filtered_data = self.filter_edge(label=label,  query=query, limit=limit, skip=skip)
        cleaned_data = []
        for _ in filtered_data.elementMap().toList():
            cleaned_data.append(EdgeElement(_, serializer=self.serializer))
        return cleaned_data

    def filter_edge_and_get_neighbor_vertices(self, edge_id=None, label=None, query=None, limit=None,
                                              skip=None):
        cleaned_edges_data = self._read_many(label=label,  query=query, limit=limit, skip=skip)
        filtered_edges = self.filter_edge(label=label,  query=query, limit=limit, skip=skip)

        vertices_data = []
        for _ in filtered_edges.inV().dedup().elementMap().toList():
            vertices_data.append(VertexElement(_, serializer=self.serializer))

        filtered_edges = self.filter_edge(label=label,  query=query, limit=limit, skip=skip)

        for _ in filtered_edges.outV().dedup().elementMap().toList():
            vertices_data.append(VertexElement(_, serializer=self.serializer))
        vertices_data = list(set(vertices_data))

        return cleaned_edges_data + vertices_data

    def _delete_one(self, edge_id):
        logger.debug("Deleting the edge with edge_id:{edge_id}".format(edge_id=edge_id))
        self.drop(self.filter_edge(edge_id=edge_id))

    def _delete_many(self, label=None, query=None):
        logger.debug("Deleting the edges with label:{label} ,"
                     " query:{query}".format(label=label, query=query, ))
        self.drop(self.filter_edge(label=label,  query=query))
