from django.contrib import admin
from django.contrib import admin
from .models import Perfume, Profile, Testimony

# Register your models here.

# Register the Perfume model with a custom display
@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Display name and price in the list view
    search_fields = ('name',)  # Search by perfume name
    list_filter = ('price',)  # Filter by price range

# Register the Profile model to manage owner status
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_owner')  # Display user and owner status in list view
    list_filter = ('is_owner',)  # Enable filtering by owner status
    search_fields = ('user__username',)  # Enable search by username

    # Allow the admin to set or change the owner status in the list view
    list_editable = ('is_owner',)

    # Prevent more than one owner from being set accidentally
    def save_model(self, request, obj, form, change):
        if obj.is_owner:
            # If setting this user as owner, unset is_owner for other users
            Profile.objects.filter(is_owner=True).update(is_owner=False)
        super().save_model(request, obj, form, change)

@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimony')  # Display name and price in the list view
    search_fields = ('name',)  # Search by perfume name
    