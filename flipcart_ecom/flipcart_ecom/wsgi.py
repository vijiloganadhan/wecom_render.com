import os; 
from django.core.wsgi import get_wsgi_application; 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipcart_ecom.settings');
import django
from django.core.management import call_command

django.setup()
call_command("migrate", interactive=False)

application = get_wsgi_application()