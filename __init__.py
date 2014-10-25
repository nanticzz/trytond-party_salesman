# This file is part of of party_salesman module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .party import *


def register():
    Pool.register(
        Employee,
        PartySalesman,
        Party,
        module='party_salesman', type_='model')
