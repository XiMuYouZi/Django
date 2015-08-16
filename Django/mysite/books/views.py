from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from books.models import Book
from contact.forms import  ContactForm


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})



def thanks(requests):
    return render_to_response('thanks.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/templates/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form': form},context_instance=RequestContext(request))


# def foobar_view(request, template_name):
#     m_list = Book.objects.filter(is_new=True)
#     return render_to_response(template_name, {'m_list': m_list})