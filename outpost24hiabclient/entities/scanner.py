import outpost24hiabclient.tools.xmltools as xmltools

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


class Scanner(object):
    """description of class"""

    def __init__(self, outpost_instance, xml_data):
        self._outpost=outpost_instance
        self._data = self._parse_xml_data(xml_data)
 
    def _parse_xml_data(self, xml_data):
        if(xml_data.tag == 'SCANNER'):
            return xml_data
        else:
            return Element('')

    @property
    def row_id(self):
        return self._data.get("rowid")

    @property
    def ipaddress(self):
       return xmltools.get_str_from_child_if_exists(self._data, 'IPADDRESS')

    @property
    def isawsscanner(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ISAWSSCANNER')

    @property
    def useproxy(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'USEPROXY')

    @property
    def polling(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'POLLING')

    @property
    def isoutpost(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ISOUTPOST')

    @property
    def mode(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'MODE')

    @property
    def appsecscalescanner(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'APPSECSCALESCANNER')

    @property
    def xid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XID')

    @property
    def approved(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'APPROVED')

    @property
    def inactive(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'INACTIVE')

    @property
    def xupdator(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XUPDATOR')

    @property
    def performupdate(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PERFORMUPDATE')

    @property
    def isgroup(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ISGROUP')

    @property
    def lastconnection(self):
       return xmltools.get_date_from_child_if_exists(self._data, 'LASTCONNECTION')

    @property
    def message(self):
       return xmltools.get_str_from_child_if_exists(self._data, 'MESSAGE')

    @property
    def xuserxid(self):
       return xmltools.get_int_from_child_if_exists(self._data, 'XUSERXID')

    @property
    def name(self):
       return xmltools.get_str_from_child_if_exists(self._data, 'NAME')

    @property
    def scanningdisabled(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SCANNINGDISABLED')
