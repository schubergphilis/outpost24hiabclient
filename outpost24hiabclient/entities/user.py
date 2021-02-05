
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import outpost24hiabclient.tools.xmltools as xmltools

class User(object):  # pylint: disable=too-many-public-methods
    """Models the user object of outpost24."""

    def __init__(self, outpost_instance, xml_data):
        self._outpost=outpost_instance
        self._data = self._parse_xml_data(xml_data)
        
    def _parse_xml_data(self, xml_data):
        if(xml_data.tag == 'USER'):
            return xml_data
        else:
            return Element('')

    @property
    def parent(self):
       return xmltools.get_str_from_child_if_exists(self._data, 'PARENT')

    @property
    def ilogon(self):
       return xmltools.get_str_from_child_if_exists(self._data, 'ILOGON')

    @property
    def dlastlogon(self):
       return xmltools.get_str_from_child_if_exists(self._data, 'DLASTLOGON')

    @property
    def scannerlist(self):
        str = xmltools.get_str_from_child_if_exists(self._data, 'SCANNERLIST')
        if(str is not None):
            return str.split(',')
        else:
            return []

    @property
    def awsarnlist(self):
       xmltools.get_str_from_child_if_exists(self._data, 'AWSARNLIST')
       raise(NotImplementedError)

    @property
    def allswat(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ALLSWAT')

    @property
    def iemailtype(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'IEMAILTYPE')

    @property
    def xisubparentid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XISUBPARENTID')

    @property
    def twofactorauthentication(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'TWOFACTORAUTHENTICATION')

    @property
    def grouplist(self):
        result = []
        str = xmltools.get_str_from_child_if_exists(self._data, 'GROUPLIST')
        if(str is not None):
            split_str = str.split(',')
            for s in split_str:
                result.append(int(s))
        return result

    @property
    def authenticationmethod(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'AUTHENTICATIONMETHOD')

    @property
    def dcreated(self):
        return xmltools.get_date_from_child_if_exists(self._data, 'DCREATED')

    @property
    def startdayofweek(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'STARTDAYOFWEEK')

    @property
    def vcphonemobile(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCPHONEMOBILE')

    @property
    def boallhosts(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BOALLHOSTS')

    @property
    def emailencryptionkey(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'EMAILENCRYPTIONKEY')

    @property
    def targetgroups(self):
        str = xmltools.get_str_from_child_if_exists(self._data, 'TARGETGROUPS')
        if(str is not None):
            return str.split(',')
        else:
            return []

    @property
    def xpathup(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'XPATHUP')

    @property
    def usergrouplist(self):
        result = []
        str = xmltools.get_str_from_child_if_exists(self._data, 'USERGROUPLIST')
        if(str is not None):
            split_str = str.split(',')
            for s in split_str:
                if(not(s == "")):
                    result.append(int(s))
        return result

    @property
    def allawsarn(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ALLAWSARN')

    @property
    def country(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'COUNTRY')

    @property
    def vclastname(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCLASTNAME')

    @property
    def xid(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'XID')

    @property
    def ticketparent(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'TICKETPARENT')

    @property
    def systemnotifications(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SYSTEMNOTIFICATIONS')

    @property
    def targetlist(self):
        str = xmltools.get_str_from_child_if_exists(self._data, 'TARGETLIST')
        if(str is not None):
            return str.split('\n')
        else:
            return []

    @property
    def allscanners(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'ALLSCANNERS')

    @property
    def bactive(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'BACTIVE')

    @property
    def vcemail(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCEMAIL')

    @property
    def demail(self):
        return xmltools.get_date_from_child_if_exists(self._data, 'DEMAIL')

    @property
    def showguide(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SHOWGUIDE')

    @property
    def vcfirstname(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCFIRSTNAME')

    @property
    def wasmaximumlinks(self):
        return xmltools.get_int_from_child_if_exists(self._data, 'WASMAXIMUMLINKS')

    @property
    def swatapplications(self):
        xmltools.get_str_from_child_if_exists(self._data, 'SWATAPPLICATIONS')
        raise(NotImplementedError)

    @property
    def vcfullname(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCFULLNAME')

    @property
    def vcusername(self):
        return xmltools.get_str_from_child_if_exists(self._data, 'VCUSERNAME')

    @property
    def swatlist(self):
        xmltools.get_str_from_child_if_exists(self._data, 'SWATLIST')
        raise(NotImplementedError)

    @property
    def superuser(self):
        return xmltools.get_bool_from_child_if_exists(self._data, 'SUPERUSER')


    #===SETTERS========================================================================

    #@parent.setter
    #def parent(self, parent):
    #   self._data.findall('PARENT')[0].text = parent

    #@ilogon.setter
    #def ilogon(self, ilogon):
    #   self._data.findall('ILOGON')[0].text = ilogon

    #@dlastlogon.setter
    #def dlastlogon(self, dlastlogon):
    #   self._data.findall('DLASTLOGON')[0].text = dlastlogon

    #@scannerlist.setter
    #def scannerlist(self, scannerlist):
    #    self._data.findall('SCANNERLIST')[0].text = ','.join(scannerlist)
        
    #@awsarnlist.setter
    #def awsarnlist(self, awsarnlist):
    #   raise(NotImplementedError)

    #@allswat.setter
    #def allswat(self, allswat):
    #    xmltools.set_boolean_value_as_string(self._data.findall('ALLSWAT')[0], allswat)

    #@iemailtype.setter
    #def iemailtype(self, iemailtype):
    #    self._data.findall('IEMAILTYPE')[0].text = str(iemailtype)

    #@xisubparentid.setter
    #def xisubparentid(self, xisubparentid):
    #    self._data.findall('XISUBPARENTID')[0].text = str(xisubparentid)

    #@twofactorauthentication.setter
    #def twofactorauthentication(self, twofactorauthentication):
    #    self._data.findall('TWOFACTORAUTHENTICATION')[0].text = str(twofactorauthentication)

    #@grouplist.setter
    #def grouplist(self, grouplist):
    #    self._data.findall('GROUPLIST')[0].text = ','.join(grouplist)

    #@authenticationmethod.setter
    #def authenticationmethod(self, authenticationmethod):
    #    self._data.findall('AUTHENTICATIONMETHOD')[0].text = str(authenticationmethod)

    #@dcreated.setter
    #def dcreated(self, dcreated):
    #    raise(NotImplementedError)

    #@startdayofweek.setter
    #def startdayofweek(self, startdayofweek):
    #    self._data.findall('STARTDAYOFWEEK')[0].text = str(startdayofweek)

    #@vcphonemobile.setter
    #def vcphonemobile(self, vcphonemobile):
    #    self._data.findall('VCPHONEMOBILE')[0].text = vcphonemobile

    #@boallhosts.setter
    #def boallhosts(self, boallhosts):
    #    xmltools.set_boolean_value_as_string(self._data.findall('BOALLHOSTS')[0], boallhosts)

    #@emailencryptionkey.setter
    #def emailencryptionkey(self, emailencryptionkey):
    #    self._data.findall('EMAILENCRYPTIONKEY')[0].text = emailencryptionkey

    #@targetgroups.setter
    #def targetgroups(self, targetgroups):
    #    self._data.findall('TARGETGROUPS')[0].text = ','.join(targetgroups)

    #@xpathup.setter
    #def xpathup(self, xpathup):
    #    self._data.findall('XPATHUP')[0].text = xpathup

    #@usergrouplist.setter
    #def usergrouplist(self, usergrouplist):
    #    self._data.findall('USERGROUPLIST')[0].text = ','.join(usergrouplist)

    #@allawsarn.setter
    #def allawsarn(self, allawsarn):
    #    xmltools.set_boolean_value_as_string(self._data.findall('ALLAWSARN')[0], allawsarn)

    #@country.setter
    #def country(self, country):
    #    self._data.findall('COUNTRY')[0].text = country

    #@vclastname.setter
    #def vclastname(self, vclastname):
    #    self._data.findall('VCLASTNAME')[0].text = vclastname

    #@xid.setter
    #def xid(self, xid):
    #    self._data.findall('XID')[0].text = str(xid)

    #@ticketparent.setter
    #def ticketparent(self, ticketparent):
    #    self._data.findall('TICKETPARENT')[0].text = ticketparent

    #@systemnotifications.setter
    #def systemnotifications(self, systemnotifications):
    #    xmltools.set_boolean_value_as_string(self._data.findall('SYSTEMNOTIFICATIONS')[0], systemnotifications)

    #@targetlist.setter
    #def targetlist(self, targetlist):
    #    self._data.findall('TARGETLIST')[0].text = '\n'.join(targetlist)

    #@allscanners.setter
    #def allscanners(self, allscanners):
    #    xmltools.set_boolean_value_as_string(self._data.findall('ALLSCANNERS')[0], allscanners)

    #@bactive.setter
    #def bactive(self, bactive):
    #    xmltools.set_boolean_value_as_string(self._data.findall('BACTIVE')[0], bactive)

    #@vcemail.setter
    #def vcemail(self, vcemail):
    #    self._data.findall('VCEMAIL')[0].text = vcemail

    #@showguide.setter
    #def showguide(self, showguide):
    #    xmltools.set_boolean_value_as_string(self._data.findall('SHOWGUIDE')[0], showguide)

    #@vcfirstname.setter
    #def vcfirstname(self, vcfirstname):
    #    self._data.findall('VCFIRSTNAME')[0].text = vcfirstname

    #@wasmaximumlinks.setter
    #def wasmaximumlinks(self, wasmaximumlinks):
    #    self._data.findall('WASMAXIMUMLINKS')[0].text = str(wasmaximumlinks)

    #@swatapplications.setter
    #def swatapplications(self, swatapplications):
    #    self._data.findall('SWATAPPLICATIONS')[0]
    #    raise(NotImplementedError)

    #@vcfullname.setter
    #def vcfullname(self, vcfullname):
    #    self._data.findall('VCFULLNAME')[0].text = vcfullname

    #@vcusername.setter
    #def vcusername(self, vcusername):
    #    self._data.findall('VCUSERNAME')[0].text = vcusername

    #@swatlist.setter
    #def swatlist(self, swatlist):
    #    self._data.findall('SWATLIST')[0]
    #    raise(NotImplementedError)

    #@superuser.setter
    #def superuser(self, superuser):
    #    xmltools.set_boolean_value_as_string(self._data.findall('SUPERUSER')[0], superuser)

