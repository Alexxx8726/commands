from django.db import models

class GithubCommand(models.Model):
    # We use db_table so Django looks for your manually created table
    command = models.CharField(max_length=100)
    description = models.TextField()
    

    class Meta:
        managed = False  # Tells Django: "I created this table manually, don't delete it!"
        db_table = 'github_commands'

    def __str__(self):
        return self.command


class DjangoCommand(models.Model):
    command = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False  # Still using your manual table
        db_table = 'django_commands'

    def __str__(self):
        return self.command

class PostgresCommand(models.Model):
    command = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False  # Still using your manual table
        db_table = 'postgres_commands'

    def __str__(self):
        return self.command