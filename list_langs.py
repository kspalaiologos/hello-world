#!/usr/bin/env python3

import os

readme = open('README.md', 'w')

# Copy template to README
with open('README_nolist.md', 'r') as temp:
  for line in temp:
    readme.write(line)

# Write title
readme.write('\n### This repository currently contains "Hello World" programs in the following languages:\n')

# List the available languages
for dir in os.listdir('.'):
  if not (dir == '.' or dir == '..' or dir[0] == '.' or os.path.isfile(dir)):
    for file in os.listdir(dir):
      if os.path.isfile(os.path.join(dir, file)):
        lang = ''
        for str in file[0:(len(file) if file.find('.') == -1 else file.find('.'))].replace('-', ' ').replace('_', ' ').split():
          lang += str.capitalize() + ' '
        readme.write('* [{}]({})\n'.format(lang[:-1], os.path.join(dir if dir != "#" else "%23", file))) # Cut trailing space

readme.close()
