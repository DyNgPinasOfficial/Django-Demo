from django.http import JsonResponse
from django.shortcuts import render
from .models import PageVisit

def difficult(request, name):
    page_visit, created = PageVisit.objects.get_or_create(page_name=name)
    
    page_visit.visit_count += 1
    page_visit.save()

    return render(request, 'difficult/message.html', {'recipient_name': name})

def increment_envelope_count(request, name):
    if request.method == 'POST':
        page_visit = PageVisit.objects.filter(page_name=name).first()
        if page_visit:
            page_visit.envelope_open_count += 1
            page_visit.save()
            return JsonResponse({'status': 'success', 'envelope_open_count': page_visit.envelope_open_count})
    return JsonResponse({'status': 'failure'})
