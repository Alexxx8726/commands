from django.shortcuts import render
from .models import GithubCommand, DjangoCommand, PostgresCommand # Import your model

# Create your views here.
def index(request):
    return render(request, 'index.html')

def git_commands(request):
    # Fetch all rows from the github_commands table
    all_commands = GithubCommand.objects.all()
    return render(request, 'git_commands.html',{'commands': all_commands} )


def django_cmds(request):
    # Fetch all rows from the django_commands table
    all_django_cmds = DjangoCommand.objects.all()
    
    # Send it to the django_commands.html template
    return render(request, 'django_commands.html', {'commands': all_django_cmds})

def postgres_commands(request):
    # Fetch all rows from the postgres_commands table
    all_postgres_commands = PostgresCommand.objects.all()
    
    # Send it to the postgres_commands.html template
    return render(request, 'postgres_commands.html', {'commands': all_postgres_commands})