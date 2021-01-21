from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    roll20_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
        
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='None')
    likes = models.ManyToManyField(User, related_name='blog_post')
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
        
    def total_likes(self):
        return self.likes.count()
        
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)

#5e models

class Bonus(models.Model):
    name = models.CharField(max_length=10, choices = [('STR','STR'),('DEX','DEX'),('CON','CON'),('INT','INT'),('WIS','WIS'), ('CHA','CHA'), ('ANY','ANY')])
    value = models.IntegerField(choices = [(-2,'-2'),(-1,'-1'),(1,'1'),(2,'2')])
    
    def __str__(self):
        return self.name + '+('+ str(self.value) + ')'

class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)
    spellcasting = models.BooleanField(default=False)
    desc = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    custom = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(choices = [(0, '0'), (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'), (9,'9')])
    time = models.CharField(max_length=100, default='Action', choices = [('24 Hours','24 Hours'),('12 Hours','12 Hours'),('8 Hours','8 Hours'),('1 Hour','1 Hour'),('10 Minutes', '10 Minutes'),('1 Minute','1 Minute'),('Action','Action'),('Reaction','Reaction'),('Bonus','Bonus')])
    school = models.CharField(max_length=100, choices = [('Abjuration','Abjuration'),('Conjuration','Conjuration'),('Divination','Divination'),('Enchantment','Enchantment'),('Evocation','Evocation'),('Illusion','Illusion'),('Necromancy','Necromancy'),('Transmutation', 'Transmutation')])
    concentration = models.BooleanField(default=False)
    ritual = models.BooleanField(default=False)
    range = models.CharField(max_length=100, choices = [('Special','Special'),('Unlimited','Unlimited'),('500 miles', '500 miles'),('Sight','Sight'), ('1 mile','1 mile'), ('1000 feet','1000 feet'),('500 feet','500 feet'),('300 feet','300 feet'),('150 feet','150 feet'),('120 feet','120 feet'),('90 feet','90 feet'),('60 feet','60 feet'),('30 feet','30 feet'),('15 feet','15 feet'),('10 feet','10 feet'),('5 feet','5 feet'),('Touch','Touch'),('Self','Self')])
    v = models.BooleanField(default=False)
    s = models.BooleanField(default=False)
    m = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, default='Instantaneous', choices = [('Instantaneous','Instantaneous'),('1 Round','1 Round'),('1 Minute','1 Minute'), ('10 Minutes','10 Minutes'),('1 Hour','1 Hour'), ('8 Hours','8 Hours'), ('24 Hours','24 Hours'), ('Special','Special'), ('Permament','Permament')])
    desc = RichTextField(blank=True, null=True)
    classes = models.ManyToManyField(Class, related_name='class_spells')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    custom = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class Feat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    prerequisite = models.CharField(max_length=100, default='-')
    desc = RichTextField()
    bonuses = models.ManyToManyField(Bonus, related_name='feat_bonuses', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    custom = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bonuses = models.ManyToManyField(Bonus, related_name='race_bonuses')
    size = models.CharField(max_length=100, choices = [('Tiny', 'Tiny'),('Small', 'Small'),('Medium','Medium'),('Large','Large')])
    speed = models.IntegerField()
    desc = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    custom = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
  
#site features for 5e

class Character(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, default="Human", on_delete=models.SET_DEFAULT)
    story = RichTextField(blank=True, null=True)
    starting_class =  models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    feats = models.ManyToManyField(Feat, related_name='character_feats', blank=True)
    spells = models.ManyToManyField(Spell, related_name='character_spells', blank=True)
    user_access = models.ManyToManyField(User, related_name='character_acc')
    
    def __str__(self):
        return self.name + ' | ' + str(self.author)
    
class Journal(models.Model):
    title = models.CharField(max_length=100)
    desc = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    user_access = models.ManyToManyField(User, related_name='journal_acc', blank=True)
    
    def __str__(self):
        return self.title

class JournalPost(models.Model):
    journal = models.ForeignKey(Journal, related_name="journal_posts", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.journal)
    