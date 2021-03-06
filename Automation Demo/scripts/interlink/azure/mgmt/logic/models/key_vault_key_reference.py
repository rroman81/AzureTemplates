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


class KeyVaultKeyReference(Model):
    """KeyVaultKeyReference.

    :param key_vault: The key vault reference.
    :type key_vault: :class:`KeyVaultKeyReferenceKeyVault
     <azure.mgmt.logic.models.KeyVaultKeyReferenceKeyVault>`
    :param key_name: The private key name in key vault.
    :type key_name: str
    :param key_version: The private key version in key vault.
    :type key_version: str
    """ 

    _attribute_map = {
        'key_vault': {'key': 'keyVault', 'type': 'KeyVaultKeyReferenceKeyVault'},
        'key_name': {'key': 'keyName', 'type': 'str'},
        'key_version': {'key': 'keyVersion', 'type': 'str'},
    }

    def __init__(self, key_vault=None, key_name=None, key_version=None):
        self.key_vault = key_vault
        self.key_name = key_name
        self.key_version = key_version
