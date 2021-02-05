import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import outpost24hiabclient.tools.xmltools as xmltools

class UserGroup(object):
    """description of class"""

    def __init__(self, outpost_instance, xml_data):
        self._outpost=outpost_instance
        self._data = self._parse_xml_data(xml_data)
        
    def _parse_xml_data(self, xml_data):
        if(xml_data.tag == 'USERGROUP'):
            return xml_data
        else:
            return Element('')

    @property
    def row_id(self):
        return self._data.get("rowid")

    @property
    def webappdeletereport(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'WEBAPPDELETEREPORT')

    @property
    def bodisable(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BODISABLE')

    @property
    def bhmonitor(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BHMONITOR')

    @property
    def webappadmin(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'WEBAPPADMIN')

    @property
    def compliance_enabled(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'COMPLIANCE_ENABLED')

    @property
    def verifyscan(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'VERIFYSCAN')

    @property
    def bovultext(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOVULTEXT')

    @property
    def xid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XID')

    @property
    def xupdator(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XUPDATOR')

    @property
    def swatcomment(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SWATCOMMENT')

    @property
    def readonly(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'READONLY')

    @property
    def webappreporting(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'WEBAPPREPORTING')

    @property
    def bodeletereport(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BODELETEREPORT')

    @property
    def wasx(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'WASX')

    @property
    def dashboard(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'DASHBOARD')

    @property
    def boemail(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOEMAIL')

    @property
    def pcireporting(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PCIREPORTING')

    @property
    def bsubadmin(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BSUBADMIN')

    @property
    def bticketmanagement(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BTICKETMANAGEMENT')

    @property
    def ruleadmin(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'RULEADMIN')

    @property
    def pcischeduling(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PCISCHEDULING')

    @property
    def approvecompliancequestions(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'APPROVECOMPLIANCEQUESTIONS')

    @property
    def rulemanagement(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'RULEMANAGEMENT')

    @property
    def xuserxid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XUSERXID')

    @property
    def autorules(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'AUTORULES')

    @property
    def vcname(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCNAME')

    @property
    def bosettings(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOSETTINGS')

    @property
    def stopscan(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'STOPSCAN')

    @property
    def forcegroupscheduling(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'FORCEGROUPSCHEDULING')

    @property
    def managedservicescomment(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'MANAGEDSERVICESCOMMENT')

    @property
    def grantalltickets(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'GRANTALLTICKETS')

    @property
    def boreports(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOREPORTS')

    @property
    def swatverification(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SWATVERIFICATION')

    @property
    def answercompliancequestions(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ANSWERCOMPLIANCEQUESTIONS')

    @property
    def read_auditlogs(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'READ_AUDITLOGS')

    @property
    def read_auditlogs(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'READ_AUDITLOGS')

    @property
    def boadmingroups(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOADMINGROUPS')

    @property
    def bacceptrisk(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BACCEPTRISK')

    @property
    def readlicense(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'READLICENSE')

    @property
    def editcompliancepolicies(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'EDITCOMPLIANCEPOLICIES')

    @property
    def web(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'WEB')

    @property
    def pciscoping(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PCISCOPING')

    @property
    def submitscoping(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SUBMITSCOPING')

    @property
    def swatrisks(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SWATRISKS')

    @property
    def boschedules(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOSCHEDULES')

    @property
    def swatdiscussion(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SWATDISCUSSION')

    @property
    def badminusergroup(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BADMINUSERGROUP')

    @property
    def markcomplianceexceptions(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'MARKCOMPLIANCEEXCEPTIONS')

    @property
    def bhadmin(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BHADMIN')

    @property
    def bosms(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOSMS')

    @property
    def pcidisputing(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'PCIDISPUTING')

    @property
    def managedservices(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'MANAGEDSERVICES')

    @property
    def editrules(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'EDITRULES')
