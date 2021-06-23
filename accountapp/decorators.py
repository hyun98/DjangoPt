from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
<<<<<<< HEAD
            return render(request)
        
    
    
    
=======
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

>>>>>>> 0336da6090023bfd94adec0375bcf27d0ec82c3f
    return decorated
