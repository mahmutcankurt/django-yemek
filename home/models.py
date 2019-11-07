from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.category_name

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='post', verbose_name='Kategoriler')
    title = models.CharField(max_length=200, blank=False, verbose_name='Başlık')
    image = models.FileField(upload_to='images/', default=True)
    text = RichTextField()
    slug = models.SlugField(unique=True,null=True, editable=False, max_length=130,)
    draft = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, auto_now=True)


    class Meta:
        verbose_name_plural = 'Gönderiler'
        verbose_name = 'Gönderiler'
        ordering = ['-created_date']
        get_latest_by = ['title']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Post, self).save(*args, **kwargs)
