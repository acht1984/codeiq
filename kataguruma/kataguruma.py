# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, height, weight):
        self.height = int(height)
        self.weight = int(weight)

    def can(self, other):
        return self.height > other.height and self.weight > other.weight

    def pair(self):
        return (self.height, self.weight)

    def __str__(self):
        return "{}, {}".format(self.height, self.weight)


class Relation(object):
    def __init__(self, person, others):
        self.person = person
        self.children = set(o for o in others if person.can(o))
        self.num = len(self.children)

    def __cmp__(self, other):
        # より多く持てる方が大きい
        return self.num - other.num


def create_persons(data):
    return set(Person(*d) for d in data)


def create_relations(persons):
    return (Relation(p, persons - {p}) for p in persons)


def collect(persons):
    relations = create_relations(persons)
    r = max(relations)
    if r.children:
        return [r.person.pair()] + collect(r.children)
    else:
        # 子がいなくなったら終了
        return [r.person.pair()]


def main(fob):
    data = (d.rstrip().split(" ") for d in fob)
    result = collect(create_persons(data))
    for line in result:
        print line

if __name__ == '__main__':
    print "============ small ======================"
    with open("./small.in.txt") as f:
        main(f)
    print "============ large ======================"
    with open("./large.in.txt") as f:
        main(f)
