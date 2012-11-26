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
