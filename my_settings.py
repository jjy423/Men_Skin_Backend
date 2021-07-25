DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',
        'USER': 'root',
        'PASSWORD' : 'password',
        'HOST':'localhost',
        'PORT': '3306',
    }
}
SECRET_KEY = 'my_settings.SECRET_KEY'