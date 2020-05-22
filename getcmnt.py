# -*- coding: utf-8 -*-
"""Parse Python source code from file and get/print source code comments."""

__all__ = ('get_comments', 'get_comment_blocks')

import tokenize

from io import StringIO


def get_comments(source):
    """Parse Python source and yield comment tokens in the order of
    appearance.
    Each token is a tuple with the comment string, start and end.
    start and end each are tuples with the line number and column of
    the start and end of the comment.
    `source` may be a file-like object with a `readline` method or
    a string.
    """
    if not hasattr(source, 'readline'):
        source = StringIO(source)

    tokenizer = tokenize.generate_tokens(source.readline)
    for token in tokenizer:
        if token[0] == tokenize.COMMENT:
            yield token[1:4]


def get_comment_blocks(source):
    """Parse Python source code and yield a tuple of comment string,
    start and end for each comment.
    *source* may be a file-like object with a ``readline`` method or
    a string.
    Comments on consecutive lines, which start on the same column,
    are returned as a single string with embedded newlines.
    """
    comments = []

    for comment, start, end in get_comments(source):
        if (not comments or comments[-1][1][0] == start[0] - 1
                and comments[-1][1][1] == start[1]):
            comments.append((comment, start, end))
        else:
            yield "\n".join(c[0] for c in comments), comments[0][1], comments[-1][2]
            comments = [(comment, start, end)]

    if comments:
        yield "\n".join(c[0] for c in comments), comments[0][1], comments[-1][2]


def cmt_input(f1,f2):
    with open(f1) as fp:
        cmnts1 = []
        for comment, start, end in get_comment_blocks(fp):
            cmnts1.append(comment)
    with open(f2) as fp:
        cmnts2 = []
        for comment, start, end in get_comment_blocks(fp):
            cmnts2.append(comment)
    flag = 0
    print()
    print("----- Comment Analysis of " + f1 + " & " + f2 + " -----")
    print()
    print("Comments Identified in "+f1)
    # print(cmnts1)
    count = 1
    flg = 0
    for i in cmnts1:
        print(str(count) + ". " + str(i))
        count += 1
        flg = 1
    if (flg == 0): print("None found")
    count = 1
    print()
    print("Comments Identified in " + f2)
    # print(cmnts2)
    count = 1
    flg = 0
    for i in cmnts2:
        print(str(count) + ". " + str(i))
        count += 1
        flg = 1
    if (flg == 0): print("None found")
    count = 1
    flag=0
    print()
    print("Comments Identified as Common : ")
    for i in cmnts1:
        for j in cmnts2:
            if(i==j):
                flag = 1
                print(str(count) + ". ", end='')
                print(i)
                count += 1
                print()
    count =1
    if(flag==0): print("None found")
