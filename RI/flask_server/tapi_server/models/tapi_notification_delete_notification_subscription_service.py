# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_notification_deletenotificationsubscriptionservice_output import TapiNotificationDeletenotificationsubscriptionserviceOutput  # noqa: F401,E501
from tapi_server import util


class TapiNotificationDeleteNotificationSubscriptionService(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiNotificationDeleteNotificationSubscriptionService - a model defined in OpenAPI

        :param output: The output of this TapiNotificationDeleteNotificationSubscriptionService.  # noqa: E501
        :type output: TapiNotificationDeletenotificationsubscriptionserviceOutput
        """
        self.openapi_types = {
            'output': TapiNotificationDeletenotificationsubscriptionserviceOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationDeleteNotificationSubscriptionService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.DeleteNotificationSubscriptionService of this TapiNotificationDeleteNotificationSubscriptionService.  # noqa: E501
        :rtype: TapiNotificationDeleteNotificationSubscriptionService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiNotificationDeleteNotificationSubscriptionService.


        :return: The output of this TapiNotificationDeleteNotificationSubscriptionService.
        :rtype: TapiNotificationDeletenotificationsubscriptionserviceOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiNotificationDeleteNotificationSubscriptionService.


        :param output: The output of this TapiNotificationDeleteNotificationSubscriptionService.
        :type output: TapiNotificationDeletenotificationsubscriptionserviceOutput
        """

        self._output = output
