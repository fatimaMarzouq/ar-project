from django.urls import path

from .views import ( HomePageView,
                     EventListView,
                     EventCreateView,
                     EventUpdateView,
                     EventDetailView,
                     EventDeleteView,
                     AssetListView,
                     AssetCreateView,
                     AssetUpdateView,
                     AssetDetailView,
                     AssetDeleteView,
                     LocationListView,
                     LocationCreateView,
                     LocationUpdateView,
                     LocationDetailView,
                     LocationDeleteView,
                     asset_create)
urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # new
    path('', asset_create),  # new
    path('events/', EventListView.as_view(), name='events'),
    path('assets/', AssetListView.as_view(), name='Assets_list'),
    path('locations/', LocationListView.as_view(), name='location_list'),
    path('new_event/', EventCreateView.as_view(), name='event_new'),
    path('<pk>/edit_event/', EventUpdateView.as_view(), name='event_edit'),
    path('<pk>/event_details', EventDetailView.as_view(), name='event_detail'),
    path('<pk>/delete_event', EventDeleteView.as_view(), name='event_delete'),
    path('new_asset/', AssetCreateView.as_view(), name='Asset_new'),
    path('<pk>/edit_asset/', AssetUpdateView.as_view(), name='Asset_edit'),
    path('<pk>/assets_details', AssetDetailView.as_view(), name='Asset_detail'),
    path('<pk>/delete_asset/',AssetDeleteView.as_view(), name='Asset_delete'),
    path('new_location/', LocationCreateView.as_view(), name='location_new'),
    path('<pk>/edit_location/', LocationUpdateView.as_view(), name='location_edit'),
    path('<pk>/location_details', LocationDetailView.as_view(), name='location_detail'),
    path('<pk>/delete_location/',LocationDeleteView.as_view(), name='location_delete'),
]
