from django.shortcuts import render
from datatable.models import EmbedError
from datatable.tables import EmbedErrorTable


# Data Table section
def embed_err(request):
    table = EmbedErrorTable()
    return render(request, "embed_error.html", {'embed_error': table})
