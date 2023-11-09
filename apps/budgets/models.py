from django.db import models

# Create your models here.
"""
    TODO:
         - カテゴリ(Category)
         - 収入(income)
            - 固定(fixation)
            - 変動(change)
         - 支払い(payment)
            - 固定(fixation)
            - 変動(change)
        - 貯蓄(savings)
"""

class IncomeCategory(models.Model):
    """ Class IncomeCategory
       TODO:
             - カテゴリ名(name)
    """
    name = models.CharField('カテゴリ名', max_length=32)
    def __str__(self):
        return self.name

class Income(models.Model):
    """ Class Income
        TODO:
             - 日付(Date)
             - 金額(Price)
             - カテゴリ(Category)
             - 摘要(description)
    """
    date = models.DateField('日付')
    price = models.IntegerField('金額')
    description = models.TextField('摘要')
    pass

class paymentCategory(models.Model):
        """ Class Income
        TODO:
             - カテゴリ名(name)
        """
        name = models.CharField('カテゴリ名', max_length=32)
         = 
class payment(models.Model):
        """ Class Income
        TODO:
             - 日付(Date)
             - 金額(Price)
             - カテゴリ(Category)
             - 摘要(description)
        """
