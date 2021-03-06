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


class PoolPatchParameter(Model):
    """Parameters for a CloudPoolOperations.Patch request.

    :param start_task: A task to run on each compute node as it joins the
     pool. If omitted, any existing start task is left unchanged.
    :type start_task: :class:`StartTask <azure.batch.models.StartTask>`
    :param certificate_references: A list of certificates to be installed on
     each compute node in the pool. If omitted, any existing certificate
     references are left unchanged.
    :type certificate_references: list of :class:`CertificateReference
     <azure.batch.models.CertificateReference>`
    :param application_package_references: A list of application packages to
     be installed on each compute node in the pool. If omitted, any existing
     application package references are left unchanged.
    :type application_package_references: list of
     :class:`ApplicationPackageReference
     <azure.batch.models.ApplicationPackageReference>`
    :param metadata: A list of name-value pairs associated with the pool as
     metadata. If omitted, any existing metadata is left unchanged.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _attribute_map = {
        'start_task': {'key': 'startTask', 'type': 'StartTask'},
        'certificate_references': {'key': 'certificateReferences', 'type': '[CertificateReference]'},
        'application_package_references': {'key': 'applicationPackageReferences', 'type': '[ApplicationPackageReference]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, start_task=None, certificate_references=None, application_package_references=None, metadata=None):
        self.start_task = start_task
        self.certificate_references = certificate_references
        self.application_package_references = application_package_references
        self.metadata = metadata
