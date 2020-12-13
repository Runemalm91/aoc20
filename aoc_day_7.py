#!/usr/bin/env python3
import sys
import re


def parse_rule(rule, regexp_matcher):
    # Assumes a certain rule structure, see input file.
    bag, bag_rule = rule.split(" bags contain ")

    if bag_rule[0] == "no":
        return bag, [(0, "" )]

    matches = re.findall(regexp_matcher, bag_rule)
    bag_content = [(int(amount), bag_in_bag) for amount, bag_in_bag in matches]

    return bag, bag_content


class RuleGraph():

    def __init__(self):
        self._graph = {}
        self._regexp = re.compile(r"(\d+) (\S+ \S+)")

    def append_rule(self, rule):
        bag, bag_content = parse_rule(rule, self._regexp)
        try:
            self._graph[bag].append(list(set(bag_content)))
        except KeyError:
            self._graph[bag] = bag_content

    @property
    def graph(self):
        return self._graph


def find_bags_in_bag(rules, bag):
    can_contain_bag = set()
    for new_bag, bag_contents in rules.items():
        if bag in [bag_content for _, bag_content in bag_contents]:
            can_contain_bag.add(new_bag)
            can_contain_bag.update(find_bags_in_bag(rules, new_bag))

    return can_contain_bag


def recursively_find_amount_of_bags(rules, bag):
    n = 0
    for nr_of_bags, inner_bag in rules[bag]:
        n += nr_of_bags
        n += nr_of_bags * recursively_find_amount_of_bags(rules, inner_bag)

    return n


def find_bags_for_shiny_gold(rules):
    can_contain_shiny_gold = find_bags_in_bag(rules, 'shiny gold')
    return can_contain_shiny_gold

def main():
    with open("aoc_day_7_data.txt", "r") as f:
        rules = f.readlines()
        rule_graph = RuleGraph()
        for rule in rules:
            rule_graph.append_rule(rule)
        bags = find_bags_for_shiny_gold(rule_graph.graph)
        number_of_bags_in_shiny_gold = recursively_find_amount_of_bags(
            rule_graph.graph, 'shiny gold')

        print('Number of bags that, eventually, can' +
              f' hold a shiny gold bag is: {len(bags)}')
        print('Number of bags that are required inside' +
              f' my shiny gold bag is: {number_of_bags_in_shiny_gold}')


if __name__ == '__main__':
    sys.exit(main())
