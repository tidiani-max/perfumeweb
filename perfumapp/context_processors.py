# myapp/context_processors.py
from .models import Profile

def owner_exists(request):
    return {
        'owner_exists': Profile.objects.filter(is_owner=True).exists()
    }
