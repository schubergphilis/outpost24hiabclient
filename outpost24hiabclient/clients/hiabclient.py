#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: hiabclient.py
import logging
from requests import Session
import xml.etree.ElementTree as ET
import os
import json
from ..exceptions.exceptions import AuthFailed
from ..entities.user import User
from ..entities.usergroup import UserGroup
from ..entities.target import Target
from ..entities.targetgroup import TargetGroup
from ..entities.scanner import Scanner
from ..tools import (xmltools, log)


class HiabClient:

    def __init__(self, url, token):
        self._logger = log.getLogger(__name__)
        self.url = url
        self.api = '{url}/opi/XMLAPI'.format(url = url)
        self.token = token
        self.session = self._setup_session()

    def _setup_session(self):
        session = Session()
        #TODO: find out why OP24 certificate is invalid and remove this line
        session.verify = False        
        session.params.update({
            'APPTOKEN': self.token
        })
        response = session.get(self.api)
        if not response.ok:
            raise AuthFailed(response.content)
        return session

    def get_users(self):
        payload={'ACTION': 'SUBACCOUNTDATA', 'node': '-1', 'INCLUDESELF': '0', 'limit': '-1', 'id': '-1'}
        response = ET.fromstring(self._post_url(self.api,payload))
        userlist = response.findall('USERLIST')
        if(len(userlist) >= 1):
            users = userlist[0].findall('USER')
            return [User(self,u) for u in users]
        return []

    def get_usergroups(self):
        payload={'ACTION': 'USERGROUPDATA', 'limit': '-1'}
        response = ET.fromstring(self._post_url(self.api,payload))
        usergrouplist = response.findall('USERGROUPLIST')
        if(len(usergrouplist) >= 1):
            usergroups = usergrouplist[0].findall('USERGROUP')
            return [UserGroup(self,g) for g in usergroups]
        return []

    def get_targetgroups(self):
        payload={'ACTION': 'TARGETGROUPDATA', 'node': '-1', 'INCLUDEUNGROUP': '1', 'limit': '-1', 'id': '-1'}
        response = ET.fromstring(self._post_url(self.api,payload))
        grouplist = response.findall('GROUPLIST')
        if(len(grouplist) >= 1):
            groups = grouplist[0].findall('GROUP')
            return [TargetGroup(self,g) for g in groups]
        return []

    def get_targets(self, targetgroup = None):
        groupid = "-1"
        if(targetgroup):
            groupid = str(targetgroup.xid)
        payload={'ACTION': 'TARGETDATA', 'GROUP': groupid, 'limit': '-1', 'sort': 'HOSTNAME', 'dir': 'ASC'}
        response = ET.fromstring(self._post_url(self.api,payload))
        targetlist = response.findall('TARGETLIST')
        if(len(targetlist) >= 1):
            targets = targetlist[0].findall('TARGET')
            return [Target(self,t) for t in targets]
        return []

    def get_target(self, xid):
        payload={'ACTION': 'TARGETDATA', 'XID': xid, 'CLEANSETTINGS': 1, 'id': xid}
        response = ET.fromstring(self._post_url(self.api,payload))
        targetlist = response.findall('TARGETLIST')
        if(len(targetlist) >= 1):
            targets = targetlist[0].findall('TARGET')
            if(len(targetlist) >= 1):
                return Target(self,targets[0])
        return None

    def get_scanners(self):
        payload={'ACTION': 'SCANNERDATA', 'SCANNERS': '1', 'GROUPS': '1', 'limit': '-1', 'sort': 'NAME', 'dir': 'ASC'}
        response = ET.fromstring(self._post_url(self.api,payload))
        scannerlist = response.findall('SCANNERLIST')
        if(len(scannerlist) >= 1):
            scanners = scannerlist[0].findall('SCANNER')
            return [Scanner(self,s) for s in scanners]
        return []

    #def get_parent_targetgroup_of_targetgroup(self, targetgroup):
    #    for t in self.get_targetgroups():
    #        if(targetgroup.xiparentid is not None):
    #            if(targetgroup.xiparentid == t.xid):
    #                return t
    #    return None

    #def get_child_targetgroups_of_targetgroup(self, targetgroup):
    #    targetgroups = self.get_targetgroups()
    #    result = []
    #    for t in targetgroups:
    #        if(t.xiparentid is not None):
    #            if(t.xiparentid == targetgroup.xid):
    #                result.append(t)
    #    return result

    #def get_user_of_targetgroup(self, targetgroup):
    #    users = self.get_users()
    #    for u in users:
    #        if(targetgroup.xuserxid is not None):
    #            if(targetgroup.xuserxid == u.xid):
    #                return u
    #    return None
    
    #def get_targets_in_targetgroup(self, targetgroup):
    #    return self.get_targets(targetgroup.xid)



    def create_user(self, vcfirstname, vclastname, vcemail, vcphonenumber, vccountry, vcusername, vcpassword, xid = -1, xisubparentid = -1, emailencryptionkey = 'Unencrypted', 
                    authenticationmethod = 0, twofactorauthentication = 0, credentialid = '', changepasswordonlogon = False, bactive = True, superuser = False, systemnotifications = False, 
                    hiabenroll = False, sendemailnotification = True, ticketparent = False, grouplist = '', usergroupliststr = "", targetliststr = "", boallhosts = True, allscanners = False, scannerliststr = ""):
        changepasswordonlogon_val = int(changepasswordonlogon == True)
        bactive_val = int(bactive == True)
        superuser_val = int(superuser == True)
        systemnotifications_val = int(systemnotifications == True)
        hiabenroll_val = int(hiabenroll == True)
        sendemailnotification_val = int(sendemailnotification == True)
        ticketparent_val = int(ticketparent == True)
        boallhosts_val = int(boallhosts == True)
        allscanners_val = int(allscanners == True)
        xid=str(xid)

        payload={'ACTION': 'UPDATESUBACCOUNTDATA', 'JSON': 1, 'XID': xid, 'USERGROUPLIST': usergroupliststr, 'VCPASSWORD': vcpassword, 'XISUBPARENTID': xisubparentid, 
                 'VCFIRSTNAME': vcfirstname, 'VCLASTNAME': vclastname, 'VCEMAIL': vcemail, 'VCPHONEMOBILE': vcphonenumber, 'VCCOUNTRY': vccountry, 'EMAILENCRYPTIONKEY': emailencryptionkey,
                 'AUTHENTICATIONMETHOD': authenticationmethod, 'VCUSERNAME': vcusername, 'VCPASSWD1': vcpassword, 'VCPASSWD2': vcpassword, 'TWOFACTORAUTHENTICATION': twofactorauthentication,
                 'CREDENTIALID': credentialid, 'CHANGEPASSWORDONLOGON': changepasswordonlogon_val, 'BACTIVE': bactive_val, 'SUPERUSER': superuser_val, 'SYSTEMNOTIFICATIONS': systemnotifications_val, 
                 'HIABENROLL': hiabenroll_val, 'SENDEMAILNOTIFICATION': sendemailnotification_val, 'TICKETPARENT': ticketparent_val, 'GROUPLIST': grouplist, 'TARGETLIST': targetliststr,
                 'BOALLHOSTS': boallhosts_val, 'ALLSCANNERS': allscanners_val, 'SCANNERLIST': scannerliststr}

        r = self._post_url_with_json_response(self.api, payload)
        if(r['success']==True):
            xid = r['data']['XID']
            users = self.get_users()
            for u in users:
                if(u.xid == xid):
                    return u
        elif(r['success']==False):
            raise RuntimeError(r['data']['errorMessage'])
        return None


    def delete_users(self, userliststr):
        payload={'ACTION': 'REMOVESUBACCOUNTDATA', 'XID': userliststr}
        response = ET.fromstring(self._post_url(self.api,payload))
        result = xmltools.get_str_from_child_if_exists(response, 'SUCCESS')
        if(result == 'true'):
            return True
        return False

    def create_targets(self, targetlist, targetgroup, dnslookup, scanner, CUSTOM0=None, CUSTOM1=None, CUSTOM2=None, CUSTOM3=None, CUSTOM4=None, CUSTOM5=None, CUSTOM6=None, CUSTOM7=None, CUSTOM8=None, CUSTOM9=None):
        result = []
        print(targetlist)
        targetliststr = '\n'.join(targetlist)
        dnslookup_val = int(dnslookup == True)
        payload={'ACTION': 'INSERTTARGETDATA', 'JSON': '1', 'GROUP': targetgroup.xid, 'TARGETLIST': targetliststr, 'DNSLOOKUP': dnslookup_val, 'SCANNERID': scanner.xid}
        if(CUSTOM0 != None):
            payload['CUSTOM0'] = CUSTOM0
        if(CUSTOM1 != None):
            payload['CUSTOM1'] = CUSTOM1
        if(CUSTOM2 != None):
            payload['CUSTOM2'] = CUSTOM2
        if(CUSTOM3 != None):
            payload['CUSTOM3'] = CUSTOM3
        if(CUSTOM4 != None):
            payload['CUSTOM4'] = CUSTOM4
        if(CUSTOM5 != None):
            payload['CUSTOM5'] = CUSTOM5
        if(CUSTOM6 != None):
            payload['CUSTOM6'] = CUSTOM5
        if(CUSTOM7 != None):
            payload['CUSTOM7'] = CUSTOM5
        if(CUSTOM8 != None):
            payload['CUSTOM8'] = CUSTOM5
        if(CUSTOM9 != None):
            payload['CUSTOM9'] = CUSTOM5

        r = self._post_url_with_json_response(self.api, payload)
        if(r['success']==True):
            targets = self.get_targets(targetgroup)
            for t1 in targets:
                for t2 in targetlist:
                    if(t1.hostname == t2 or t1.ipaddress == t2):
                        result.append(t1)
        elif(r['success']==False):
            raise RuntimeError(r['data']['errorMessage'])
        return result

    def delete_targets(self, targetlist):
        targetliststr=""
        for t in targetlist:
            if(targetliststr == ""):
                targetliststr = str(t.xid)
            else:
                targetliststr = targetliststr + ',' + str(t.xid)
        payload={'ACTION': 'REMOVETARGETDATA', 'XID': targetliststr}
        response = ET.fromstring(self._post_url(self.api,payload))
        result = xmltools.get_str_from_child_if_exists(response, 'SUCCESS')
        if(result == 'true'):
            return True
        return False

    def update_target(self, target,
                        macaddress = "",
                        businesscriticality = "MEDIUM",
                        exposed = 0,
                        scannerid = 0,
                        virtualhosts = "",
                        hiddenurls = "",
                        urlblacklist = "",
                        requestbodyblacklist = "",
                        cvss_cdrp = "ND",
                        cvss_sr_avail = "ND",
                        cvss_sr_integ = "ND",
                        cvss_sr_conf = "ND",
                        cvss_td = "ND",
                        custom0 = "",
                        custom1 = "",
                        custom2 = "",
                        custom3 = "",
                        custom4 = "",
                        custom5 = "",
                        custom6 = "",
                        custom7 = "",
                        custom8 = "",
                        custom9 = "",
                        testresults = "",
                        authenticationtype = 0,
                        sshusername = "",
                        sshpassword = "",
                        sshsubstituteuser = "",
                        sshpublickey = "",
                        sshprivatekey = "",
                        sshprivatekeypassword = "",
                        smbdomain = "",
                        smbntlmv1 = 0,
                        smbusername = "",
                        smbpassword = "",
                        enableremoteregistry = 0,
                        cyberarkusername = "",
                        cyberarkname = "",
                        cyberarkoverridesafe = "",
                        cyberarkoverridefolder = "",
                        cyberarkdomain = "",
                        cyberarkntlmv1 = 0,
                        cyberarkenableremoteregistry = 0,
                        vsphereusername = "",
                        vspherepassword = "",
                        ignorecerts = 0,
                        thycoticsshsecret = "",
                        thycoticsshoverridepath = "",
                        thycoticsshsubstituteuser = "",
                        thycoticsmbsecret = "",
                        thycoticsmboverridepath = "",
                        thycoticsmbntlmv1 = 0,
                        thycoticsmbenableremoteregistry = 0,
                        sshport = 22,
                        compliancesenabled = "",
                        databases = "<itemlist></itemlist>"):
        payload={'ACTION': 'UPDATETARGETDATA', 'XID': target.xid}
        payload['MACADDRESS'] = macaddress
        payload['BUSINESSCRITICALITY'] = businesscriticality
        payload['EXPOSED'] = exposed
        payload['SCANNERID'] = scannerid
        payload['VIRTUALHOSTS'] = virtualhosts
        payload['HIDDENURLS'] = hiddenurls
        payload['URLBLACKLIST'] = urlblacklist
        payload['REQUESTBODYBLACKLIST'] = requestbodyblacklist
        payload['CVSS_CDRP'] = cvss_cdrp
        payload['CVSS_SR_AVAIL'] = cvss_sr_avail
        payload['CVSS_SR_INTEG'] = cvss_sr_integ
        payload['CVSS_SR_CONF'] = cvss_sr_conf
        payload['CVSS_TD'] = cvss_td
        payload['CUSTOM0'] = custom0
        payload['CUSTOM1'] = custom1
        payload['CUSTOM2'] = custom2
        payload['CUSTOM3'] = custom3
        payload['CUSTOM4'] = custom4
        payload['CUSTOM5'] = custom5
        payload['CUSTOM6'] = custom6
        payload['CUSTOM7'] = custom7
        payload['CUSTOM8'] = custom8
        payload['CUSTOM9'] = custom9
        payload['TESTRESULTS'] = testresults
        payload['AUTHENTICATIONTYPE'] = authenticationtype
        payload['SSHUSERNAME'] = sshusername
        payload['SSHPASSWORD'] = sshpassword
        payload['SSHSUBSTITUTEUSER'] = sshsubstituteuser
        payload['SSHPUBLICKEY'] = sshpublickey
        payload['SSHPRIVATEKEY'] = sshprivatekey
        payload['SSHPRIVATEKEYPASSWORD'] = sshprivatekeypassword
        payload['SMBDOMAIN'] = smbdomain
        payload['SMBNTLMV1'] = smbntlmv1
        payload['SMBUSERNAME'] = smbusername
        payload['SMBPASSWORD'] = smbpassword
        payload['ENABLEREMOTEREGISTRY'] = enableremoteregistry
        payload['CYBERARKUSERNAME'] = cyberarkusername
        payload['CYBERARKNAME'] = cyberarkname
        payload['CYBERARKOVERRIDESAFE'] = cyberarkoverridesafe
        payload['CYBERARKOVERRIDEFOLDER'] = cyberarkoverridefolder
        payload['CYBERARKDOMAIN'] = cyberarkdomain
        payload['CYBERARKNTLMV1'] = cyberarkntlmv1
        payload['CYBERARKENABLEREMOTEREGISTRY'] = cyberarkenableremoteregistry
        payload['VSPHEREUSERNAME'] = vsphereusername
        payload['VSPHEREPASSWORD'] = vspherepassword
        payload['IGNORECERTS'] = ignorecerts
        payload['THYCOTICSSHSECRET'] = thycoticsshsecret
        payload['THYCOTICSSHOVERRIDEPATH'] = thycoticsshoverridepath
        payload['THYCOTICSSHSUBSTITUTEUSER'] = thycoticsshsubstituteuser
        payload['THYCOTICSMBSECRET'] = thycoticsmbsecret
        payload['THYCOTICSMBOVERRIDEPATH'] = thycoticsmboverridepath
        payload['THYCOTICSMBNTLMV1'] = thycoticsmbntlmv1
        payload['THYCOTICSMBENABLEREMOTEREGISTRY'] = thycoticsmbenableremoteregistry
        payload['SSHPORT'] = sshport
        payload['COMPLIANCESENABLED'] = compliancesenabled
        payload['DATABASES'] = databases
        
        r = self._post_url_with_json_response(self.api, payload)
        xid = r['data']['XID']
        tg = self.get_target(xid)
        return tg

    def move_target(self, target, src_targetgroup, dst_targetgroup, dst_parent_targetgroup):
        payload={'ACTION': 'UPDATETARGETGROUPDATA', 'MOVE': 'true'}
        payload['ADDTARGETLIST'] = target.xid
        payload['XID'] = dst_targetgroup.xid
        payload['XIPARENTID'] = dst_parent_targetgroup.xid
        payload['GROUPXID'] = src_targetgroup.xid
        
        response = ET.fromstring(self._post_url(self.api,payload))
        result = xmltools.get_str_from_child_if_exists(response, 'SUCCESS')
        if(result == 'true'):
            return True
        else:
            return False

    def create_targetgroup(self, name, parent_targetgroup=None):
        payload={'ACTION': 'UPDATETARGETGROUPDATA', 'JSON': '1', 'XID': '-1', 'NAME': name}
        if(parent_targetgroup):
            payload['XIPARENTID'] = parent_targetgroup.xid
        r = self._post_url_with_json_response(self.api, payload)
        xid = r['data']['XID']
        tgs = self.get_targetgroups()
        for t in tgs:
            if(t.xid == xid):
                return t

    def delete_targetgroups(self, targetgrouplist):
        targetgroupliststr=""
        for t in targetgrouplist:
            if(targetgroupliststr == ""):
                targetgroupliststr = str(t.xid)
            else:
                targetgroupliststr = targetgroupliststr + ',' + str(t.xid)
        payload={'ACTION': 'REMOVETARGETGROUPDATA', 'XID': targetgroupliststr}
        response = ET.fromstring(self._post_url(self.api,payload))
        result = xmltools.get_str_from_child_if_exists(response, 'SUCCESS')
        if(result == 'true'):
            return True
        return False



    def _post_url(self, url, payload, request_timeout=120):
        results = []
        payload['REQUESTTIMEOUT'] = request_timeout
        try:
            response = self.session.post(url, data=payload)
            if(response.ok):
                if(len(response.text)>1):
                    textresponse = ET.fromstring(response.text)
                    result = xmltools.get_str_from_child_if_exists(textresponse, 'SUCCESS')
                    if(result == 'false'):
                        errorcode = xmltools.get_str_from_child_if_exists(textresponse, 'ERRORCODE')
                        message = xmltools.get_str_from_child_if_exists(textresponse, 'MESSAGE')
                        errorstr = 'Posting to url: {} failed with error code: {} and message: {}'.format(url, errorcode, message)
                        self._logger.error(errorstr)
                        raise RuntimeError('Failed to call Outpost24 HIAB API' + os.linesep + errorstr)
                    else:
                        return response.text
                else:
                    raise RuntimeError('Failed to call Outpost24 HIAB API as the request is invalid.')
            else:
                errorstr = 'Posting to url: {} failed with error code: {} and message: {}'.format(url, str(response.status_code))
                self._logger.error(errorstr)
                raise RuntimeError('Failed to call Outpost24 HIAB API' + os.linesep + errorstr)
        except ValueError as e:
            self._logger.error('Error getting url :%s', url)
            raise RuntimeError(str(e))

    def _post_url_with_json_response(self, url, payload, request_timeout=120):
        results = []
        payload['REQUESTTIMEOUT'] = request_timeout
        payload['JSON'] = '1'
        try:
            response = self.session.post(url, data=payload)
            if(response.ok):
                r = json.loads(response.text)
                if(r['success']==True):
                    return r
                elif(r['success']==False):
                    raise RuntimeError(r['data']['errorMessage'])
            else:
                errorstr = 'Posting to url: {} failed with error code: {} and message: {}'.format(url, str(response.status_code))
                self._logger.error(errorstr)
                raise RuntimeError('Failed to call Outpost24 HIAB API' + os.linesep + errorstr)
        except ValueError as e:
            self._logger.error('Error getting url :%s', url)
            raise RuntimeError(str(e))