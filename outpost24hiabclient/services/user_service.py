from requests import Session
import xml.etree.ElementTree as ET
import json


from ..tools import (xmltools, log)
from outpost24hiabclient.clients.hiabclient import HiabClient
from ..entities.user import User
from ..entities.usergroup import UserGroup


class UserService:

    def __init__(self, hiabclient):
        self._logger = log.getLogger(__name__)
        self._hiabclient = hiabclient

    def get_users(self):
        self._logger.critical("test")
        return self._hiabclient.get_users()

    def get_user_by_username(self, username):
        users = self._hiabclient.get_users()
        for u in users:
            if(u.vcusername == username):
                return u
        return None

    def get_usergroups(self):
        return self._hiabclient.get_usergroups()

    def get_users_in_usergroup(self, usergroup):
        result = []
        usergroupid = usergroup.xid
        users = self.get_users()
        for u in users:
            groups = u.usergrouplist
            if(usergroupid in groups):
                result.append(u)
        return result

    def get_usergroups_of_user(self, user):
        result = []
        groups = self.get_usergroups()
        grouplist = user.usergrouplist
        for gids in grouplist:
            for g in groups:
                if(gids == g.xid):
                    result.append(g)
        return result

    def create_user(self, vcfirstname, vclastname, vcemail, vcphonenumber, vccountry, vcusername, vcpassword, xid = -1, xisubparentid = -1, emailencryptionkey = 'Unencrypted', 
                    authenticationmethod = 0, twofactorauthentication = 0, credentialid = '', changepasswordonlogon = False, bactive = True, superuser = False, systemnotifications = False, 
                    hiabenroll = False, sendemailnotification = True, ticketparent = False, grouplist = '', usergrouplist = [], targetlist = [], boallhosts = True, allscanners = False, scannerlist = []):
        usergroupliststr = self._convert_list_to_string(usergrouplist)
        targetliststr = self._convert_list_to_string(targetlist)
        scannerliststr = self._convert_list_to_string(scannerlist)

        return self._hiabclient.create_user(self, vcfirstname, vclastname, vcemail, vcphonenumber, vccountry, vcusername, vcpassword, xid, xisubparentid, emailencryptionkey, 
                    authenticationmethod, twofactorauthentication, credentialid, changepasswordonlogon, bactive, superuser, systemnotifications, 
                    hiabenroll, sendemailnotification, ticketparent, grouplist, usergroupliststr, targetliststr, boallhosts, allscanners, scannerliststr)

    def delete_users(self, userlist):
        userliststr=self._convert_list_to_string(userlist)
        return self._hiabclient.delete_users(userliststr)

    def _convert_list_to_string(self, list):
        result = ''
        for l in list:
            if(result == ''):
                result = str(l.xid)
            else:
                result = result + ',' + str(l.xid)
        return result

