from collections import namedtuple

Transaction = namedtuple(
    'Transaction', [
        'amount',
        'name',
        'iban',
        'reference',
        'datetime',
        'datestart',
        'currency',
        'after_balance',
        'before_balance',
        'type',
        'card',
        'id',
    ])
