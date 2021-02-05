import datetime

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import outpost24hiabclient.tools.xmltools as xmltools

class Target(object):
    """description of class"""

    def __init__(self, outpost_instance, xml_data):
        self._outpost=outpost_instance
        self._data = self._parse_xml_data(xml_data)

    def _parse_xml_data(self, xml_data):
        if(xml_data.tag == 'TARGET'):
            return xml_data
        else:
            return Element('')

    @property
    def row_id(self):
        return self._data.get("rowid")

    @property
    def testcredxid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'TESTCREDXID')

    @property
    def authenticationtype(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'AUTHENTICATIONTYPE')

    @property
    def hostname(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'HOSTNAME')

    @property
    def xupdator(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XUPDATOR')

    @property
    def credentialproviderid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'CREDENTIALPROVIDERID')

    @property
    def scannername(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'SCANNERNAME')

    @property
    def macaddress(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'MACADDRESS')

    @property
    def enableremoteregistry(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ENABLEREMOTEREGISTRY')

    @property
    def cvss_sr_conf(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CVSS_SR_CONF')

    @property
    def ungrouped(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'UNGROUPED')

    @property
    def macsource(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'MACSOURCE')

    @property
    def crawled(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'CRAWLED')

    @property
    def low_count(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'LOW_COUNT')

    @property
    def reachable(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'REACHABLE')

    @property
    def outofscope(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'OUTOFSCOPE')

    @property
    def scanless_possible(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SCANLESS_POSSIBLE')

    @property
    def confirmed(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'CONFIRMED')

    @property
    def scanupdateavailible(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SCANUPDATEAVAILIBLE')

    @property
    def nextscandate(self):
        return xmltools.get_date_from_child_if_exists(self._data, 'NEXTSCANDATE')

    @property
    def batchmode(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BATCHMODE')

    @property
    def useslicense(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'USESLICENSE')

    @property
    def authenticationresult(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'AUTHENTICATIONRESULT')

    @property
    def cyberarkntlmv1(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'CYBERARKNTLMV1')

    @property
    def medium_count(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'MEDIUM_COUNT')

    @property
    def xid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XID')

    @property
    def scannerid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'SCANNERID')

    @property
    def lookupperformed(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'LOOKUPPERFORMED')

    @property
    def cyberarkenableremoteregistry(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'CYBERARKENABLEREMOTEREGISTRY')

    @property
    def templateoverride(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'TEMPLATEOVERRIDE')

    @property
    def count(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'COUNT')

    @property
    def sync(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'SYNC')

    @property
    def ipercentv(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'IPERCENTV')

    @property
    def pcicompliance(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'PCICOMPLIANCE')

    @property
    def hostnameid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'HOSTNAMEID')

    @property
    def xuserxid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XUSERXID')

    @property
    def latestscanstatus(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'LATESTSCANSTATUS')

    @property
    def cvss_sr_avail(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CVSS_SR_AVAIL')

    @property
    def ipaddress(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'IPADDRESS')

    @property
    def smbntlmv1(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SMBNTLMV1')

    @property
    def platform(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'PLATFORM')

    @property
    def latestscandate(self):
        return xmltools.get_date_from_child_if_exists(self._data, 'LATESTSCANDATE')

    @property
    def pci(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PCI')

    @property
    def custom0(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM0')

    @property
    def custom1(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM1')

    @property
    def custom2(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM2')

    @property
    def custom3(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM3')

    @property
    def custom4(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM4')

    @property
    def custom5(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM5')

    @property
    def custom6(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM6')

    @property
    def custom7(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM7')
    
    @property
    def custom8(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM8')

    @property
    def custom9(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CUSTOM9')

    @property
    def ignorecerts(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'IGNORECERTS')

    @property
    def hasdiscoverydata(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'HASDISCOVERYDATA')

    @property
    def cvss_sr_integ(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CVSS_SR_INTEG')

    @property
    def cvss_cdp(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CVSS_CDP')

    @property
    def cvss_td(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'CVSS_TD')

    @property
    def compliant(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'COMPLIANT')

    @property
    def high_count(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'HIGH_COUNT')

    @property
    def limited(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'LIMITED')

    @property
    def virtualhosts(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VIRTUALHOSTS')
