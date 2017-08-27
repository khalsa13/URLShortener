from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'127', settings.ROOT_URLCONF, name='127'),
    #host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
)