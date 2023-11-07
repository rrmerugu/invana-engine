import graphene
from ..utils import get_client_info, get_host
import socket


class BackendBasicInfoType(graphene.ObjectType):
    connection_uri = graphene.String()
    backend_class = graphene.String()
    is_readonly = graphene.Boolean()
    default_query_language = graphene.String()
    supported_query_languages = graphene.List(graphene.String)

class ClientInfoType(graphene.ObjectType):
    host = graphene.String()
    host_ip_address = graphene.String()

    # def resolve_host(self, info):
    #     return socket.gethostname()
 
    # def resolve_host_ip_address(self, info):
    #     return socket.gethostbyname(socket.gethostname())
 

class BasicInfoType(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))
    client = graphene.Field(ClientInfoType)
    backend = graphene.Field(BackendBasicInfoType)

    def resolve_hello(self, info, name):
        return name
    
    def resolve_client(self, info):
        return {
            "host": socket.gethostname(),
            "host_ip_address": socket.gethostbyname(socket.gethostname())
        }
    
    def resolve_backend(self, info):
        return info.context['request'].app.state.graph.backend.get_basic_info()