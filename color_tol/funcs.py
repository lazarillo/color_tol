# Create color schemes / palettes based upon the
# excellent work done by Paul Tol at
# personal.sron.nl/~pault/colourschemes.pdf
# (PDF documentation also included in this package.)

import json
import os

#_DATADIR = 'color_tol/color_data'
_DATADIR = os.path.join(os.path.dirname(__file__), 'color_data')
_DATAFILE = os.path.join(_DATADIR, 'color_tol.json')

with open(_DATAFILE, 'r') as color_file:
    COLOR_MAPS = json.load(color_file)

MAP_TYPES = ('Qualitative', 'Sequential', 'Diverging')

class _TolColorMap(object):
    """
    Representation of a color map using Paul Tol's suggestions.

    Parameters
    ----------
    map_type : str
        Type of map. E.g., Qualitative
    colors_html : list
        Colors as list of HTML codes. E.g., [#FF3359, #FFFFFF]
    colors_rgb : list
        Colors as list of 0-255 RGB triplets.
        E.g., [(12, 15, 125), (200, 12, 111)] or [[12, 15, 125], [200, 12, 111]
    num_colors: int
        E.g., 4 (colors in the scale)

    Attributes
    ----------
    map_type : str
    number : int
        Number of colors in color map.
    colors : list
        Colors as list of 0-255 RGB triplets.
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap

    """
    def __init__(self, map_type, colors_html, colors_rgb, reverse=False):
        self._type = map_type
        self._html_colors = colors_html
        self._rgb_colors = [tuple(color_rgb) for color_rgb in colors_rgb]
        self._num_colors = len(colors_html)
        self._reversed = reverse

    @property
    def map_type(self):
        """
        Type of color map, as a string. (e.g. 'Qualitative')

        """
        return self._type

    @property
    def html_colors(self):
        """
        Colors as a list of hex strings. (e.g. ['#A912F4',...])

        """

        return self._html_colors

    @property
    def rgb_colors(self):
        """
        Colors as a list of rgb. (e.g. [(12, 50, 110),...])

        """
        return self._rgb_colors

    @property
    def reversed(self):
        """
        State whether this color map has been reversed or not.

        """
        return self._reversed


    def __len__(self):
        """
        Number of colors in the map, as an integer. (e.g. 5)

        """
        return self._num_colors


def _tol_colormap(map_type, number, reverse=False):
    """
    Return a Paul Tol-type colormap representation of the specified color map.

    Parameters
    ----------
    map_type : From 'Qualitative', 'Sequential', or 'Diverging'
        Select color map type.
    number : int
        Number of defined colors in color map.
    reverse : bool, optional
        Set to True to get the reversed color map.

    Example:
    >>> my_map = _tol_colormap('Sequential', 5)
    >>> my_map.html_colors
    ['#FFFBD5', '#FED98E', '#FB9A29', '#D95F0E', '#993404']
    """
    map_type = map_type[0].capitalize() + map_type[1:].lower()

    # check for valid type
    if map_type not in MAP_TYPES:
        s = 'Invalid map type, must be one of {0}'.format(MAP_TYPES)
        raise ValueError(s)

    # check for valid number
    if number < 1 or number > len(COLOR_MAPS[map_type]):
        s = 'Invalid number for map type {0!r}.\n'
        s = s.format(map_type)
        s += 'Valid numbers are between 1 and {0}'.format(len(COLOR_MAPS[map_type]))
        raise ValueError(s)

    # The color maps are provided in an array that starts with 1
    # color (0 colors doesn't make much sense), so we need to
    # subtract by one to get the proper number of colors.
    colors_html = COLOR_MAPS[map_type][number - 1]['ColorsHTML']
    colors_rgb = COLOR_MAPS[map_type][number - 1]['ColorsRGB']

    if reverse:
        colors_html = [x for x in reversed(colors_html)]
        colors_rgb = [x for x in reversed(colors_rgb)]

    return _TolColorMap(map_type, colors_html, colors_rgb, reverse)

def qualitative(number, reverse=False):
    """
    Return a Paul Tol-type QUALITATIVE colormap. (12 colors max)

    Parameters
    ----------
    number : int
        Number of defined colors in color map.
    reverse : bool, optional
        Set to True to get the reversed color map.

    Example:
    >>> my_map = qualitative(6)
    >>> my_map.html_colors
    ['#332288', '#88CCEE', '#117733', '#DDCC77', '#CC6677', '#AA4499']

    """
    return _tol_colormap('Qualitative', number, reverse)

def sequential(number, reverse=False):
    """
    Return a Paul Tol-type SEQUENTIAL colormap. (9 colors max)

    Parameters
    ----------
    number : int
        Number of defined colors in color map.
    reverse : bool, optional
        Set to True to get the reversed color map.

    Example:
    >>> my_map = sequential(5)
    >>> my_map.html_colors
    ['#FFFBD5', '#FED98E', '#FB9A29', '#D95F0E', '#993404']
    """
    return _tol_colormap('Sequential', number, reverse)

def diverging(number, reverse=False):
    """
    Return a Paul Tol-type DIVERGING colormap. (11 colors max)

    Parameters
    ----------
    number : int
        Number of defined colors in color map.
    reverse : bool, optional
        Set to True to get the reversed color map.

    Example:
    >>> my_map = diverging(4, reverse=True)
    >>> my_map.html_colors
    ['#D03232', '#F9BD7E', '#B4DDF7', '#008BCE']
    """
    return _tol_colormap('Diverging', number, reverse)


