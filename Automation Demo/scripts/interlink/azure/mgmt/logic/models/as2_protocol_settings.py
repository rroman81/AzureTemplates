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


class AS2ProtocolSettings(Model):
    """AS2ProtocolSettings.

    :param message_connection_settings: The message connection settings.
    :type message_connection_settings: :class:`AS2MessageConnectionSettings
     <azure.mgmt.logic.models.AS2MessageConnectionSettings>`
    :param acknowledgement_connection_settings: The acknowledgement
     connection settings.
    :type acknowledgement_connection_settings:
     :class:`AS2AcknowledgementConnectionSettings
     <azure.mgmt.logic.models.AS2AcknowledgementConnectionSettings>`
    :param mdn_settings: The MDN settings.
    :type mdn_settings: :class:`AS2MdnSettings
     <azure.mgmt.logic.models.AS2MdnSettings>`
    :param security_settings: The security settings.
    :type security_settings: :class:`AS2SecuritySettings
     <azure.mgmt.logic.models.AS2SecuritySettings>`
    :param validation_settings: The validation settings.
    :type validation_settings: :class:`AS2ValidationSettings
     <azure.mgmt.logic.models.AS2ValidationSettings>`
    :param envelope_settings: The envelope settings.
    :type envelope_settings: :class:`AS2EnvelopeSettings
     <azure.mgmt.logic.models.AS2EnvelopeSettings>`
    :param error_settings: The error settings.
    :type error_settings: :class:`AS2ErrorSettings
     <azure.mgmt.logic.models.AS2ErrorSettings>`
    """ 

    _attribute_map = {
        'message_connection_settings': {'key': 'messageConnectionSettings', 'type': 'AS2MessageConnectionSettings'},
        'acknowledgement_connection_settings': {'key': 'acknowledgementConnectionSettings', 'type': 'AS2AcknowledgementConnectionSettings'},
        'mdn_settings': {'key': 'mdnSettings', 'type': 'AS2MdnSettings'},
        'security_settings': {'key': 'securitySettings', 'type': 'AS2SecuritySettings'},
        'validation_settings': {'key': 'validationSettings', 'type': 'AS2ValidationSettings'},
        'envelope_settings': {'key': 'envelopeSettings', 'type': 'AS2EnvelopeSettings'},
        'error_settings': {'key': 'errorSettings', 'type': 'AS2ErrorSettings'},
    }

    def __init__(self, message_connection_settings=None, acknowledgement_connection_settings=None, mdn_settings=None, security_settings=None, validation_settings=None, envelope_settings=None, error_settings=None):
        self.message_connection_settings = message_connection_settings
        self.acknowledgement_connection_settings = acknowledgement_connection_settings
        self.mdn_settings = mdn_settings
        self.security_settings = security_settings
        self.validation_settings = validation_settings
        self.envelope_settings = envelope_settings
        self.error_settings = error_settings
