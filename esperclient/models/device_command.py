# coding: utf-8

"""
    Esper Manage API

    # Introduction Esper Manage APIs for Cloud are a set of REST-based APIs that help you programmatically control and monitor your enterprise's dedicated Esper endpoint. Using these APIs, one can orchestrate & manage devices that have been provisioned against your endpoint. Furthermore, this API allows you to manage android applications that get installed on such devices. To read more about the various capabilities of Esper endpoints and Esper managed devices, please visit [esper.io](https://esper.io). This guide describes all the available APIs in detail, along with code samples for you to quickly ramp up to using them.  You can find out more about Esper at [https://esper.io](https://esper.io)  We've done our best to keep this document up to date, but if you find any issues, please reach out to us at developer@esper.io.  # SDK    You are welcome to use your favorite HTTP/REST library for your programming language in order to use these APIs, or you can use our official SDK (currently available in [python](https://github.com/esper-io/esper-client-py)) to do so.   # Authentication Client needs to send authentication details to access APIs. Following authentication schemes are supported:  #### Basic Authentication Client can use username and password to authenticate. These are your developer account credentials. For example, the client sends HTTP requests with the Authorization header that contains the word `Basic` followed by a space and a base64-encoded string `username:password`. ##### Base64 encoding Bash  ``` echo 'username:password' | base64 ```  Powershell  ``` [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes(\"username:password\")) ```  **Example request** ```bash curl -X GET \\   https://DOMAIN.shoonyacloud.com/api/enterprise/<enterprise_id>/device/ \\   -H 'Authorization: Basic cl0ZWFkbWluOnNpdG1pbjEyMyQ=' \\   -H 'Content-Type: application/json' \\ ``` You can read more about basic authentication scheme  [here](https://swagger.io/docs/specification/authentication/basic-authentication/)  # Errors The API uses standard HTTP status codes to indicate success or failure. All error responses will have a JSON body in the following format  ``` {   \"errors\": [],   \"message\": \"error message\",   \"status\": 400 } ``` * `errors` -  List of error details * `message` - Error description * `status` - HTTP status code   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@esper.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from esperclient.models.device_command_enum import DeviceCommandEnum  # noqa: F401,E501


class DeviceCommand(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'current_base_uri': 'str',
        'command_args': 'str',
        'action': 'str',
        'schedule': 'str',
        'group_schedule_id': 'str',
        'command': 'DeviceCommandEnum',
        'state': 'str',
        'details': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'enterprise': 'str',
        'device': 'str',
        'group_command': 'str',
        'issued_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'current_base_uri': 'current_base_uri',
        'command_args': 'command_args',
        'action': 'action',
        'schedule': 'schedule',
        'group_schedule_id': 'group_schedule_id',
        'command': 'command',
        'state': 'state',
        'details': 'details',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'enterprise': 'enterprise',
        'device': 'device',
        'group_command': 'group_command',
        'issued_by': 'issued_by'
    }

    def __init__(self, id=None, current_base_uri=None, command_args=None, action=None, schedule=None, group_schedule_id=None, command=None, state=None, details=None, created_on=None, updated_on=None, enterprise=None, device=None, group_command=None, issued_by=None):  # noqa: E501
        """DeviceCommand - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._current_base_uri = None
        self._command_args = None
        self._action = None
        self._schedule = None
        self._group_schedule_id = None
        self._command = None
        self._state = None
        self._details = None
        self._created_on = None
        self._updated_on = None
        self._enterprise = None
        self._device = None
        self._group_command = None
        self._issued_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if current_base_uri is not None:
            self.current_base_uri = current_base_uri
        if command_args is not None:
            self.command_args = command_args
        if action is not None:
            self.action = action
        if schedule is not None:
            self.schedule = schedule
        if group_schedule_id is not None:
            self.group_schedule_id = group_schedule_id
        self.command = command
        if state is not None:
            self.state = state
        if details is not None:
            self.details = details
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        self.enterprise = enterprise
        self.device = device
        if group_command is not None:
            self.group_command = group_command
        if issued_by is not None:
            self.issued_by = issued_by

    @property
    def id(self):
        """Gets the id of this DeviceCommand.  # noqa: E501


        :return: The id of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceCommand.


        :param id: The id of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def current_base_uri(self):
        """Gets the current_base_uri of this DeviceCommand.  # noqa: E501


        :return: The current_base_uri of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._current_base_uri

    @current_base_uri.setter
    def current_base_uri(self, current_base_uri):
        """Sets the current_base_uri of this DeviceCommand.


        :param current_base_uri: The current_base_uri of this DeviceCommand.  # noqa: E501
        :type: str
        """
        if current_base_uri is not None and len(current_base_uri) < 1:
            raise ValueError("Invalid value for `current_base_uri`, length must be greater than or equal to `1`")  # noqa: E501

        self._current_base_uri = current_base_uri

    @property
    def command_args(self):
        """Gets the command_args of this DeviceCommand.  # noqa: E501


        :return: The command_args of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._command_args

    @command_args.setter
    def command_args(self, command_args):
        """Sets the command_args of this DeviceCommand.


        :param command_args: The command_args of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._command_args = command_args

    @property
    def action(self):
        """Gets the action of this DeviceCommand.  # noqa: E501


        :return: The action of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this DeviceCommand.


        :param action: The action of this DeviceCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["acknowledge", "in_progress", "success", "failed"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def schedule(self):
        """Gets the schedule of this DeviceCommand.  # noqa: E501


        :return: The schedule of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this DeviceCommand.


        :param schedule: The schedule of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def group_schedule_id(self):
        """Gets the group_schedule_id of this DeviceCommand.  # noqa: E501


        :return: The group_schedule_id of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._group_schedule_id

    @group_schedule_id.setter
    def group_schedule_id(self, group_schedule_id):
        """Sets the group_schedule_id of this DeviceCommand.


        :param group_schedule_id: The group_schedule_id of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._group_schedule_id = group_schedule_id

    @property
    def command(self):
        """Gets the command of this DeviceCommand.  # noqa: E501


        :return: The command of this DeviceCommand.  # noqa: E501
        :rtype: DeviceCommandEnum
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this DeviceCommand.


        :param command: The command of this DeviceCommand.  # noqa: E501
        :type: DeviceCommandEnum
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def state(self):
        """Gets the state of this DeviceCommand.  # noqa: E501


        :return: The state of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeviceCommand.


        :param state: The state of this DeviceCommand.  # noqa: E501
        :type: str
        """
        allowed_values = ["Command Initiated", "Command Acknowledged", "Command In Progress", "Command TimeOut", "Command Success", "Command Failure", "Command Scheduled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def details(self):
        """Gets the details of this DeviceCommand.  # noqa: E501


        :return: The details of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DeviceCommand.


        :param details: The details of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def created_on(self):
        """Gets the created_on of this DeviceCommand.  # noqa: E501


        :return: The created_on of this DeviceCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceCommand.


        :param created_on: The created_on of this DeviceCommand.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this DeviceCommand.  # noqa: E501


        :return: The updated_on of this DeviceCommand.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this DeviceCommand.


        :param updated_on: The updated_on of this DeviceCommand.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def enterprise(self):
        """Gets the enterprise of this DeviceCommand.  # noqa: E501


        :return: The enterprise of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this DeviceCommand.


        :param enterprise: The enterprise of this DeviceCommand.  # noqa: E501
        :type: str
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")  # noqa: E501

        self._enterprise = enterprise

    @property
    def device(self):
        """Gets the device of this DeviceCommand.  # noqa: E501


        :return: The device of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceCommand.


        :param device: The device of this DeviceCommand.  # noqa: E501
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def group_command(self):
        """Gets the group_command of this DeviceCommand.  # noqa: E501


        :return: The group_command of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._group_command

    @group_command.setter
    def group_command(self, group_command):
        """Sets the group_command of this DeviceCommand.


        :param group_command: The group_command of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._group_command = group_command

    @property
    def issued_by(self):
        """Gets the issued_by of this DeviceCommand.  # noqa: E501


        :return: The issued_by of this DeviceCommand.  # noqa: E501
        :rtype: str
        """
        return self._issued_by

    @issued_by.setter
    def issued_by(self, issued_by):
        """Sets the issued_by of this DeviceCommand.


        :param issued_by: The issued_by of this DeviceCommand.  # noqa: E501
        :type: str
        """

        self._issued_by = issued_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceCommand, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other