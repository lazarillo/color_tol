
# color_tol: Colour maps for analysis

This Python package is meant to complement the wonderful work by [Cynthia Brewer](http://colorbrewer2.org/), using the work of [Paul Tol](https://personal.sron.nl/~pault/), where he introduced a very rigorous set of colors that were clearly identifyable for those with or without color-blindness. [His work](https://personal.sron.nl/~pault/colourschemes.pdf) can also be found under the `docs` folder of this package.

-----

## Use

Three different color maps - qualitative, sequential, and diverging - are available, either in RGB or HTML codes.

To access any of them, you call the functions

`qualitative(<number>)`

`sequential(<number>)`

`diverging(<number>)`

where the `<number>` represents the number of colors you wish.

E.g.,

    >>> my_map = qualitative(7)
    >>> my_map.html_colors
    ['#332288', '#88CCEE', '#44AA99', '#117733', '#DDCC77', '#CC6677', '#AA4499']
    
    >>> my_map.rgb_colors
    [(51, 34, 136), (136, 204, 238), (68, 170, 153), (17, 119, 51), (221, 204, 119), (204, 102, 119), (170, 68, 153)]


