import logging
from requests import Session
import xml.etree.ElementTree as ET
import json


from ..tools import xmltools
from outpost24hiabclient.clients.hiabclient import HiabClient
from ..entities.scanner import Scanner



LOGGER_BASENAME = '''outpost24hiabclient'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())

class ScannerService:

    def __init__(self, hiabclient):
        logger_name = u'{base}.{suffix}'.format(base=LOGGER_BASENAME,
                                                suffix=self.__class__.__name__)
        logging.config.fileConfig('logging.conf')
        self._logger = logging.getLogger(logger_name)
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