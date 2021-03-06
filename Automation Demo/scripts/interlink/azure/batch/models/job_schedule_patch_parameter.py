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


class JobSchedulePatchParameter(Model):
    """Parameters for a CloudJobScheduleOperations.Patch request.

    :param schedule: The schedule according to which jobs will be created.
    :type schedule: :class:`Schedule <azure.batch.models.Schedule>`
    :param job_specification: The details of the jobs to be created on this
     schedule.
    :type job_specification: :class:`JobSpecification
     <azure.batch.models.JobSpecification>`
    :param metadata: A list of name-value pairs associated with the job
     schedule as metadata.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    """ 

    _attribute_map = {
        'schedule': {'key': 'schedule', 'type': 'Schedule'},
        'job_specification': {'key': 'jobSpecification', 'type': 'JobSpecification'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
    }

    def __init__(self, schedule=None, job_specification=None, metadata=None):
        self.schedule = schedule
        self.job_specification = job_specification
        self.metadata = metadata
