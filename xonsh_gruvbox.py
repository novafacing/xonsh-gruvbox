# -*- coding: utf-8 -*-
"""
    pygments.styles.xonsh_gruvbox
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The classic Gruvbox theme for xonsh

    :copyright: Rowan Hart, colorscheme by morhetz
    :license: MIT
"""

from pygments.style import Style
from pygments.token import (Comment, Error, Generic, Name, Number, Operator,
                            String, Text, Whitespace, Keyword)

BLUE_LIGHT = '#83a598'
BLUE = '#458588'
GREEN_LIGHT = '#b8bb26'
GREEN = '#98971a'
YELLOW_LIGHT = '#fabd2f'
YELLOW = '#d79921'
RED_LIGHT = '#fb4934'
RED = '#cc241d'
PURPLE_LIGHT = '#d3869b'
PURPLE = '#b16286'
AQUA_LIGHT = '#8ec07c'
AQUA = '#689d6a'
ORANGE_LIGHT = '#fe8019'
ORANGE = '#d65d0e'
GREY = '#928374'
GREY_LIGHT = '#a89984'
GREY_DARK = '#928374'
FOREGROUND = '#ebdbb2'
BACKGROUND = '#282828'

class GruvboxStyle(Style):
    """
    A readable and contrastful color theme.
    """

    background_color = BACKGROUND

    styles = {
        Comment: 'italic {}'.format(BLUE_LIGHT),
        Comment.Preproc: 'noitalic',
        Comment.Special: 'bold',

        Error: 'bg:{} {}'.format(RED_LIGHT, BACKGROUND),

        Generic.Deleted: 'border: {} bg: {}'.format(RED_DARK, RED_LIGHT),
        Generic.Emph: 'italic',
        Generic.Error: 'RED_LIGHT',
        Generic.Heading: 'bold {}'.format(PURPLE_LIGHT),
        Generic.Inserted: 'border:{} bg:{}'.format(GREEN, GREEN_LIGHT),
        Generic.Output: FOREGROUND,
        Generic.Prompt: 'bold {}'.format(YELLOW_LIGHT),
        Generic.Strong: 'bold',
        Generic.Subheading: 'bold {}'.format(AQUA_LIGHT),
        Generic.Traceback: RED_LIGHT,

        Keyword: 'bold {}'.format(BLUE_LIGHT),
        Keyword.Pseudo: 'nobold',
        Keyword.Type: PURPLE,

        Name.Attribute: 'italic {}'.format(BLUE_LIGHT),
        Name.Builtin: 'bold {}'.format(PURPLE),
        Name.Class: 'underline',
        Name.Constant: AQUA,
        Name.Decorator: 'bold {}'.format(GREEN_LIGHT),
        Name.Entity: 'bold {}'.format(ORANGE_LIGHT),
        Name.Exception: 'bold {}'.format(PURPLE),
        Name.Function: 'bold {}'.format(YELLOW_LIGHT),
        Name.Tag: 'bold {}'.format(YELLOW),
        Number: 'bold {}'.format(GREEN_LIGHT),

        Operator: BLUE_LIGHT,
        Operator.word: 'bold',

        String: GREEN,
        String.doc: 'italic',
        String.Escape: 'bold {}'.format(ORANGE_LIGHT),
        String.Other: AQUA_BOLD,
        String.Symbol: 'bold {}'.format(ORANGE),

        Text: GREY,

        Whitespace: GREY_LIGHT
    }



