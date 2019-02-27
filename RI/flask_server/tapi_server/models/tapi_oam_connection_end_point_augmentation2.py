# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_mep_mip_list import TapiOamMepMipList  # noqa: F401,E501
from tapi_server import util


class TapiOamConnectionEndPointAugmentation2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mep_mip_list=None):  # noqa: E501
        """TapiOamConnectionEndPointAugmentation2 - a model defined in OpenAPI

        :param mep_mip_list: The mep_mip_list of this TapiOamConnectionEndPointAugmentation2.  # noqa: E501
        :type mep_mip_list: TapiOamMepMipList
        """
        self.openapi_types = {
            'mep_mip_list': TapiOamMepMipList
        }

        self.attribute_map = {
            'mep_mip_list': 'mep-mip-list'
        }

        self._mep_mip_list = mep_mip_list

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamConnectionEndPointAugmentation2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.ConnectionEndPointAugmentation2 of this TapiOamConnectionEndPointAugmentation2.  # noqa: E501
        :rtype: TapiOamConnectionEndPointAugmentation2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mep_mip_list(self):
        """Gets the mep_mip_list of this TapiOamConnectionEndPointAugmentation2.


        :return: The mep_mip_list of this TapiOamConnectionEndPointAugmentation2.
        :rtype: TapiOamMepMipList
        """
        return self._mep_mip_list

    @mep_mip_list.setter
    def mep_mip_list(self, mep_mip_list):
        """Sets the mep_mip_list of this TapiOamConnectionEndPointAugmentation2.


        :param mep_mip_list: The mep_mip_list of this TapiOamConnectionEndPointAugmentation2.
        :type mep_mip_list: TapiOamMepMipList
        """

        self._mep_mip_list = mep_mip_list