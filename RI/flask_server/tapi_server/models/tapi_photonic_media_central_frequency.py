# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_frequency_constraint import TapiPhotonicMediaFrequencyConstraint  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaCentralFrequency(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, central_frequency=None, frequency_constraint=None):  # noqa: E501
        """TapiPhotonicMediaCentralFrequency - a model defined in OpenAPI

        :param central_frequency: The central_frequency of this TapiPhotonicMediaCentralFrequency.  # noqa: E501
        :type central_frequency: int
        :param frequency_constraint: The frequency_constraint of this TapiPhotonicMediaCentralFrequency.  # noqa: E501
        :type frequency_constraint: TapiPhotonicMediaFrequencyConstraint
        """
        self.openapi_types = {
            'central_frequency': int,
            'frequency_constraint': TapiPhotonicMediaFrequencyConstraint
        }

        self.attribute_map = {
            'central_frequency': 'central-frequency',
            'frequency_constraint': 'frequency-constraint'
        }

        self._central_frequency = central_frequency
        self._frequency_constraint = frequency_constraint

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaCentralFrequency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.CentralFrequency of this TapiPhotonicMediaCentralFrequency.  # noqa: E501
        :rtype: TapiPhotonicMediaCentralFrequency
        """
        return util.deserialize_model(dikt, cls)

    @property
    def central_frequency(self):
        """Gets the central_frequency of this TapiPhotonicMediaCentralFrequency.

        The central frequency of the laser specified in MHz. It is the oscillation frequency of the corresponding electromagnetic wave.   # noqa: E501

        :return: The central_frequency of this TapiPhotonicMediaCentralFrequency.
        :rtype: int
        """
        return self._central_frequency

    @central_frequency.setter
    def central_frequency(self, central_frequency):
        """Sets the central_frequency of this TapiPhotonicMediaCentralFrequency.

        The central frequency of the laser specified in MHz. It is the oscillation frequency of the corresponding electromagnetic wave.   # noqa: E501

        :param central_frequency: The central_frequency of this TapiPhotonicMediaCentralFrequency.
        :type central_frequency: int
        """

        self._central_frequency = central_frequency

    @property
    def frequency_constraint(self):
        """Gets the frequency_constraint of this TapiPhotonicMediaCentralFrequency.


        :return: The frequency_constraint of this TapiPhotonicMediaCentralFrequency.
        :rtype: TapiPhotonicMediaFrequencyConstraint
        """
        return self._frequency_constraint

    @frequency_constraint.setter
    def frequency_constraint(self, frequency_constraint):
        """Sets the frequency_constraint of this TapiPhotonicMediaCentralFrequency.


        :param frequency_constraint: The frequency_constraint of this TapiPhotonicMediaCentralFrequency.
        :type frequency_constraint: TapiPhotonicMediaFrequencyConstraint
        """

        self._frequency_constraint = frequency_constraint
