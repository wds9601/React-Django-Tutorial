from django.urls import path
from .views import RoomView, CreateRoomView

# this file controls the url endpoints, sending the app the proper file
# when the url endpint is hit

urlpatterns = [
    # path('', main)  # since argument is blank string = "domain.com/..."
                    # when any url endpint is hit, dispatch to views and run "main" function
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view())
]