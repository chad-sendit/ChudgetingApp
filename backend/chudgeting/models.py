from django.db import models

# Create your models here.
class RecurringIncome(models.Model):
    # Pay Frequency Choices
    FREQUENCY_CHOICES = [
        (1, "Weekly"),
        (2, "Biweekly"),
        (3, "Monthly"),
    ]

    # Pay Day Choices
    DAY_CHOICES = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]

    income_source = models.CharField(max_length=255)  # E.g. Venmo, Work
    description = models.CharField(max_length=255)
    first_pay_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.IntegerField(choices=FREQUENCY_CHOICES)
    pay_day = models.IntegerField(choices=DAY_CHOICES, blank=True, null=True) # Optional week date

    def __str__(self):
        return f"{self.income_source} - {self.description}: $ {self.amount}"
class SingleIncome(models.Model):
    income_source = models.CharField(max_length=255)  # E.g. Venmo, Work
    description = models.CharField(max_length=255)  
    date_received = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.income_source} - {self.description}: $ {self.amount}"
class RunningExpense(models.Model):
    vendor_name = models.CharField(max_length=255)
    transaction_date = models.DateField()
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.transaction_date} - {self.category} - {self.amount}"
class MonthlyRecurringExpense(models.Model):
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class YearlyRecurringExpense(models.Model):
    description = models.CharField(max_length=255)
    due_month = models.CharField(max_length=20)  # E.g., "January", "February", etc.
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.amount}"