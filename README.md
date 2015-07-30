# menu
text base menu system for use in python

if you want generate menu in cycle
```python
from menu import *
  def f(s):
    print s
  m = Menu("Main menu")
  for sub_folder in os.listdir(folder):
      m.addoption(sub_folder, lambda a=sub_folder:f(a))
  m.start()
  ```
