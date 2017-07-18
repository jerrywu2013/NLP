```
pip install git+https://github.com/lucasdnd/Wikipedia.
pip install hanziconv
```
```
import wikipedia

wikipedia.set_lang('zh')
ny = wikipedia.page("紐約")
ny.content
x = ny.content
x[0:x.find('，')]
```
```
from hanziconv import HanziConv
print(HanziConv.toTraditional(x))
```
