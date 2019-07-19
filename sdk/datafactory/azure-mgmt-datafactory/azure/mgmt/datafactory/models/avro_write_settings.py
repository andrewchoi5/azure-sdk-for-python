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

from .format_write_settings import FormatWriteSettings


class AvroWriteSettings(FormatWriteSettings):
    """Delimited text write settings.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param type: Required. The write setting type.
    :type type: str
    :param record_name: Top level record name in write result, which is
     required in AVRO spec.
    :type record_name: str
    :param record_namespace: Record namespace in the write result.
    :type record_namespace: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'record_name': {'key': 'recordName', 'type': 'str'},
        'record_namespace': {'key': 'recordNamespace', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AvroWriteSettings, self).__init__(**kwargs)
        self.record_name = kwargs.get('record_name', None)
        self.record_namespace = kwargs.get('record_namespace', None)