from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300, help_text="Short description for the project card")
    description = models.TextField(help_text="Detailed description for the project detail page")
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True, null=True)
    tech_stack = models.CharField(max_length=300, help_text="Comma separated, e.g. Django, React, PostgreSQL")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text="Smaller numbers show up first")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class Skill(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Python, Django, JavaScript")
    percentage = models.IntegerField(help_text="Skill level from 0 to 100")
    icon_class = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. fa-brands fa-python")
    
    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

    class Meta:
        ordering = ['-percentage']


class Service(models.Model):
    title = models.CharField(max_length=150, help_text="e.g. Web Development, API Development")
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class e.g. fa-solid fa-code", blank=True)
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True, null=True)
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    review = models.TextField()
    rating = models.IntegerField(default=5, help_text="Rating from 1 to 5")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Review by {self.client_name}"


class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"


class SocialLink(models.Model):
    platform = models.CharField(max_length=50, help_text="e.g. GitHub, LinkedIn, Twitter")
    url = models.URLField()
    icon_class = models.CharField(max_length=100, help_text="FontAwesome icon class e.g. fa-brands fa-github")
    
    def __str__(self):
        return self.platform


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"