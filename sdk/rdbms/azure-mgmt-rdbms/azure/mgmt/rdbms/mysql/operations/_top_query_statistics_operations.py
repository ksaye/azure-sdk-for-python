# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
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

def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    server_name: str,
    query_statistic_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2018-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/topQueryStatistics/{queryStatisticId}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "queryStatisticId": _SERIALIZER.url("query_statistic_id", query_statistic_id, 'str'),
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


def build_list_by_server_request(
    subscription_id: str,
    resource_group_name: str,
    server_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2018-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/topQueryStatistics')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
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
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )

class TopQueryStatisticsOperations(object):
    """TopQueryStatisticsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.rdbms.mysql.models
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
    def get(
        self,
        resource_group_name: str,
        server_name: str,
        query_statistic_id: str,
        **kwargs: Any
    ) -> "_models.QueryStatistic":
        """Retrieve the query statistic for specified identifier.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param query_statistic_id: The Query Statistic identifier.
        :type query_statistic_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryStatistic, or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql.models.QueryStatistic
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QueryStatistic"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            server_name=server_name,
            query_statistic_id=query_statistic_id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QueryStatistic', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/topQueryStatistics/{queryStatisticId}'}  # type: ignore


    @distributed_trace
    def list_by_server(
        self,
        resource_group_name: str,
        server_name: str,
        parameters: "_models.TopQueryStatisticsInput",
        **kwargs: Any
    ) -> Iterable["_models.TopQueryStatisticsResultList"]:
        """Retrieve the Query-Store top queries for specified metric and aggregation.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param server_name: The name of the server.
        :type server_name: str
        :param parameters: The required parameters for retrieving top query statistics.
        :type parameters: ~azure.mgmt.rdbms.mysql.models.TopQueryStatisticsInput
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TopQueryStatisticsResultList or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.rdbms.mysql.models.TopQueryStatisticsResultList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TopQueryStatisticsResultList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                _json = self._serialize.body(parameters, 'TopQueryStatisticsInput')
                
                request = build_list_by_server_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    content_type=content_type,
                    json=_json,
                    template_url=self.list_by_server.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                _json = self._serialize.body(parameters, 'TopQueryStatisticsInput')
                
                request = build_list_by_server_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    content_type=content_type,
                    json=_json,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("TopQueryStatisticsResultList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_server.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/topQueryStatistics'}  # type: ignore
