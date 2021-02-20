import csvproject as cs
import os


def test_pytestworking():
    assert 1 == 1


def test_csvsort():
    comparelist1 = []
    comparelist2 = []
    cs.csvsort('test_inputfile.txt', 'test_outputfile.txt', 1)
    foo = open('test_outputfile.txt', 'r')
    prefoo = open('test_inputfile.txt', 'r')
    for column in foo:
        comparelist1.append(column)
    for line in prefoo:
        comparelist2.append(line)
    assert comparelist1 == comparelist2


def test_emptyfile():
    cs.csvsort('troll.txt', 'test_outputfile.txt', 0)
    assert os.stat('test_outputfile.txt').st_size == 0
