from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from engine import calculate_sentiment
from random import random
from statistics import mean
from DatabaseFunctions import *
from django.contrib.auth import login as login_check
from mongoengine.queryset import DoesNotExist
from mongoengine.django.auth import User


def index(request):
    return render(request, 'index.html', {'products': return_all_products()})


def add_user_new(request):
    try:
        User.objects.get(username=request.POST['username'])
    except DoesNotExist:
        try:
            add_user(request.POST['username'], request.POST['password'])
            return render(request, 'index.html')
        except Exception:
            return HttpResponse("Add Failed")


def login_check(request):
    try:
        user = User.objects.get(username=request.POST['username'])
        if check_user(user, request.POST['password']):
            user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            print login(request, user)
            request.session.set_expiry(60 * 60 * 1)
            print "rer"
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('login failed')
    except DoesNotExist:
        return HttpResponse('user does not exist')


def add_new_product(request):
    product_name = request.POST['product_name']
    product_features = []
    i = 0
    try:
        # to get multiple product features
        while request.POST['product_feature' + str(i)] or i < 3:
            product_features.append(request.POST['product_feature' + str(i)])
            i += 1
    except Exception as e:
        print "some : " + str(e)
    print product_features
    add_product_and_feature(request.user.username, product_name, product_features)

    return HttpResponseRedirect("/dashboard/")


def engine(request):
    product_name = request.GET['product_name']
    product = return_product(product_name, request.user.username).first()
    features = return_feature_for_product(request.user.username, product_name)
    return render(request, 'engine.html', {'product_name': product_name, 'features': features, 'product': product})


def pricing(request):
    return HttpResponse("Sixth sheikh of the shiekhs shakes when the sheiks shakes")


def about(request):
    return HttpResponse("About is empty when the content is about to empty the about content")


def dashboard(request):

    return render(request, 'dashboard.html', {'data': return_all_products_data(request.user.username)})


def delete_product(request):
    remove_product(request.user.username, request.GET.get('product_name', ''))


def process(request):
    product_name = request.GET.get('product_name', 'iphone')
    product_feature = request.GET.get('product_feature', 'camera')
    tweet_limit = 100

    print product_name, product_feature, tweet_limit
    print "Received GET Request"
    mean1 = calculate_sentiment(product_name, product_feature, tweet_limit)
    t = []
    t.append((mean1/6)*1)
    t.append(mean1)
    return render(request, 'process.html', {'sentiment_data': t})


def custom_survey(request):
    return HttpResponse("Custom Survey")


