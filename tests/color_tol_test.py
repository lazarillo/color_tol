
import unittest
import color_tol.core.funcs as ct


class GenericPaletteTest(unittest.TestCase):
  def setUp(self):
    self.palette = ct._tol_colormap('Qualitative', 5)

  def test_number_of_colors_in_map_should_be_five(self):
    self.assertEqual(5, len(self.palette))

  def test_validate_the_set_of_html_colors(self):
    self.assertEqual(['#332288', '#88CCEE', '#117733', '#DDCC77', '#CC6677'],
                       self.palette.html_colors)

  def test_validate_the_set_of_rgb_colors(self):
    self.assertEqual([(51, 34, 136), (136, 204, 238), (17, 119, 51),
                       (221, 204, 119), (204, 102, 119)],
                      self.palette.rgb_colors)

  def test_validate_color_map_type_is_qualitative(self):
    self.assertEqual('Qualitative', self.palette.map_type)


class ColorPaletteFailAssertions(unittest.TestCase):
  def setUp(self):
    self.palette = ct.qualitative(2)

  def test_number_of_colors_in_map_should_be_two(self):
    self.assertEqual(2, len(self.palette))

  def test_cannot_access_html_color_index_beyond_two(self):
    with self.assertRaises(IndexError):
      self.palette.html_colors[10]

  def test_cannot_access_rgb_color_index_beyond_two(self):
    with self.assertRaises(IndexError):
      self.palette.rgb_colors[10]

class SequentialPaletteTest(unittest.TestCase):
  def setUp(self):
    self.palette = ct.sequential(7)

  def test_number_of_colors_in_map_should_be_seven(self):
    self.assertEqual(7, len(self.palette))

  def test_validate_the_set_of_html_colors(self):
    self.assertEqual(['#FFFBD5', '#FEE391', '#FEC44F', '#FB9A29', '#EC7014',
      '#CC4C02', '#8C2D04'],
                       self.palette.html_colors)

  def test_validate_the_set_of_rgb_colors(self):
    self.assertEqual([(255, 251, 213), (254, 227, 145), (254, 196, 79),
      (251, 154, 41), (236, 112, 20), (204, 76, 2), (140, 45, 4)],
                      self.palette.rgb_colors)

  def test_validate_color_map_type_is_sequential(self):
    self.assertEqual('Sequential', self.palette.map_type)


class DivergingPaletteTest(unittest.TestCase):
  def setUp(self):
    self.palette = ct.diverging(4)

  def test_number_of_colors_in_map_should_be_four(self):
    self.assertEqual(4, len(self.palette))

  def test_validate_the_set_of_html_colors(self):
    self.assertEqual(['#008BCE', '#B4DDF7', '#F9BD7E', '#D03232'],
                       self.palette.html_colors)

  def test_validate_the_set_of_rgb_colors(self):
    self.assertEqual([(0, 139, 206), (180, 221, 247), (249, 189, 126),
      (208, 50, 50)],
                      self.palette.rgb_colors)

  def test_validate_color_map_type_is_sequential(self):
    self.assertEqual('Diverging', self.palette.map_type)

  def test_validate_color_map_type_is_not_reversed(self):
    self.assertEqual(False, self.palette.reversed)


class ReversedPaletteTest(unittest.TestCase):
  def setUp(self):
    self.palette = ct.diverging(4, reverse=True)

  def test_number_of_colors_in_map_should_be_four(self):
    self.assertEqual(4, len(self.palette))

  def test_validate_the_set_of_html_colors(self):
    self.assertEqual(['#D03232', '#F9BD7E', '#B4DDF7', '#008BCE'],
                       self.palette.html_colors)

  def test_validate_the_set_of_rgb_colors(self):
    self.assertEqual([(208, 50, 50), (249, 189, 126), (180, 221, 247),
      (0, 139, 206)],
                      self.palette.rgb_colors)

  def test_validate_color_map_type_is_reversed(self):
    self.assertEqual(True, self.palette.reversed)

if __name__ == '__main__':
  unittest.main()
