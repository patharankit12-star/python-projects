# regualar Expressions in match same alimate find from paragraph with location 

import re

pattern=r"[A-Z]inestro"
text = '''"Sinestro Corps War" is an American comic book 
crossover event published by DC Comics in its Green Lantern
and Green Lantern Corps titles. Written by Geoff Johns (pictured) 
 and Dave Gibbons, and drawn by Ivan Reis, Patrick sinestro Dinestro Gleason, and Ethan
Van Sciver, the 11-part saga was published between June and December 
2007 with a main storyline, four supplemental "Tales of the Sinestro Corps"
 one-shot specials and a Blue Beetle tie-in issue concurrently released.
The story centers on the Green Lantern Corps' interstellar war against 
the Sinestro Corps, led by Sinestro, who seek a universe ruled through fear. 
The 1986 "Tales of the Green Lantern Corps" story was the thematic basis of the storyline.
 Critical and fan reception to "Sinestro Corps War" was positive. Many reviewers ranked
   it among the top comic books of the year and the storyline's first issue garnered
 a 2008 Eisner Award nomination. The storyline was a financial success and several
   issues underwent multiple printings. (Full article...)'''
# use in keyword also
# stop first accurence 
# if not find print None
match = re.search(pattern,text)
print(match)
print("all maches")
matches = re.finditer(pattern,text)

for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])