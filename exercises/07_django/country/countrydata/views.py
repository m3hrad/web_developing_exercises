from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
import json

from .models import Continent, Country


def continent_json(request, continent_code):

    """ Write your answer in 7.2 here. """
    #dicts
    #dump
    callBack = request.GET.get('callback', "-1")
    my_json_data = continent_code
    country =Continent.objects.filter(code=continent_code)
    get_object_or_404(country)
    countries = country.values('countries')
    #test= countries[1].get("countries")
    #return HttpResponse(my_json_data, content_type="application/json")
    response_data={}
    for id in country.values('countries'):
        #test += str(id.get("countries"))
        #id.get("countries")
        eachCountry = Country.objects.filter(pk=id.get("countries"))
        get_object_or_404(eachCountry)
        eachCode = eachCountry.values("code")[0].get("code")
        eachName = eachCountry.values("name")[0].get("name")
        response_data[eachCode] = eachName;

    #return HttpResponse(json.dumps(response_data), content_type="application/json")
    if (callBack != "-1"):
        response_D = callBack + '(' + str(json.dumps(response_data)) + ')'
        return HttpResponse(response_D, content_type="application/json")
    else:
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    #raise Http404("Not implemented")


def country_json(request, continent_code, country_code):
    """ Write your answer in 7.2 here. """
    country =Country.objects.filter(code=country_code)
    get_object_or_404(country)
    response_data = {}
    response_data['area'] = country.values('area')[0].get("area")
    response_data['population'] = country.values('population')[0].get('population')
    response_data['capital'] = country.values('capital')[0].get('capital')

    #return HttpResponse(my_json_data, content_type="application/json")
    continentPk = country.values('continent')[0].get('continent')
    continentObject = Continent.objects.filter(pk=continentPk)
    continentCodeFromDB = continentObject.values('code')[0].get("code")
    if(continentCodeFromDB == continent_code):
        callBack = request.GET.get('callback', "-1")

        if (callBack != "-1"):
            response_D = callBack + '(' + str(response_data) + ')'
            return HttpResponse(response_D, content_type="application/json")
        else:
            return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        raise Http404("wrong continent")
