from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model import Model
from server import util


class StatusChanged(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_id=None, job_id=None, level=None, timestamp=None, message=None, status=None):  # noqa: E501
        """StatusChanged - a model defined in OpenAPI

        :param device_id: The device_id of this StatusChanged.  # noqa: E501
        :type device_id: str
        :param job_id: The job_id of this StatusChanged.  # noqa: E501
        :type job_id: str
        :param level: The level of this StatusChanged.  # noqa: E501
        :type level: str
        :param timestamp: The timestamp of this StatusChanged.  # noqa: E501
        :type timestamp: str
        :param message: The message of this StatusChanged.  # noqa: E501
        :type message: str
        :param status: The status of this StatusChanged.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'device_id': str,
            'job_id': str,
            'level': str,
            'timestamp': str,
            'message': str,
            'status': str
        }

        self.attribute_map = {
            'device_id': 'deviceId',
            'job_id': 'jobId',
            'level': 'level',
            'timestamp': 'timestamp',
            'message': 'message',
            'status': 'status'
        }

        self._device_id = device_id
        self._job_id = job_id
        self._level = level
        self._timestamp = timestamp
        self._message = message
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'StatusChanged':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The statusChanged of this StatusChanged.  # noqa: E501
        :rtype: StatusChanged
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_id(self) -> str:
        """Gets the device_id of this StatusChanged.


        :return: The device_id of this StatusChanged.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id: str):
        """Sets the device_id of this StatusChanged.


        :param device_id: The device_id of this StatusChanged.
        :type device_id: str
        """

        self._device_id = device_id

    @property
    def job_id(self) -> str:
        """Gets the job_id of this StatusChanged.


        :return: The job_id of this StatusChanged.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id: str):
        """Sets the job_id of this StatusChanged.


        :param job_id: The job_id of this StatusChanged.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def level(self) -> str:
        """Gets the level of this StatusChanged.


        :return: The level of this StatusChanged.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level: str):
        """Sets the level of this StatusChanged.


        :param level: The level of this StatusChanged.
        :type level: str
        """

        self._level = level

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this StatusChanged.


        :return: The timestamp of this StatusChanged.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this StatusChanged.


        :param timestamp: The timestamp of this StatusChanged.
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def message(self) -> str:
        """Gets the message of this StatusChanged.


        :return: The message of this StatusChanged.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this StatusChanged.


        :param message: The message of this StatusChanged.
        :type message: str
        """

        self._message = message

    @property
    def status(self) -> str:
        """Gets the status of this StatusChanged.


        :return: The status of this StatusChanged.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this StatusChanged.


        :param status: The status of this StatusChanged.
        :type status: str
        """

        self._status = status