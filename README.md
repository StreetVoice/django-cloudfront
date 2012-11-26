CloudFront Private content signing for Django
=============================================

usage:

    import cloudfront
    cloudfront.sign(url, secs)


add these two settings in settings.py

    CLOUDFRONT_KEY_PAIR_ID = 'your_key_pair_id'
    CLOUDFRONT_PRIVATE_KEY = 'your_private_key'
