import random,string
from django.conf import settings

SHORTCODE_MIN=getattr(settings,"SHORTCODE_MIN",8)


def code_generator(size=8,chars=string.ascii_lowercase+string.digits):
    code = ''
    for i in range(size):
        code += random.choice(chars)
    return code

    # or directly return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance,size=8):
    code=code_generator()
    Klass=instance.__class__
    quesrySet=Klass.objects.filter(shortcode=code).exists()
    if quesrySet:
        return create_shortcode(instance,size=size)
    else:
        return code