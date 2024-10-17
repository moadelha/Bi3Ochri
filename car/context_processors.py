# This file is needed for  passing variable to base.html
from .models import Car, Privacy, Ads

"""
def ad_processor(request):
    popup_ad = Ads.objects.all()
    return {
        'ad' : popup_ad[0]
    }
"""
def ad_processor(request):
    popup_ad = Ads.objects.all()
    if popup_ad:
        return {'ad': popup_ad[0]}
    else:
        return {}  # Return an empty dictionary if no ads exist