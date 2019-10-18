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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AppPlatformManagementClientConfiguration
from .operations import ServicesTestOperations
from .operations import ServicesOperations
from .operations import AppsOperations
from .operations import BindingsOperations
from .operations import DeploymentsOperations
from .operations import Operations
from . import models


class AppPlatformManagementClient(SDKClient):
    """REST API for Azure Spring Cloud

    :ivar config: Configuration for client.
    :vartype config: AppPlatformManagementClientConfiguration

    :ivar services_test: ServicesTest operations
    :vartype services_test: azure.mgmt.appplatform.operations.ServicesTestOperations
    :ivar services: Services operations
    :vartype services: azure.mgmt.appplatform.operations.ServicesOperations
    :ivar apps: Apps operations
    :vartype apps: azure.mgmt.appplatform.operations.AppsOperations
    :ivar bindings: Bindings operations
    :vartype bindings: azure.mgmt.appplatform.operations.BindingsOperations
    :ivar deployments: Deployments operations
    :vartype deployments: azure.mgmt.appplatform.operations.DeploymentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.appplatform.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription ID which uniquely identify the
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AppPlatformManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AppPlatformManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-05-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.services_test = ServicesTestOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bindings = BindingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
