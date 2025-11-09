# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_selection, name='course_selection'),

    # MAX курс
    path('max-course/', views.max_course, name='max_course'),
    path('max-course-2/', views.max_course_2, name='max_course_2'),
    path('max-course-3/', views.max_course_3, name='max_course_3'),
    path('max-course-4/', views.max_course_4, name='max_course_4'),
    path('max-course-5/', views.max_course_5, name='max_course_5'),
    path('max-course-6/', views.max_course_6, name='max_course_6'),
    path('max-course-7/', views.max_course_7, name='max_course_7'),
    path('max-course-8/', views.max_course_8, name='max_course_8'),
    path('max-course-9/', views.max_course_9, name='max_course_9'),

    # БАНК курс
    path('bank-course/', views.bank_course, name='bank_course'),
    path('bank-course-2/', views.bank_course_2, name='bank_course_2'),
    path('bank-course-3/', views.bank_course_3, name='bank_course_3'),
    path('bank-course-4/', views.bank_course_4, name='bank_course_4'),
    path('bank-course-5/', views.bank_course_5, name='bank_course_5'),
    path('bank-course-6/', views.bank_course_6, name='bank_course_6'),
    path('bank-course-7/', views.bank_course_7, name='bank_course_7'),
    path('bank-course-8/', views.bank_course_8, name='bank_course_8'),
    path('bank-course-9/', views.bank_course_9, name='bank_course_9'),
    path('bank-course-10/', views.bank_course_10, name='bank_course_10'),

    # ART курс
    path('apt-course/', views.apt_course, name='apt_course'),
    path('apt-course-2/', views.apt_course_2, name='apt_course_2'),
    path('apt-course-3/', views.apt_course_3, name='apt_course_3'),
    path('apt-course-4/', views.apt_course_4, name='apt_course_4'),
    path('apt-course-5/', views.apt_course_5, name='apt_course_5'),
    path('apt-course-6/', views.apt_course_6, name='apt_course_6'),

    # PAT курс
    path('pat-course/', views.pat_course, name='pat_course'),
    path('pat-course-2/', views.pat_course_2, name='pat_course_2'),
    path('pat-course-3/', views.pat_course_3, name='pat_course_3'),
    path('pat-course-4/', views.pat_course_4, name='pat_course_4'),
    path('pat-course-5/', views.pat_course_5, name='pat_course_5'),
    path('pat-course-6/', views.pat_course_6, name='pat_course_6'),
    path('pat-course-final/', views.pat_course_final, name='pat_course_final'),  # ИСПРАВЛЕНО!
]