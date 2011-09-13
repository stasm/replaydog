from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from upload.forms import UploadFileForm

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # do stuff with request.FILES['file']
            # redirect to /UUID
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render_to_response('upload/index.html',
                              {'form': form},
                              context_instance=RequestContext(request))
