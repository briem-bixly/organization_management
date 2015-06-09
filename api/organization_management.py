# Example API Call
import logging

logging.basicConfig(filename='organization_management.log', level=logging.DEBUG)


def add_department(request):
    if not isinstance(request, Process) and not isinstance(request, NebriOS):
        if request.FORM is not None:
            data = request.FORM.as_dict()
            logging.debug('...')
        else:
            data = request.BODY.as_dict()
            logging.debug('---')
    else:
        data = request.as_dict()
        logging.debug('***')
        
    logging.debug(data)
    
    try:
        org = Process.objects.get(kind="organization")
    except:
        org = Process.objects.create(kind="organization")
        org.save()
    dept = Process.objects.create(PARENT=org, kind="department", name=data['name'])
    dept.save()
