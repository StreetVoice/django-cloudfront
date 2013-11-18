CloudFront Private content signing for Django
=============================================

Installation:

    pip install django-cloudfront


Usage:

    import cloudfront
    cloudfront.sign(url, secs)


Add these two settings in settings.py

    CLOUDFRONT_KEY_PAIR_ID = 'your_key_pair_id'
    CLOUDFRONT_PRIVATE_KEY = 'your_private_key'


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/StreetVoice/django-cloudfront/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

