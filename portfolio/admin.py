from django.contrib import admin
from .models import Project, Skill, Service, Testimonial, ContactInfo, SocialLink, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order')
    list_filter = ('is_featured',)
    search_fields = ('title', 'tech_stack')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured', 'order')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'is_active')
    list_editable = ('is_active',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass # Sirf 1 hi record banega

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')