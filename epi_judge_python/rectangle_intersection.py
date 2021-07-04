import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))
Line = collections.namedtuple('Line', ('x', 'width'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # TODO - you fill in here.
    lx_1, ly_1 = Line(r1.x, r1.width), Line(r1.y, r1.height)
    lx_2, ly_2 = Line(r2.x, r2.width), Line(r2.y, r2.height)
    result = []
    for l, m in [(lx_1, lx_2), (ly_1, ly_2)]:
        if l.x > m.x:
            l,m = m,l
        if is_overlapping(l, m):
            result.append(overlapping_line(l,m))
        else:
            return Rect(0, 0, -1, -1)
    return Rect(
        result[0].x,
        result[1].x,
        result[0].width,
        result[1].width,
    )


def is_overlapping(l1: Line, l2: Line) -> bool:
    # Assume lines are ordered by bottom-left origin.
    return l1.x + l1.width >= l2.x


def overlapping_line(l1: Line, l2: Line) -> Line:
    return Line(l2.x, min(l1.width - l2.x + l1.x, l2.width))


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
