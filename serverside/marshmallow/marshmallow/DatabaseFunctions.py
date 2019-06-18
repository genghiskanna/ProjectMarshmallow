from mongoengine import *
from models import *
from mongoengine.django.auth import User as use

connect('marshmallow_database')


def add_user(username, password):
    new_user = use()
    new_user.username = username
    new_user.password = password
    new_user.save()


def add_product_and_feature(username, product_name, product_features):
    print "adding products"
    try:
        new_product = Products()
        new_product.product_name = product_name
        new_product.product_owner = username
        new_product.save()
        for product_feature in product_features:
            new_feature = Features()
            new_feature.name = product_feature
            new_feature.product_id = new_product
            new_feature.save()
            del new_feature
        print new_product.product_name
    except Exception as e:
        print str(e)


def add_feature(product_name, product_feature):
    product = Products.objects(product_name=product_name)

    new_feature = Features()
    new_feature.name = product_feature
    new_feature.product_id = product


def return_product(name, user):
    product = Products.objects(product_name=name, product_owner=user)
    return product


def return_all_products_data(username):
    products = []
    for loop in Products.objects(product_owner=username):
        products.append(loop)
        print loop.product_name

    return products


def return_feature_for_product(username, product_name):
    features = []
    product = Products.objects(product_name=product_name, product_owner=username).first()
    for loop in Features.objects(product_id=product):
        features.append(loop)

    return features


def return_all_products():
    products = []
    for loop in Products.objects():
        products.append(loop)
    return products


def remove_product(username, product_name):
    product = Products.objects(product_name=product_name, product_owner=username)
    product.delete()


def check_user(user, password):
    if user.password == password:
        return True
    else:
        False


def return_user(name):
    return use.objects(username=name)
