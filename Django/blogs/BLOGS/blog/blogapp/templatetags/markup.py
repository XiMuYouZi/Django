# coding=utf-8
from django import template
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown2(value):
    try:
        import markdown2
    except ImportError:
        if settings.DEBUG:
            raise template.TemplateSyntaxError("Error in 'markdonw' filter: The Python markdown2 library isn't install.")
        return force_text(value)
    else:
        return mark_safe(markdown2.markdown(force_unicode(value),
                                            safe_mode=True,
                                            extras=["code-friendly",]))




# from markdown import markdown
# # 作为合法的标签库，模块需要包含一个名为register的模块级变量。
# # 这个变量是template.Library的实例，是所有注册标签和过滤器的数据结构。
# #  所以，请在你的模块的顶部插入如下语句：
# from django import template
# register = template.Library()
# # 以上语句
# @register.filter(name="markdown2")
# def markdown2(value):
#     return markdown(value)