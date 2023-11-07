from invana_engine2.invana.base.querysets.schema  import SchemaWriterQuerySetBase
import logging

logger = logging.getLogger(__name__)


class GremlinSchemaWriterQuerySet(SchemaWriterQuerySetBase):
    from invana_engine2.invana.ogm.models import VertexModel, EdgeModel

    @staticmethod
    def create(model: [VertexModel, EdgeModel]):
        raise NotImplementedError("Not sure if gremlin has way to write schema ")