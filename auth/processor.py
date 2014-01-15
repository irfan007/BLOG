from auth.models import UserProfile



def current_user(req):
    
    try:
        if req.user.is_superuser:
            superUP=UserProfile()
            superUP.user=req.user
            superUP.image=None
            return {'UP':superUP}
        else:
            return {'UP':UserProfile.objects.get(user=req.user)}
    except:
        return {}



