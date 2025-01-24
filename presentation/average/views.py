from django.http import HttpResponse

def average(request, number):
    if number < 1:
        return HttpResponse("Invalid input. Please provide a positive integer.")

    messages = [f"Sorry na x{i}" for i in range(1, number + 1)]
    return HttpResponse("<br>".join(messages))
