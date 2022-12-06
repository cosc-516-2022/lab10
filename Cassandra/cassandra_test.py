import unittest

from Cassandra import CassandraDB

class CassandraTest(unittest.TestCase):

    def setUp(self) -> None:
        print()
        print('*'*5 + 'Cassandra test begin' + '*'*5)
        self.client = None

    def test_connect(self):
        self.client = CassandraDB()
        # test
        self.assertIsNotNone(self.client, None)

    def test_load_data(self):
        self.client = CassandraDB()
        self.client.connect()
        self.client.create_table()
        self.client.load_data()

        query_statement = "select * from Customers"
        res = self.client.session.execute(query_statement)

        self.assertEqual(len(res.all()), 2500)

    def test_query_1(self):
        self.client = CassandraDB()
        self.client.connect()
        res = self.client.query_1()
        self.assertEqual(res.all()[0].a, 26)

    def test_query_2(self):
        self.client = CassandraDB()
        self.client.connect()
        res = self.client.query_2()
        # print(len(res.all()))
        # print(str(res))
        self.assertEqual(str(res),"[Row(id='260637', age=35, gender='MALE', num_kids=2), "
                                  "Row(id='660910', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='586079', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='132775', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='282322', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='910326', age=25, gender='MALE', num_kids=3), "
                                  "Row(id='689783', age=35, gender='MALE', num_kids=2), "
                                  "Row(id='449815', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='124145', age=25, gender='MALE', num_kids=4), "
                                  "Row(id='845849', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='343632', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='206606', age=35, gender='MALE', num_kids=1), "
                                  "Row(id='111839', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='797424', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='187546', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='921541', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='788091', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='835258', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='362379', age=35, gender='MALE', num_kids=3), "
                                  "Row(id='890574', age=35, gender='MALE', num_kids=1), "
                                  "Row(id='415434', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='274003', age=25, gender='MALE', num_kids=2), "
                                  "Row(id='782282', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='843192', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='660433', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='760708', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='485604', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='763311', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='307634', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='509413', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='906022', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='513296', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='867327', age=25, gender='MALE', num_kids=4), "
                                  "Row(id='260432', age=25, gender='MALE', num_kids=3), "
                                  "Row(id='187753', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='366126', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='719512', age=25, gender='MALE', num_kids=2), "
                                  "Row(id='852202', age=25, gender='MALE', num_kids=1), "
                                  "Row(id='446167', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='241846', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='949742', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='159444', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='376324', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='964311', age=35, gender='MALE', num_kids=3), "
                                  "Row(id='154517', age=25, gender='MALE', num_kids=2), "
                                  "Row(id='431277', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='783443', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='271951', age=25, gender='MALE', num_kids=4), "
                                  "Row(id='194053', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='688630', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='689019', age=25, gender='MALE', num_kids=3), "
                                  "Row(id='732365', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='784783', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='635091', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='651784', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='371346', age=35, gender='MALE', num_kids=3), "
                                  "Row(id='841699', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='772057', age=25, gender='MALE', num_kids=1), "
                                  "Row(id='349135', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='981262', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='939046', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='405542', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='359968', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='672846', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='374435', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='435329', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='757232', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='187172', age=25, gender='MALE', num_kids=1), "
                                  "Row(id='641830', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='276571', age=25, gender='MALE', num_kids=1), "
                                  "Row(id='493357', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='764457', age=35, gender='MALE', num_kids=4), "
                                  "Row(id='971236', age=25, gender='MALE', num_kids=2), "
                                  "Row(id='343362', age=25, gender='MALE', num_kids=2), "
                                  "Row(id='938852', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='835732', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='771574', age=35, gender='MALE', num_kids=2), "
                                  "Row(id='390643', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='513007', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='622665', age=25, gender='MALE', num_kids=1), "
                                  "Row(id='165666', age=35, gender='MALE', num_kids=1), "
                                  "Row(id='616310', age=25, gender='MALE', num_kids=1), "
                                  "Row(id='943867', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='533283', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='568576', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='162852', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='579117', age=35, gender='MALE', num_kids=2), "
                                  "Row(id='334197', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='247028', age=25, gender='MALE', num_kids=3), "
                                  "Row(id='211582', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='241956', age=35, gender='MALE', num_kids=0), "
                                  "Row(id='603109', age=35, gender='MALE', num_kids=3), "
                                  "Row(id='948809', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='163579', age=35, gender='MALE', num_kids=3), "
                                  "Row(id='160350', age=25, gender='MALE', num_kids=0), "
                                  "Row(id='730487', age=25, gender='MALE', num_kids=4)]")

if __name__ == "__main__":
    unittest.main()