from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# 제목
# 본문
# 작성자 => 패스(추후 업데이트)
# 작성일자
# 수정일자
# 카테고리

class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free', '자유'),
        ('food', '음식'),
        ('bowling', '볼링'),
        ('coding', '코딩'),
    )

    category = models.CharField("category", max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField('title', max_length=100)
    content = models.TextField("content")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE => 같이 삭제
    # models.PROTECT => 삭제가 불가능함(유저를 삭제하려고 할 때 블로그가 있으면 유저 삭제가 불가능함)
    # models.SET_NULL => 유저 삭제 시 blog 모델의 author가 null이 됨

    created_at = models.DateTimeField("작성일자",auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title}'

    class Meta:
        verbose_name = "블로그"
        verbose_name_plural = "블로그 목록"