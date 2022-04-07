# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DeploymentProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the status of the resource at the time the operation was called.
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    DELETING = "Deleting"
    MOVING = "Moving"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"

class DeploymentScaleType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Deployment scale type.
    """

    MANUAL = "Manual"

class HostingModel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Account hosting model.
    """

    WEB = "Web"
    CONNECTED_CONTAINER = "ConnectedContainer"
    DISCONNECTED_CONTAINER = "DisconnectedContainer"

class KeyName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """key name to generate (Key1|Key2)
    """

    KEY1 = "Key1"
    KEY2 = "Key2"

class KeySource(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates the possible value of keySource for Encryption
    """

    MICROSOFT_COGNITIVE_SERVICES = "Microsoft.CognitiveServices"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"

class NetworkRuleAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The default action when no rule from ipRules and from virtualNetworkRules match. This is only
    used after the bypass property has been evaluated.
    """

    ALLOW = "Allow"
    DENY = "Deny"

class Origin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the status of the cognitive services account at the time the operation was called.
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    DELETING = "Deleting"
    MOVING = "Moving"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    RESOLVING_DNS = "ResolvingDNS"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Whether or not public endpoint access is allowed for this account.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class QuotaUsageStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Cognitive Services account quota usage status.
    """

    INCLUDED = "Included"
    BLOCKED = "Blocked"
    IN_OVERAGE = "InOverage"
    UNKNOWN = "Unknown"

class ResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"

class ResourceSkuRestrictionsReasonCode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for restriction.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class ResourceSkuRestrictionsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of restrictions.
    """

    LOCATION = "Location"
    ZONE = "Zone"

class SkuTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"

class UnitType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    MILLISECONDS = "Milliseconds"
