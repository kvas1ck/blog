from django.db import models
from django.conf import settings
from django.urls import reverse

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status = 'published', published_at__isnull=False)

    def with_related(self):
        return self.select_related('author','category').prefetch_related('tag')

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=70,unique=True)


    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=70,unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    objects = PostQuerySet.as_manager()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220,unique=True)
    excerpt = models.CharField(max_length=200,blank=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,related_name= 'posts',null=True,blank=True)
    tag = models.ManyToManyField(Tag, related_name='posts', blank=True)
    status = models.CharField(max_length=10, choices=Status.choices,default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    published_at = models.DateTimeField(blank= True, null=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

