import data
import unittest


class TestCases(unittest.TestCase):

    def test_point1(self):
        point1 = data.Point(420, 69, 666)
        self.assertAlmostEqual(point1.x, 420)
        self.assertAlmostEqual(point1.y, 69)
        self.assertAlmostEqual(point1.z, 666)

    def test_point2(self):
        point2 = data.Point(42069, 270, 6363)
        self.assertAlmostEqual(point2.x, 42069)
        self.assertAlmostEqual(point2.y, 270)
        self.assertAlmostEqual(point2.z, 6363)

    def test_vector(self):
        vector1 = data.Vector(3.3, 5.5, 6.6)
        self.assertAlmostEqual(vector1.x, 3.3)
        self.assertAlmostEqual(vector1.y, 5.5)
        self.assertAlmostEqual(vector1.z, 6.6)

    def test_vector2(self):
        vector2 = data.Vector(789, 456, 123)
        self.assertAlmostEqual(vector2.x, 789)
        self.assertAlmostEqual(vector2.y, 456)
        self.assertAlmostEqual(vector2.z, 123)

    def test_ray1(self):
        ray1 = data.Ray(data.Point(12, 24, 36), data.Vector(48, 60, 72))
        self.assertAlmostEqual(ray1.pt.x, 12)
        self.assertAlmostEqual(ray1.pt.y, 24)
        self.assertAlmostEqual(ray1.pt.z, 36)
        self.assertAlmostEqual(ray1.dir.x, 48)
        self.assertAlmostEqual(ray1.dir.y, 60)
        self.assertAlmostEqual(ray1.dir.z, 72)

    def test_ray2(self):
        ray2 = data.Ray(data.Point(8, 16, 24), data.Vector(32, 40, 48))
        self.assertAlmostEqual(ray2.pt.x, 8)
        self.assertAlmostEqual(ray2.pt.y, 16)
        self.assertAlmostEqual(ray2.pt.z, 24)
        self.assertAlmostEqual(ray2.dir.x, 32)
        self.assertAlmostEqual(ray2.dir.y, 40)
        self.assertAlmostEqual(ray2.dir.z, 48)

    def test_sphere1(self):
        sphere1 = data.Sphere(data.Point(40, 20, 500), 5)
        self.assertAlmostEqual(sphere1.center.x, 40)
        self.assertAlmostEqual(sphere1.center.y, 20)
        self.assertAlmostEqual(sphere1.center.z, 500)
        self.assertAlmostEqual(sphere1.radius, 5)

    def test_sphere2(self):
        sphere2 = data.Sphere(data.Point(45, 665, 419), 68)
        self.assertAlmostEqual(sphere2.center.x, 45)
        self.assertAlmostEqual(sphere2.center.y, 665)
        self.assertAlmostEqual(sphere2.center.z, 419)
        self.assertAlmostEqual(sphere2.radius, 68)




if __name__ == '__main__':
    unittest.main()
