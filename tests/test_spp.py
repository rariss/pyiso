from pyiso_lmp import client_factory
from unittest import TestCase


# class TestSPP(TestCase):
#     def setUp(self):
#         self.c = client_factory('SPP')


#     def test_auth_keys(self):
#         auth, idstr, headers = self.c.auth_keys()
#         self.assertEqual(len(auth), 8)
#         self.assertEqual(len(idstr), 12+50)
#         self.assertIn('set-cookie', headers)

    # def test_fetch_csv(self):
    #     self.c.handle_options(data='gen')
    #     self.c.fetch_csv(*self.c.auth_keys())
