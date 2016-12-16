from django.conf.urls import url

from core.views import MainPageTemplateView
urlpatterns = [
    url(r'^$', MainPageTemplateView.as_view(), name='home'),

]
# from profile_info.views import ProfileMyMarksTemplateView, ProfileMarksForMeTemplateView, ProfileTemplateView
#
# urlpatterns = [
#
#     url(r'^$', ProfileTemplateView.as_view(), name="all"),
#     url(r'marks/my/$', ProfileMyMarksTemplateView.as_view(), name="my"),
#     url(r'marks/for_me/$', ProfileMarksForMeTemplateView.as_view(), name="for_me"),
#
# ]
