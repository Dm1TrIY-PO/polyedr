import unittest
from unittest.mock import patch, mock_open
from shadow.mod_polyedr import Polyedr


class TestModPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        first_fake_file_content = """200.0   20.0    90.0 0.0
6       5       18
0.0     0.0     0.0
1.0     0.0     0.0
0.5     0.866   0.0
0.0     0.0     1.0
1.0     0.0     1.0
0.5     0.866   1.0
3       1    2    3
3       4    5    6
4       1    2    5    4
4       2    3    6    5
4       3    1    4    6"""
        first_fake_file_path = 'data/prism.geom'
        with patch('shadow.mod_polyedr.open'.format(__name__),
                   new=mock_open(read_data=first_fake_file_content)) as _file:
            cls.first_poly = Polyedr(first_fake_file_path)
            _file.assert_called_once_with(first_fake_file_path)

        second_fake_file_content = """200.0   60.0   30.0 0.0
8       6       24
-0.5    -0.5    0.5
-0.5    0.5     0.5
0.5     0.5     0.5
0.5     -0.5    0.5
-0.5    -0.5    -0.5
-0.5    0.5     -0.5
0.5     0.5     -0.5
0.5     -0.5    -0.5
4       1    2    3    4
4       5    6    2    1
4       3    2    6    7
4       7    8    4    3
4       8    5    1    4
4       6    5    8    7"""
        second_fake_file_path = 'data/new_cube.geom'
        with patch('shadow.mod_polyedr.open'.format(__name__),
                   new=mock_open(read_data=second_fake_file_content)) as _file:
            cls.second_poly = Polyedr(second_fake_file_path)
            _file.assert_called_once_with(second_fake_file_path)

        third_fake_file_content = """200.0   30.0   60.0  30.0
6       8       24
0.0     0.0     1.0
0.0     0.0     -1.0
1.0     0.0     0.0
-1.0    0.0     0.0
0.0     1.0     0.0
0.0     -1.0    0.0
3       1    3    5
3       1    3    6
3       1    4    5
3       1    4    6
3       2    3    5
3       2    3    6
3       2    4    5
3       2    4    6
"""
        third_fake_file_path = 'data/octahedron.geom'
        with patch('shadow.mod_polyedr.open'.format(__name__),
                   new=mock_open(read_data=third_fake_file_content)) as _file:
            cls.third_poly = Polyedr(third_fake_file_path)
            _file.assert_called_once_with(third_fake_file_path)

    # призма, повернутая боком, у которой не видно 5 ребер, два повернуты
    # под углом 80 градусов к горизонтали, ещё два под углом 40 градусов и одно
    # горизонтальное длины 200 под углом 0 градусов с центром вне ед. куба
    def test_first_mod_par(self):
        self.first_poly.shadow()
        self.assertEqual(self.first_poly.find_mod_par(), 200.0)

    def test_second_mod_par(self):
        self.second_poly.shadow()
        self.assertEqual(round(self.second_poly.find_mod_par(), 3), 373.927)

    def test_third_mod_par(self):
        self.third_poly.shadow()
        self.assertEqual(round(self.third_poly.find_mod_par(), 2), 836.56)
