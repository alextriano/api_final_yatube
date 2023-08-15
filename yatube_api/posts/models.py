from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
text_limit = 15


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'группа'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)
    image = models.ImageField(
        'Картинка', upload_to='posts/',
        null=True,
        blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'пост'
        default_related_name = 'posts'
        ordering = ('pub_date',)

    def __str__(self):
        return (self.author + "|" + self.text[:text_limit])


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост')

    class Meta:
        verbose_name = 'комментарий'
        default_related_name = 'comments'
        ordering = ('-created',)

    def __str__(self):
        return self.text[:text_limit]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_author_pair')
        ]

    def __str__(self):
        return f'Автор {self.following.id} - Пользователь {self.user.id}'
