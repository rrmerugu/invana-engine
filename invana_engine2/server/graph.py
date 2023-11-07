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
from invana_engine2.invana import InvanaGraph

from invana_engine2.settings import gremlin_server_url, gremlin_traversal_source

graph = InvanaGraph(
    gremlin_server_url,
    # gremlin_server_username=gremlin_server_username,
    # gremlin_server_password=gremlin_server_password,
    traversal_source=gremlin_traversal_source
)