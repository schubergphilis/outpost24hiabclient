import unittest
from outpost24hiabclient.entities.scanner import Scanner
from outpost24hiabclient.clients.hiabclient import HiabClient
from outpost24hiabclient.services.scanner_service import ScannerService

import logging
import xml.etree.ElementTree as ET

class HiabClientTest:
 
    def get_scanners(self):
        data="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                <RESPONSE ACTION=\"SCANNERDATA\" TIMESTAMP=\"2021-01-28 11:54\" USERNAME=\"ACCEPTANCE\" VERSION=\"4.22.12.0\">\
	                <SCANNERLIST>\
		                <TOTALCOUNT>2</TOTALCOUNT>\
		                <COLLAPSEDTOTAL>2</COLLAPSEDTOTAL>\
		                <SCANNER rowid=\"1\">\
			                <IPADDRESS>127.0.0.1</IPADDRESS>\
			                <ISAWSSCANNER>false</ISAWSSCANNER>\
			                <USEPROXY>false</USEPROXY>\
			                <POLLING>false</POLLING>\
			                <ISOUTPOST>false</ISOUTPOST>\
			                <MODE>1</MODE>\
			                <APPSECSCALESCANNER>false</APPSECSCALESCANNER>\
			                <XID>0</XID>\
			                <APPROVED>true</APPROVED>\
			                <INACTIVE>false</INACTIVE>\
			                <XUPDATOR>0</XUPDATOR>\
			                <PERFORMUPDATE>false</PERFORMUPDATE>\
			                <ISGROUP>false</ISGROUP>\
			                <XUSERXID>11</XUSERXID>\
			                <NAME>Local</NAME>\
			                <SCANNINGDISABLED>false</SCANNINGDISABLED>\
			                <SLSSCANSCHEDULED>false</SLSSCANSCHEDULED>\
		                </SCANNER>\
		                <SCANNER rowid=\"2\">\
			                <IPADDRESS>outscan.outpost24.com</IPADDRESS>\
			                <ISAWSSCANNER>false</ISAWSSCANNER>\
			                <USEPROXY>false</USEPROXY>\
			                <POLLING>false</POLLING>\
			                <ISOUTPOST>true</ISOUTPOST>\
			                <MODE>1</MODE>\
			                <APPSECSCALESCANNER>false</APPSECSCALESCANNER>\
			                <XID>2</XID>\
			                <APPROVED>false</APPROVED>\
			                <INACTIVE>false</INACTIVE>\
			                <XUPDATOR>0</XUPDATOR>\
			                <PERFORMUPDATE>false</PERFORMUPDATE>\
			                <ISGROUP>false</ISGROUP>\
			                <XUSERXID>11</XUSERXID>\
			                <NAME>Outscan</NAME>\
			                <SCANNINGDISABLED>false</SCANNINGDISABLED>\
			                <SLSSCANSCHEDULED>false</SLSSCANSCHEDULED>\
		                </SCANNER>\
	                </SCANNERLIST>\
	                <PROXYENABLED>0</PROXYENABLED>\
	                <NOTIFYMISSING>0</NOTIFYMISSING>\
                </RESPONSE>"
        xmldata = ET.fromstring(data)
        scannerlist = xmldata.findall('SCANNERLIST')
        if(len(scannerlist) >= 1):
            scanners = scannerlist[0].findall('SCANNER')
            return [Scanner(self,s) for s in scanners]


class ScannerServiceTests(unittest.TestCase):

    def setUp(self):
        self.scanner_service = ScannerService(HiabClientTest())


    def test_parse_xml_data(self):
        scanners = self.scanner_service.get_scanners()
        self.assertTrue(len(scanners) == 2)

    def test_get_scanner_by_name(self):
        scanner0 = self.scanner_service.get_scanner_by_name("Local")
        scanner1 = self.scanner_service.get_scanner_by_name("Outscan")
        self.assertEqual(scanner0.xid, 0)
        self.assertEqual(scanner1.xid, 2)

    def test_get_scanner_by_id(self):
        scanner0 = self.scanner_service.get_scanner_by_id(0)
        scanner2 = self.scanner_service.get_scanner_by_id(2)
        self.assertEqual(scanner0.xid, 0)
        self.assertEqual(scanner2.xid, 2)






