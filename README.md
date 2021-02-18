# 5eStuff Website
This is my simple website project made with django-python with sqlite database (and ofcourse html).  
It shares data about the tabletop RPG game _Dungeons&Dragons_, giving users a possibility to create their own content.  
This website: 
 - uses simple user authentication system, 
 - displays, sorts and filters some basic datasets, 
 - allows users to create posts, comment and like on built-in forum
 - create user-shared journals and personal (shared only by the link and only for chosen registered users) characters using collected data
 
 Note: It is uploaded as a debug version with some sample data. Example screenshots below.

## Env setup and hotfixes

```bash
pip install django==3.1.6
pip install django-filter
pip install django-chosen
pip install django-ckeditor
```

After imports in the file src\django-chosen\chosen\widgets.py add:
```python
def unicode(x):
    return str(x)
```
And change file src\django-chosen\chosen\forms.py to:
```python
from .fields import *
from .widgets import *
```
In the end change the following line in  src\django-chosen\chosen\fields.py
```python
from widgets import ChosenSelect, ChosenSelectMultiple, ChosenGroupSelect
```
to
```python
from .widgets import ChosenSelect, ChosenSelectMultiple, ChosenGroupSelect
```
## Website view

![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/image.png?raw=true "Homepage")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/auth.png?raw=true "Authoristation")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/spells.png?raw=true "Listing Data")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/view.png?raw=true "View Button")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/forum.png?raw=true "Forum")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/post.png?raw=true "Example Post")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/journal.png?raw=true "Journals")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/character.png?raw=true "Create Character")
![alt text](https://github.com/kozakusek/pictures/blob/main/stuff5e/char.png?raw=true "View Character")
