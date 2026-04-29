from django.db import models

class Resource(models.Model):
    # Added all your requested resource types here
    RESOURCE_TYPES = [
        ('books', 'Books'),
        ('review', 'Book Review'),
        ('notes', 'Notes'),
        ('paper', 'Question Paper'),
        ('module', 'Learning Modules'),
    ]

    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    class_level = models.CharField(max_length=10)
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES)
    pdf_file = models.FileField(upload_to='pdfs/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        