import unittest
import logging
import logging.config
import sys
import os
from configparser import ConfigParser
from outpost24hiabclient.clients.hiabclient import HiabClient

class TestOutpost24Hiab(unittest.TestCase):

    def setUp(self):
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger('simple')
        mode = os.environ["SYNC_MODE"]
        config = ConfigParser()
        config.read('config.ini')
        
        if mode not in config:
            logger.error("Please set SYNC_MODE environment variable to 'production' or 'acceptance' according to 'config.ini'")
            sys.exit(1)

        op24_url = config[mode]['op24_url']
        op24_token = os.environ['OP24_TOKEN']
        self.hiabclient = HiabClient(op24_url, op24_token)

    @unittest.skip("Skip - remove this line if you have an Outpost24 HIAB test instance")
    def test_Users(self):
        usergroups = self.hiabclient.get_usergroups()
        user = self.hiabclient.create_user("testuser123_firstname", "testuser123_lastname", "testuser123@testuser123.com", "612950589", "nl", "testuser123", "testuser123password@#", usergroupliststr = str(usergroups[0].xid), allscanners = True)
        isdeleted = self.hiabclient.delete_users(str(user.xid))

        self.assertEqual(user.vcfirstname, 'testuser123_firstname')
        self.assertEqual(user.vclastname, 'testuser123_lastname')
        self.assertEqual(user.vcusername, 'TESTUSER123')
        self.assertTrue(isdeleted)
       
    @unittest.skip("Skip - remove this line if you have an Outpost24 HIAB test instance")
    def test_Targets(self):
        targetgroup = self.hiabclient.get_targetgroups()[0]
        scanner = self.hiabclient.get_scanners()[0]
        tg = ["test.outpost24.com"]
        targets = self.hiabclient.create_targets(tg, targetgroup, False, scanner)
        isdeleted = self.hiabclient.delete_targets(targets)

        self.assertEqual(targets[0].hostname, 'test.outpost24.com')
        self.assertTrue(isdeleted)

    @unittest.skip("Skip - remove this line if you have an Outpost24 HIAB test instance")
    def test_Targetgroups(self):
        targetgroup = self.hiabclient.create_targetgroup("test1")
        isdeleted = self.hiabclient.delete_targetgroups([targetgroup])
        
        self.assertEqual(targetgroup.name, 'test1')
        self.assertTrue(isdeleted)

if __name__ == '__main__':
    unittest.main()
