from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from books.models import Book
from contact.forms import  ContactForm
from django.http import HttpResponse
import csv
import reportlab
from reportlab.pdfgen import canvas
from cStringIO import StringIO


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


def my_image(request):
    image_data = open("/media/psf/Django/Django/mysite/mysite/media/1.jpg", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")


UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]
def unruly_passengers_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'
    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response


def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    temp=StringIO()
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(temp)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(10,0, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response