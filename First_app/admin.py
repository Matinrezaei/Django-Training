from django.contrib import admin
from First_app.models import AccessRecord, Topic, Webpage, UserProfileInfo

# admin.site.register(User)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)

