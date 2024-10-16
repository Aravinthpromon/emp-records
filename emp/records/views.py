from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import data  # Change Product to data
import json

@csrf_exempt
def data_list(request):
    if request.method == 'GET':
        # Get all data entries and convert them to a list of dictionaries
        data_entries = list(data.objects.values())
        return JsonResponse(data_entries, safe=False)

    elif request.method == 'POST':
        # Parse the JSON data from the request body
        data_dict = json.loads(request.body)
        # Create a new data entry
        data_entry = data.objects.create(
            empname=data_dict['empname'],
            role=data_dict['role'],
            salary=data_dict['salary'],
            experience=data_dict['experience']
        )
        # Return the ID of the created entry with a 201 status code
        return JsonResponse({'id': data_entry.id}, status=201)

@csrf_exempt
def data_detail(request, data_id):
    try:
        # Fetch the specific data entry by ID
        data_entry = data.objects.get(id=data_id)
    except data.DoesNotExist:
        # Return a 404 error if the data entry is not found
        return JsonResponse({'error': 'Data not found'}, status=404)

    if request.method == 'GET':
        # Return the details of the data entry as JSON
        return JsonResponse({
            'empname': data_entry.empname,
            'role': data_entry.role,
            'salary': str(data_entry.salary),
            'experience': data_entry.experience,
            'created_at': data_entry.created_at,
            'updated_at': data_entry.updated_at
        })

    elif request.method == 'PUT':
        # Parse the JSON data from the request body
        data_dict = json.loads(request.body)
        # Update the data entry with new values
        data_entry.empname = data_dict.get('empname', data_entry.empname)
        data_entry.role = data_dict.get('role', data_entry.role)
        data_entry.salary = data_dict.get('salary', data_entry.salary)
        data_entry.experience = data_dict.get('experience', data_entry.experience)
        data_entry.save()
        # Return the ID of the updated entry with a 200 status code
        return JsonResponse({'id': data_entry.id}, status=200)

    elif request.method == 'DELETE':
        # Delete the data entry
        data_entry.delete()
        # Return a message indicating the deletion with a 204 status code
        return JsonResponse({'message': 'Data deleted'}, status=204)
