import graphene


def default_node_type_search_by_id_resolve_query(self, info: graphene.ResolveInfo, **kwargs):
    return []


def default_node_type_search_resolve_query(self, info: graphene.ResolveInfo, **kwargs):
    return []


def resolve_relationship_field_resolver(self, info: graphene.ResolveInfo, **kwargs):
    return []
