import json

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import RouteForm, StopForm
from .models import Route


class RouteListView(ListView):
    model = Route
    template_name = "planner/route_list.html"
    context_object_name = "routes"


class RouteCreateView(CreateView):
    model = Route
    form_class = RouteForm
    template_name = "planner/route_form.html"
    success_url = reverse_lazy("planner:route_list")


class RouteDetailView(DetailView):
    model = Route
    template_name = "planner/route_detail.html"
    context_object_name = "route"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stops = self.object.stops.all()
        context["stops_json"] = json.dumps(
            [
                {"lat": stop.location.y, "lng": stop.location.x, "name": stop.name}
                for stop in stops
            ]
        )
        context["stop_form"] = StopForm()
        return context


def add_stop_to_route(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == "POST":
        form = StopForm(request.POST)
        if form.is_valid():
            stop = form.save(commit=False)
            stop.route = route
            stop.save()
            return redirect("planner:route_detail", pk=route.pk)
    return redirect("planner:route_detail", pk=route.pk)
