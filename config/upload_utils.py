import os
from uuid import uuid4

def upload_equipamento(instance, filename):
	upload_to = 'equip_files/{}'.format(instance.id)
	field = 'equipamento'
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}_{}.{}'.format(field,instance.id,ext)
	else:
		filename = '{}.{}'.format(uuid4().hex, ext)
	return os.path.join(upload_to, filename)