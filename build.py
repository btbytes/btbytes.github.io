#!/usr/bin/env python

"""
Read all the markdown files in the content directory iteratively into subdirectories,
and populate sqlite table named 'content' with the following columns:
    - title
    - date (use git to read the original date)
    - updated (use git to read the last updated date)
    - content (the markdown content)
    - url (use the filename as the url, minus the .md part)
    - tags (use the tags in the markdown file)
    - category (use the directory name as the type)
    - properties (key-value pairs read from the top of the file)

read title from the YAML frontmatter.
properties is a dictionary read from the YAML frontmatter
"""
