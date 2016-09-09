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

from msrest.serialization import Model


class GatewayProfile(Model):
    """JSON properties that the gateway service uses know how to communicate with
    the resource.

    :param data_plane_service_base_address: the Dataplane connection URL
    :type data_plane_service_base_address: str
    :param gateway_id: the ID of the gateway
    :type gateway_id: str
    :param environment: the environment for the gateway (DEV, DogFood, or
     Production)
    :type environment: str
    :param upgrade_manifest_url: Gateway upgrade manifest URL
    :type upgrade_manifest_url: str
    :param messaging_namespace: Messaging namespace
    :type messaging_namespace: str
    :param messaging_account: Messaging Account
    :type messaging_account: str
    :param messaging_key: Messaging Key
    :type messaging_key: str
    :param request_queue: Request queue name
    :type request_queue: str
    :param response_topic: Response topic name
    :type response_topic: str
    :param status_blob_signature: The gateway status blob SAS url
    :type status_blob_signature: str
    """ 

    _attribute_map = {
        'data_plane_service_base_address': {'key': 'dataPlaneServiceBaseAddress', 'type': 'str'},
        'gateway_id': {'key': 'gatewayId', 'type': 'str'},
        'environment': {'key': 'environment', 'type': 'str'},
        'upgrade_manifest_url': {'key': 'upgradeManifestUrl', 'type': 'str'},
        'messaging_namespace': {'key': 'messagingNamespace', 'type': 'str'},
        'messaging_account': {'key': 'messagingAccount', 'type': 'str'},
        'messaging_key': {'key': 'messagingKey', 'type': 'str'},
        'request_queue': {'key': 'requestQueue', 'type': 'str'},
        'response_topic': {'key': 'responseTopic', 'type': 'str'},
        'status_blob_signature': {'key': 'statusBlobSignature', 'type': 'str'},
    }

    def __init__(self, data_plane_service_base_address=None, gateway_id=None, environment=None, upgrade_manifest_url=None, messaging_namespace=None, messaging_account=None, messaging_key=None, request_queue=None, response_topic=None, status_blob_signature=None):
        self.data_plane_service_base_address = data_plane_service_base_address
        self.gateway_id = gateway_id
        self.environment = environment
        self.upgrade_manifest_url = upgrade_manifest_url
        self.messaging_namespace = messaging_namespace
        self.messaging_account = messaging_account
        self.messaging_key = messaging_key
        self.request_queue = request_queue
        self.response_topic = response_topic
        self.status_blob_signature = status_blob_signature
