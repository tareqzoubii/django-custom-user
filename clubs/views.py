from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Clubs


class ClubsListView(ListView):
    template_name = "clubs/clubs-list.html"
    model = Clubs


class ClubsDetailView(DetailView):
    template_name = "clubs/clubs-detail.html"
    model = Clubs


class ClubsCreateView(CreateView):
    template_name = "clubs/clubs-create.html"
    model = Clubs
    fields = ['club_name', 'league_name', 'trophies', 'purchaser']


class ClubsUpdateView(UpdateView):
    template_name = "clubs/clubs-update.html"
    model = Clubs
    fields = ['club_name', 'league_name', 'trophies', 'purchaser']


class ClubsDeleteView(DeleteView):
    template_name = "clubs/clubs-delete.html"
    model = Clubs
    success_url = reverse_lazy("clubs-list")