import os
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Matin_First_Project.settings')

import django
django.setup()

from First_app.models import Topic, AccessRecord, Webpage

fakegen = Faker()

topics = ['economy', 'news', 'math', 'chemistry']

def Add_Topics():

    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]

    t.save()

    return t;

def populate(number = 10):

    for num in range(number):

        addition = Add_Topics()

        fake_url = fakegen.url()

        fake_date = fakegen.date()

        fake_name = fakegen.company()

        w = Webpage.objects.get_or_create(topic = addition, url = fake_url, name= fake_name)[0]

        a = AccessRecord.objects.get_or_create(name= w, date = fake_date)[0]


if __name__ == '__main__':

    print('population Script')

    populate()

    print('population complete')
