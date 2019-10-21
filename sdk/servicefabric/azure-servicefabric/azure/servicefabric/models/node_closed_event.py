# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .node_event import NodeEvent


class NodeClosedEvent(NodeEvent):
    """Node Closed event.

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param node_name: Required. The name of a Service Fabric node.
    :type node_name: str
    :param node_id: Required. Id of Node.
    :type node_id: str
    :param node_instance: Required. Id of Node instance.
    :type node_instance: long
    :param error: Required. Describes error.
    :type error: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'node_name': {'required': True},
        'node_id': {'required': True},
        'node_instance': {'required': True},
        'error': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'node_id': {'key': 'NodeId', 'type': 'str'},
        'node_instance': {'key': 'NodeInstance', 'type': 'long'},
        'error': {'key': 'Error', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NodeClosedEvent, self).__init__(**kwargs)
        self.node_id = kwargs.get('node_id', None)
        self.node_instance = kwargs.get('node_instance', None)
        self.error = kwargs.get('error', None)
        self.kind = 'NodeClosed'