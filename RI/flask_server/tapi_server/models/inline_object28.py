# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_updatenotificationsubscriptionservice_input import TapiNotificationUpdatenotificationsubscriptionserviceInput  # noqa: F401,E501
from tapi_server import util


class InlineObject28(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject28 - a model defined in OpenAPI

        :param input: The input of this InlineObject28.  # noqa: E501
        :type input: TapiNotificationUpdatenotificationsubscriptionserviceInput
        """
        self.openapi_types = {
            'input': TapiNotificationUpdatenotificationsubscriptionserviceInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject28':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_28 of this InlineObject28.  # noqa: E501
        :rtype: InlineObject28
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject28.


        :return: The input of this InlineObject28.
        :rtype: TapiNotificationUpdatenotificationsubscriptionserviceInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject28.


        :param input: The input of this InlineObject28.
        :type input: TapiNotificationUpdatenotificationsubscriptionserviceInput
        """

        self._input = input
