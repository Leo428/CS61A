def num_splits(s: list, d: int) -> int:
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    def helper_part(lst: list):
        # return a list of lists, each list is a unique way to partition lst
        parts = []
        for i in range(len(lst)):
            parts.append([lst[i]])
            rest_parts = [[lst[i]] + p for p in helper_part(lst[i+1:])]
            parts += rest_parts
        return parts
    total = 0
    for part in helper_part(s):
        temp = s[:]
        for p in part:
            temp.remove(p)
        # print('DEBUG: ', 'part: ', part, 'rest: ', temp)
        if abs(sum(part) - sum(temp)) <= d:
            # print('DEBUG: ', 'diff: ', sum(part), sum(temp))
            if len(temp) == 0:
                total += 2
            else:
                total += 1
    return total // 2
    
    
def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    if link is Link.empty:
        raise IndexError
    if index == 0:
        link.first, link.rest = value, Link(link.first, link.rest)
    else:
        insert(link.rest, value, index-1)

# Link Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'