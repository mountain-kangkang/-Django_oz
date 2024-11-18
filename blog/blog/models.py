from django.db import models

# 제목
# 본문
# 작성자
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

    created_at = models.DateTimeField("작성일자",auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)

    class Meta:
        verbose_name = "블로그"
        verbose_name_plural = "블로그 목록"