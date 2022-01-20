# -*- coding:utf-8 -*-
"""
参考 https://github.com/seatgeek/thefuzz
"""
__author__ = "aaron.qiu"


from pprint import pprint
from thefuzz import fuzz
from thefuzz import process


if __name__ == '__main__':
    pprint(fuzz.ratio("this is a test", "this is a test!"))
    pprint(fuzz.partial_ratio("this is a test", "this is a test!"))
    pprint(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))
    pprint(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear"))
    pprint(fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
    pprint(fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear"))
    choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
    pprint(process.extract("new york jets", choices, limit=2))
    pprint(process.extractOne("cowboys", choices))
    songs = "/data/soft"
    pprint(process.extractOne("System of a down - Hypnotize - apache", songs))
    process.extractOne("System of a down - Hypnotize - Heroin", songs, scorer=fuzz.token_sort_ratio)