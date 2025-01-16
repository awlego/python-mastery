
from typing import List

def print_table(seq: List, attr_names: List[str]) -> None:

    header_string = ""
    for attr in attr_names:
        header_string += ('%10s' % attr)
    print(header_string)
    spacer_string = ""
    for attr in attr_names:
        spacer_string += (" " + '-'*9)
    print(spacer_string)

    for obj in seq:
        row_string = ""
        for name in attr_names:
            row_string += ('%10s' % getattr(obj, name))
        print(row_string)

