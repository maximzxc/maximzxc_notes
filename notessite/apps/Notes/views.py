# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    '''
    home page
    '''
    return render_to_response(
        'base.html', {}, context_instance=RequestContext(request))


def search_form(request):
    return render_to_response(
        'notes/search_form.html', {'status': ''}, context_instance=RequestContext(request))


def search(request):
    if 'range' in request.GET and request.GET['range']:
        rng = request.GET['range']
        if len(rng.split(',')) != 2:
            status = 'Please submit a search term with a range. Like "a, b" where a - min and b - max args'
            return render_to_response(
                'notes/search_form.html', {'status': status}, context_instance=RequestContext(request))
        try:
            first = int(rng.split(',')[0])
            second = int(rng.split(',')[1])
            if second < 0 or first < 0:
                status = 'Error. Your args should be not negative numbers'
                return render_to_response(
                    'notes/search_form.html', {'status': status}, context_instance=RequestContext(request))
            if second < first:
                status = 'Error. Your first argument is less than second: %d < %d' % (first, second)
                return render_to_response(
                    'notes/search_form.html', {'status': status}, context_instance=RequestContext(request))
            if second == first:
                status = 'Error. Your first and second args are equals: %d == %d' % (first, second)
                return render_to_response(
                    'notes/search_form.html', {'status': status}, context_instance=RequestContext(request))
            return render(request, 'notes/search.html', {'first': first,
                                                         'second': second})
        except:
            status = 'Please submit a search term with a range. Like "a, b" where a - min and b - max args'
            return render_to_response(
                'notes/search_form.html', {'status': status}, context_instance=RequestContext(request))
    else:
        status = 'Please submit a search term.'
        return render_to_response(
            'notes/search_form.html', {'status': status}, context_instance=RequestContext(request))
