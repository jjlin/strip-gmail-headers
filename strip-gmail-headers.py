#!/usr/bin/env python
#
# 05/30/2011: Initial revision.
#
import re
import sys

# Open HTML file.
html_file = open(sys.argv[1], 'rb')
html = html_file.read()
html_file.close()

# Delete: onload="Print()"
target = ' onload="Print()"'
start = html.find(target)
end = start + len(target)
html = html[:start] + html[end:]

# Delete: First <table ...> to the next <table ...> (exclusive)
regex = re.compile(
    r'('       # Begin match group.
    r'<table ' # First opening tag.
    r'.+?'     # Everything up to the next <table> (non-greedy).
    r')'       # End match group.
    r'<table ' # Next opening tag (not included in the match).
    ,
    re.DOTALL
)
match = regex.search(html)
(start, end) = (match.start(1), match.end(1))
html = html[:start] + html[end:]

# Delete: Next two <tr> to </tr>
regex = re.compile(
    r'('     # Begin match group.
    r'<tr>'  # Opening angle bracket and tag name.
    r'.+?'   # Everything up to the next </tr> (non-greedy).
    r'</tr>' # Closing tag.
    r')'     # End match group.
    ,
    re.DOTALL
)
for count in range(2):
    match = regex.search(html)
    (start, end) = (match.start(1), match.end(1))
    html = html[:start] + html[end:]

# Delete: Last <hr>
target = '<hr>'
start = html.rfind(target)
end = start + len(target)
html = html[:start] + html[end:]

# Write out the result.
html_file = open(sys.argv[1], 'wb')
html_file.write(html)
html_file.close()
