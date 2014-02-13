# Bootstrap the Sentry environment
from sentry.utils.runner import configure
configure()

# Do something crazy
from sentry.models import Team, Project, ProjectKey, User

user = User()
user.username = 'admin'
user.email = 'admin@localhost'
user.is_superuser = True
user.set_password('admin')
user.save()

team = Team()
team.name = 'Sentry'
team.owner = user
team.save()

project = Project()
project.team = team
project.owner = user
project.name = 'Test'
project.save()

key = ProjectKey.objects.filter(project=project)[0]
print 'SENTRY_DSN = "%s"' % (key.get_dsn(),)