from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns = [
    path("",views.homepage,name='homepage'),
    path("Login",views.user_login ,name='login-page'),
    path("Signup",views.signup, name='signup'),
    path("Home",views.notes,name='note-home'),
    path("Add-Notes",views.add_notes,name='Add-Notes'),
    path("View-Notes/<int:id>",views.view_notes,name='View-Notes'),
    path('Logout',views.logout_view,name='logout-app'),
    path('Delete-Note/<int:id>',views.note_delete,name='delete-note'),
    path('Edit-note/<int:id>',views.edit_note,name='edit-note'),
    path('.*', RedirectView.as_view(url='/', permanent=False), name='homepage'),
    
]
