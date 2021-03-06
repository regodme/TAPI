# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiOduOduCommonPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, odu_rate_tolerance=None, odu_rate=None, odu_type=None):  # noqa: E501
        """TapiOduOduCommonPac - a model defined in OpenAPI

        :param odu_rate_tolerance: The odu_rate_tolerance of this TapiOduOduCommonPac.  # noqa: E501
        :type odu_rate_tolerance: int
        :param odu_rate: The odu_rate of this TapiOduOduCommonPac.  # noqa: E501
        :type odu_rate: int
        :param odu_type: The odu_type of this TapiOduOduCommonPac.  # noqa: E501
        :type odu_type: str
        """
        self.openapi_types = {
            'odu_rate_tolerance': int,
            'odu_rate': int,
            'odu_type': str
        }

        self.attribute_map = {
            'odu_rate_tolerance': 'odu-rate-tolerance',
            'odu_rate': 'odu-rate',
            'odu_type': 'odu-type'
        }

        self._odu_rate_tolerance = odu_rate_tolerance
        self._odu_rate = odu_rate
        self._odu_type = odu_type

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduOduCommonPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.OduCommonPac of this TapiOduOduCommonPac.  # noqa: E501
        :rtype: TapiOduOduCommonPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def odu_rate_tolerance(self):
        """Gets the odu_rate_tolerance of this TapiOduOduCommonPac.

        This attribute indicates the rate tolerance of the ODU termination point.                       Valid values are real value in the unit of ppm.                       Standardized values are defined in Table 7-2/G.709.  # noqa: E501

        :return: The odu_rate_tolerance of this TapiOduOduCommonPac.
        :rtype: int
        """
        return self._odu_rate_tolerance

    @odu_rate_tolerance.setter
    def odu_rate_tolerance(self, odu_rate_tolerance):
        """Sets the odu_rate_tolerance of this TapiOduOduCommonPac.

        This attribute indicates the rate tolerance of the ODU termination point.                       Valid values are real value in the unit of ppm.                       Standardized values are defined in Table 7-2/G.709.  # noqa: E501

        :param odu_rate_tolerance: The odu_rate_tolerance of this TapiOduOduCommonPac.
        :type odu_rate_tolerance: int
        """

        self._odu_rate_tolerance = odu_rate_tolerance

    @property
    def odu_rate(self):
        """Gets the odu_rate of this TapiOduOduCommonPac.

        This attribute indicates the rate of the ODU terminatino point.                       This attribute is Set at create; i.e., once created it cannot be changed directly.                       In case of resizable ODU flex, its value can be changed via HAO (not directly on the attribute).                         # noqa: E501

        :return: The odu_rate of this TapiOduOduCommonPac.
        :rtype: int
        """
        return self._odu_rate

    @odu_rate.setter
    def odu_rate(self, odu_rate):
        """Sets the odu_rate of this TapiOduOduCommonPac.

        This attribute indicates the rate of the ODU terminatino point.                       This attribute is Set at create; i.e., once created it cannot be changed directly.                       In case of resizable ODU flex, its value can be changed via HAO (not directly on the attribute).                         # noqa: E501

        :param odu_rate: The odu_rate of this TapiOduOduCommonPac.
        :type odu_rate: int
        """

        self._odu_rate = odu_rate

    @property
    def odu_type(self):
        """Gets the odu_type of this TapiOduOduCommonPac.

        This attribute specifies the type of the ODU termination point.  # noqa: E501

        :return: The odu_type of this TapiOduOduCommonPac.
        :rtype: str
        """
        return self._odu_type

    @odu_type.setter
    def odu_type(self, odu_type):
        """Sets the odu_type of this TapiOduOduCommonPac.

        This attribute specifies the type of the ODU termination point.  # noqa: E501

        :param odu_type: The odu_type of this TapiOduOduCommonPac.
        :type odu_type: str
        """

        self._odu_type = odu_type
