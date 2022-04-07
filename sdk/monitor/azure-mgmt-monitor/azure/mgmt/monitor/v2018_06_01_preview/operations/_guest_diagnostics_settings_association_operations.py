# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_create_or_update_request(
    resource_uri: str,
    association_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2018-06-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}')
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, 'str', skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_request(
    resource_uri: str,
    association_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-06-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}')
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, 'str', skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    resource_uri: str,
    association_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-06-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}')
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, 'str', skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_update_request(
    resource_uri: str,
    association_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2018-06-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}')
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, 'str', skip_quote=True),
        "associationName": _SERIALIZER.url("association_name", association_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_list_request(
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-06-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/microsoft.insights/guestDiagnosticSettingsAssociations')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_by_resource_group_request(
    resource_group_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-06-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/guestDiagnosticSettingsAssociations')
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class GuestDiagnosticsSettingsAssociationOperations(object):
    """GuestDiagnosticsSettingsAssociationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2018_06_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def create_or_update(
        self,
        resource_uri: str,
        association_name: str,
        diagnostic_settings_association: "_models.GuestDiagnosticSettingsAssociationResource",
        **kwargs: Any
    ) -> "_models.GuestDiagnosticSettingsAssociationResource":
        """Creates or updates guest diagnostics settings association.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association.
        :type association_name: str
        :param diagnostic_settings_association: The diagnostic settings association to create or
         update.
        :type diagnostic_settings_association:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GuestDiagnosticSettingsAssociationResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(diagnostic_settings_association, 'GuestDiagnosticSettingsAssociationResource')

        request = build_create_or_update_request(
            resource_uri=resource_uri,
            association_name=association_name,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('GuestDiagnosticSettingsAssociationResource', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('GuestDiagnosticSettingsAssociationResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_uri: str,
        association_name: str,
        **kwargs: Any
    ) -> "_models.GuestDiagnosticSettingsAssociationResource":
        """Gets guest diagnostics association settings.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association.
        :type association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GuestDiagnosticSettingsAssociationResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_uri=resource_uri,
            association_name=association_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GuestDiagnosticSettingsAssociationResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_uri: str,
        association_name: str,
        **kwargs: Any
    ) -> None:
        """Delete guest diagnostics association settings.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association.
        :type association_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            resource_uri=resource_uri,
            association_name=association_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}'}  # type: ignore


    @distributed_trace
    def update(
        self,
        resource_uri: str,
        association_name: str,
        parameters: "_models.GuestDiagnosticSettingsAssociationResourcePatch",
        **kwargs: Any
    ) -> "_models.GuestDiagnosticSettingsAssociationResource":
        """Updates an existing guestDiagnosticsSettingsAssociation Resource. To update other fields use
        the CreateOrUpdate method.

        :param resource_uri: The fully qualified ID of the resource, including the resource name and
         resource type.
        :type resource_uri: str
        :param association_name: The name of the diagnostic settings association.
        :type association_name: str
        :param parameters: Parameters supplied to the operation.
        :type parameters:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResourcePatch
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GuestDiagnosticSettingsAssociationResource, or the result of cls(response)
        :rtype:
         ~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GuestDiagnosticSettingsAssociationResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'GuestDiagnosticSettingsAssociationResourcePatch')

        request = build_update_request(
            resource_uri=resource_uri,
            association_name=association_name,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GuestDiagnosticSettingsAssociationResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/{resourceUri}/providers/microsoft.insights/guestDiagnosticSettingsAssociation/{associationName}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> Iterable["_models.GuestDiagnosticSettingsAssociationList"]:
        """Get a list of all guest diagnostic settings association in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GuestDiagnosticSettingsAssociationList or the
         result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GuestDiagnosticSettingsAssociationList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("GuestDiagnosticSettingsAssociationList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/microsoft.insights/guestDiagnosticSettingsAssociations'}  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> Iterable["_models.GuestDiagnosticSettingsAssociationList"]:
        """Get a list of all guest diagnostic settings association in a resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GuestDiagnosticSettingsAssociationList or the
         result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2018_06_01_preview.models.GuestDiagnosticSettingsAssociationList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GuestDiagnosticSettingsAssociationList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_resource_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("GuestDiagnosticSettingsAssociationList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/guestDiagnosticSettingsAssociations'}  # type: ignore
