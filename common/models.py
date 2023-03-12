from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()

WORK_TYPE_CHOISE = [
    ('dry', 'Химчистка'),
]


class Work(models.Model):
    work_type = models.CharField(
        'Вид работы', max_length=30, choices=WORK_TYPE_CHOISE)
    count = models.IntegerField(verbose_name='Количесво', default=1)
    user = models.ForeignKey(verbose_name='Исполнитель',
                             to=USER, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.work_type} {self.user.get_username()} ({self.count})'

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
