#  Copyright 2021 Invana
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#  http:www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from starlette.applications import Starlette
import logging
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route, WebSocketRoute
from .views import HomePageView, GremlinQueryView
from invana_engine.settings import GRAPH_BACKEND, DEBUG, GRAPH_BACKEND_URL,  \
    GRAPH_BACKEND_GREMLIN_TRAVERSAL_SOURCE, SERVER_PORT
from starlette_graphene3 import GraphQLApp
from invana_engine.graphql.graphiql.handler import make_graphiql_handler
# from invana_engine.graphql.schema import get_schema
from ..settings import __VERSION__, __AUTHOR_NAME__, __AUTHOR_EMAIL__
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from ariadne.asgi import GraphQL
from ..graphql.schema_generators import GrapheneGraphQLSchemaGenerator, AriadneGraphQLSchemaGenerator
from invana_engine.connector.graph import InvanaGraph
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.getLogger('neo4j').setLevel(logging.INFO)

logger = logging.getLogger(__name__)


def welcome():
    logger.info(f"""
██ ███    ██ ██    ██  █████  ███    ██  █████      ███████ ███    ██  ██████  ██ ███    ██ ███████ 
██ ████   ██ ██    ██ ██   ██ ████   ██ ██   ██     ██      ████   ██ ██       ██ ████   ██ ██      
██ ██ ██  ██ ██    ██ ███████ ██ ██  ██ ███████     █████   ██ ██  ██ ██   ███ ██ ██ ██  ██ █████   
██ ██  ██ ██  ██  ██  ██   ██ ██  ██ ██ ██   ██     ██      ██  ██ ██ ██    ██ ██ ██  ██ ██ ██      
██ ██   ████   ████   ██   ██ ██   ████ ██   ██     ███████ ██   ████  ██████  ██ ██   ████ ███████
{__VERSION__} version ; {__AUTHOR_NAME__}({__AUTHOR_EMAIL__})""")
    logger.info(".................................................")
    logger.info(f"Starting Invana Engine server at 0.0.0.0:{SERVER_PORT}")
    logger.info(f"Using GRAPH_BACKEND_URL: {GRAPH_BACKEND_URL}")
    logger.info(f"Using GRAPH_BACKEND: {GRAPH_BACKEND}")
    logger.info(f"Using DEBUG: {DEBUG}")
    logger.info(".................................................")


welcome()

if GRAPH_BACKEND_URL is None:
    logger.error("ERROR: GRAPH_BACKEND_URL environment variable not set. Please fix it .")
    logger.error(
        "Exiting the program now. Please refer the documentation at https://github.com/invana/invana-engine")
    exit()


def create_app():

    routes = [
        Route('/', endpoint=HomePageView),
        WebSocketRoute('/gremlin', GremlinQueryView),
        Mount('/static', app=StaticFiles(packages=[('invana_engine.graphql.graphiql', 'static')]), name="static"),
    ]

    middleware = [
        Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=["GET", "POST", "PUT", "DELETE"])
    ]

    app = Starlette(routes=routes, middleware=middleware, debug=DEBUG)

    # schema = Query  # , mutation=Mutation, subscription=Subscription)

    schema =  GrapheneGraphQLSchemaGenerator().get_schema()

    # app.mount("/graph", GraphQLApp(schema, on_get=make_graphiql_handler()))  # starlette graphql 

    # from ariadne import QueryType, make_executable_schema
    # from ariadne.asgi import GraphQL
    # type_defs = """
    #     type Query {
    #         hello: String!
    #     }
    # """

    # query = QueryType()


    # @query.field("hello")
    # def resolve_hello(*_):
    #     return "Hello world!"


    # # Create executable schema instance
    # schema = make_executable_schema(type_defs, query)
    import asyncio
    from ariadne.asgi.handlers import GraphQLTransportWSHandler
    from ariadne import SubscriptionType, make_executable_schema
    type_def = """
        type Query {
            _unused: Boolean
        }

        type Subscription {
            counter: Int!
        }
    """

    subscription = SubscriptionType()

    @subscription.source("counter")
    async def counter_generator(obj, info):
        for i in range(50):
            await asyncio.sleep(1)
            yield i


    @subscription.field("counter")
    def counter_resolver(count, info):
        return count + 1
    schema = AriadneGraphQLSchemaGenerator().get_schema(type_def, subscription)


    # app.mount("/graph", GraphQL(schema.graphql_schema, debug=True ))  # Graphiql IDE
    app.mount("/graph", GraphQL(schema, debug=True,
                                websocket_handler=GraphQLTransportWSHandler(),
                                 ))  # Graphiql IDE

    app.state.graph = InvanaGraph(GRAPH_BACKEND)
    return app

app = create_app()