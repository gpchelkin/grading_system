from django.views.generic import ListView

from marks.forms import CreateNPDMarkForm
from npd.models import NPD


class NPDListView(ListView):
    model = NPD

    def get_context_data(self, **kwargs):
        data = super(NPDListView, self).get_context_data()
        form = CreateNPDMarkForm()
        data.update({'form': form})
        return data
