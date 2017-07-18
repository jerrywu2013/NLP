pip install git+https://github.com/lucasdnd/Wikipedia.

import wikipedia

wikipedia.set_lang('zh')
ny = wikipedia.page("紐約")
ny.content
x = ny.content
x[0:x.find('，')]
