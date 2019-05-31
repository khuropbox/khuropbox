from django import template

register = template.Library()


@register.inclusion_tag("index.html", takes_context=True)
def load_s3(context):
    request = context['request']
    return {'root' : '-' + str(request.user.username) + '/' }

@register.inclusion_tag("header.html")
def load_s3_header():
    return {}