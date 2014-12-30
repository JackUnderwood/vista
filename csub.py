__author__ = 'John'
from base import UI
import asub
import bsub


class C(UI):
    override = {
        'login': ("Type", "path2", "John Underwood"),
    }
    asub.A(override)
    bsub.B()

    runtime = {
        'deep': ("Click", "path_14", ""),
        'advance': ("Type", "path_15", "Candy"),
        'drop2': ("Select", "path_16", "Top Select"),
        'submit': ("Click", "path_17", "")
    }
    UI().update(runtime)
    order = ('deep', 'advance', 'drop2', 'submit')
    UI().execute(order)

