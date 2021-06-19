from django.contrib.auth.models import User

def decorator(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk==kwargs['pk'])
        if not user == request.user:
            return HttpR
        
    
    
    
    return decorated