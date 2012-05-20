#!/usr/bin/env python

import re
import sys

# Check arguments.
if len(sys.argv) != 2:
    print "Usage: %s <gmail_msg_html_file>" % sys.argv[0]
    sys.exit(1)

# Open HTML file.
html_file = open(sys.argv[1], 'rb')
html = html_file.read()
html_file.close()

# Delete: onload="Print()"
target = ' onload="Print()"'
start = html.find(target)
end = start + len(target)
html = html[:start] + html[end:]

# Delete: Next two <table> to </table>
regex = re.compile(
    r'('        # Begin match group.
    r'<table '  # Opening tag.
    r'.+?'      # Everything up to the next </table> (non-greedy).
    r'</table>' # Closing tag.
    r')'        # End match group.
    ,
    re.DOTALL
)
for count in range(2):
    match = regex.search(html)
    (start, end) = (match.start(1), match.end(1))
    html = html[:start] + html[end:]

# Delete: Next two <hr>
target = '<hr>'
for count in range(2):
    start = html.find(target)
    end = start + len(target)
    html = html[:start] + html[end:]

# Delete: Next two <tr> to </tr>
regex = re.compile(
    r'('     # Begin match group.
    r'<tr>'  # Opening tag.
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

# Write out the result.
html_file = open(sys.argv[1], 'wb')
html_file.write(html)
html_file.close()
