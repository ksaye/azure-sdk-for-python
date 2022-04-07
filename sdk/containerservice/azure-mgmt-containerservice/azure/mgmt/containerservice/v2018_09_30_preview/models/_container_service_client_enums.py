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


class OpenShiftAgentPoolProfileRole(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """OpenShiftAgentPoolProfileRole represents the role of the AgentPoolProfile.
    """

    COMPUTE = "compute"
    INFRA = "infra"

class OpenShiftContainerServiceVMSize(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Size of OpenShift VMs.
    """

    STANDARD_D2_S_V3 = "Standard_D2s_v3"
    STANDARD_D4_S_V3 = "Standard_D4s_v3"
    STANDARD_D8_S_V3 = "Standard_D8s_v3"
    STANDARD_D16_S_V3 = "Standard_D16s_v3"
    STANDARD_D32_S_V3 = "Standard_D32s_v3"
    STANDARD_D64_S_V3 = "Standard_D64s_v3"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_F8_S_V2 = "Standard_F8s_v2"
    STANDARD_F16_S_V2 = "Standard_F16s_v2"
    STANDARD_F32_S_V2 = "Standard_F32s_v2"
    STANDARD_F64_S_V2 = "Standard_F64s_v2"
    STANDARD_F72_S_V2 = "Standard_F72s_v2"
    STANDARD_F8_S = "Standard_F8s"
    STANDARD_F16_S = "Standard_F16s"
    STANDARD_E4_S_V3 = "Standard_E4s_v3"
    STANDARD_E8_S_V3 = "Standard_E8s_v3"
    STANDARD_E16_S_V3 = "Standard_E16s_v3"
    STANDARD_E20_S_V3 = "Standard_E20s_v3"
    STANDARD_E32_S_V3 = "Standard_E32s_v3"
    STANDARD_E64_S_V3 = "Standard_E64s_v3"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_L4_S = "Standard_L4s"
    STANDARD_L8_S = "Standard_L8s"
    STANDARD_L16_S = "Standard_L16s"
    STANDARD_L32_S = "Standard_L32s"

class OSType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux.
    """

    LINUX = "Linux"
    WINDOWS = "Windows"
