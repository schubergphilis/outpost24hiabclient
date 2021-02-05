import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import outpost24hiabclient.tools.xmltools as xmltools

class TargetGroup(object):
    """description of class"""

    def __init__(self, outpost_instance, xml_data):
        self._outpost=outpost_instance
        self._data = self._parse_xml_data(xml_data)
        
    def _parse_xml_data(self, xml_data):
        if(xml_data.tag == 'GROUP'):
            return xml_data
        else:
            return Element('')

    @property
    def row_id(self):
        return self._data.get("rowid")

    @property
    def rulebased(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'RULEBASED')

    @property
    def rule(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'RULE')

    @property
    def reportbased(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'REPORTBASED')

    @property
    def xid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XID')

    @property
    def icount(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'ICOUNT')

    @property
    def pci(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PCI')

    @property
    def xuserxid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XUSERXID')

    @property
    def name(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'NAME')

    @property
    def xiparentid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XIPARENTID')



    #===SETTERS========================================================================

    #@row_id.setter
    #def row_id(self, row_id):
    #    self._data.set("rowid", str(row_id))

    #@rulebased.setter
    #def rulebased(self, rulebased):
    #    xmltools.set_boolean_value_as_string(self._data.findall('RULEBASED')[0].text, rulebased)

    #@rule.setter
    #def rule(self, rule):
    #    self._data.findall('RULE')[0].text = str(rule)

    #@reportbased.setter
    #def reportbased(self, reportbased):
    #    xmltools.set_boolean_value_as_string(self._data.findall('REPORTBASED')[0].text, reportbased)

    #@xid.setter
    #def xid(self, xid):
    #    self._data.findall('XID')[0].text = str(xid)

    #@icount.setter
    #def icount(self, icount):
    #    self._data.findall('ICOUNT')[0].text = str(icount)

    #@pci.setter
    #def pci(self, pci):
    #    xmltools.set_boolean_value_as_string(self._data.findall('PCI')[0].text, pci)

    #@xuserxid.setter
    #def xuserxid(self, xuserxid):
    #    self._data.findall('XUSERXID')[0].text = str(xuserxid)

    #@name.setter
    #def name(self, name):
    #    self._data.findall('NAME')[0].text = str(name)

    #@xparentid.setter
    #def xparentid(self, xparentid):
    #    self._data.findall('XPARENTID')[0].text = str(xparentid)
