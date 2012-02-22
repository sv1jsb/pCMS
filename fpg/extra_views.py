import re
from django.db.models import Q
from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from elFinder import connector as api
from django.utils import simplejson as json
from django.http import HttpResponse
from fpg.models import Flatpage

def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'content',])
        if not request.user.is_authenticated():
            found_entries = Flatpage.objects.filter(entry_query).filter(published=True).filter(registration_required=False)
        else:
            found_entries = Flatpage.objects.filter(entry_query).filter(published=True)
    return render_to_response('search_results.html',
            { 'query_string': query_string, 'found_entries': found_entries },
        context_instance=RequestContext(request))

@login_required
def elfinder_mce(request):
    return render_to_response('elfinder_mce.html',{'user':request.user,'STATIC_URL':settings.STATIC_URL,'MEDIA_URL':settings.MEDIA_URL,'MEDIA_ROOT':settings.MEDIA_ROOT})

@csrf_exempt
@login_required
def elfinder_connector_mce(request):
    try:
        finder = api(settings.ELFINDER_MCE)
    except:
        response = {}
        response['error'] = 'Invalid backend configuration'
        return HttpResponse(json.dumps(response),mimetype='application/json')

    if request.POST:
        if "cmd" in request.POST and request.POST["cmd"] == "upload":
            request.POST['upload[]'] = request.FILES.getlist('upload[]')

        finder.run(request.POST)
        return HttpResponse(json.dumps(finder.httpResponse))

    finder.run(request.GET)

    ret = HttpResponse(mimetype=finder.httpHeader["Content-type"])

    if finder.httpHeader["Content-type"] == "application/json":
        ret.content = json.dumps(finder.httpResponse)
    else:
        ret.content = finder.httpResponse

    for head in finder.httpHeader:
        if head != "Content-type":
            ret[head] =  finder.httpHeader[head]
    ret.status_code = finder.httpStatusCode
    return ret
