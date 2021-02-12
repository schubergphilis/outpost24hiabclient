from requests import Session
import xml.etree.ElementTree as ET
import json
from ..tools import (xmltools, log)
from outpost24hiabclient.clients.hiabclient import HiabClient
from ..entities.scanner import Scanner


class ScannerService:

    def __init__(self, hiabclient):
        self._logger = log.getLogger(__name__)
        self._hiabclient = hiabclient


    def get_scanners(self):
        return self._hiabclient.get_scanners()


    def get_scanner_by_name(self, scanner_name):
        scanners = self._hiabclient.get_scanners()
        for s in scanners:
            if(s.name == scanner_name):
                return s
        return None


    def get_scanner_by_id(self, scanner_id):
        scanners = self._hiabclient.get_scanners()
        for s in scanners:
            if(s.xid == scanner_id):
                return s
        return None