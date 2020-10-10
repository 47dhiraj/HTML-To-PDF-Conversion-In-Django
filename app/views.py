from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def index(request):						
	context = {}
	return render(request, 'app/index.html', context)



def render_to_pdf(template_src, context_dict={}):				
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {											
	"company": "HITMAN 47 Company",
	"address": "Kathmandu",
	"city": "Jingalala",
	"state": "Mingalala",
	"zipcode": "98471",


	"phone": "9816666666",
	"email": "hitman47@gmaily.com",
	"website": "hitman47.com",
	}


class ViewPDF(View):										
	def get(self, request, *args, **kwargs):				

		pdf = render_to_pdf('app/pdf_template.html', data)				
		return HttpResponse(pdf, content_type='application/pdf')		



class DownloadPDF(View):
	def get(self, request, *args, **kwargs):				
		
		pdf = render_to_pdf('app/pdf_template.html', data)    	

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response									



