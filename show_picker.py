#!/usr/bin/python

import random
import tvdb_api
import sys

def pick_show(show_name):
    t = tvdb_api.Tvdb()
    show = t[show_name]
    season = random.choice([i for i in show.keys() if i > 0])
    episode = show[season][random.choice(show[season].keys())]

    return episode

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print pick_show(sys.argv[1])
    else:
        best_shows = []
        f = open('best.txt')
        for line in f:
            best_shows.append(line)
        show = random.choice(best_shows)
        print show
        print pick_show(show)

