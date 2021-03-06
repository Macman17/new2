# Generated by Django 4.0.5 on 2022-06-15 17:27

from django.db import migrations

from articles.models import Section

def populate_sections(apps, schemaeditor):
    sections = {
        "News": "Check out the news of the day!",
        "Politics": "What's going on in the world of politics?",
        "Personal Finance": "The latest financial news!",
        "Go Gamecocks": "Stay tune for the latest Gamecock news!",
        "Sports": "Today this happen in the world of sports!."
    }
    Section = apps.get_model('articles', 'Section')
    for name, desc in sections.items():
        sect_obj = Section(name=name, description=desc)
        sect_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_sections)
    ]
