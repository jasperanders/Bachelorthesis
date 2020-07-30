import os
import sys

path = sys.argv[1]
i = open(f'./{path}', 'r')
o = open('./Thesis/md/needCitation.md', 'w')
print('file is open\nlooking...')
o.write('# Citations Needed for\n\n')

sentence_for_citation = []
current_section = 'no section'

for line in i:  
  if '#' in line:
    current_section = line.replace('#', '')
    o.write(f'## {current_section} \n')
  
  sentences = line.split('.')

  for current_sentence in sentences:
    if '<cite>' in current_sentence:
      write = current_sentence.replace('<cite>', '').rstrip().lstrip()
      o.write(
        f'- [] {write}\n\n'
      )

o.close()
i.close()
print('written and closed')
