from django.db import migrations

def populate_universities(apps, schema_editor):
    University = apps.get_model('userprofiles', 'University')
    
    universities = [
        # Public Universities
        ('University of Ghana', 'UG', 'Accra'),
        ('Kwame Nkrumah University of Science and Technology', 'KNUST', 'Kumasi'),
        ('University of Cape Coast', 'UCC', 'Cape Coast'),
        ('University of Education, Winneba', 'UEW', 'Winneba'),
        ('University for Development Studies', 'UDS', 'Tamale'),
        ('University of Mines and Technology', 'UMaT', 'Tarkwa'),
        ('University of Health and Allied Sciences', 'UHAS', 'Ho'),
        ('University of Energy and Natural Resources', 'UENR', 'Sunyani'),
        ('Ghana Institute of Management and Public Administration', 'GIMPA', 'Accra'),
        ('University of Professional Studies', 'UPSA', 'Accra'),
        ('Ghana Communication Technology University', 'GCTU', 'Accra'),
        ('SD Dombo University of Business and Integrated Development Studies', 'SDD-UBIDS', 'Wa'),

        # Technical Universities
        ('Accra Technical University', 'ATU', 'Accra'),
        ('Kumasi Technical University', 'KsTU', 'Kumasi'),
        ('Cape Coast Technical University', 'CCTU', 'Cape Coast'),
        ('Takoradi Technical University', 'TTU', 'Takoradi'),
        ('Sunyani Technical University', 'STU', 'Sunyani'),
        ('Ho Technical University', 'HTU', 'Ho'),
        ('Tamale Technical University', 'TaTU', 'Tamale'),
        ('Koforidua Technical University', 'KTU', 'Koforidua'),
        ('Bolgatanga Technical University', 'BTU', 'Bolgatanga'),

        # Private Universities
        ('Ashesi University', 'Ashesi', 'Berekuso'),
        ('Central University', 'CU', 'Accra'),
        ('Valley View University', 'VVU', 'Accra'),
        ('Methodist University College Ghana', 'MUCG', 'Accra'),
        ('Presbyterian University College', 'PUC', 'Abetifi'),
        ('Catholic University College of Ghana', 'CUCG', 'Sunyani'),
        ('All Nations University', 'ANU', 'Koforidua'),
        ('Academic City University College', 'ACity', 'Accra'),
        ('Regent University College of Science and Technology', 'Regent', 'Accra'),
        ('Wisconsin International University College', 'WIUC', 'Accra'),
        ('Islamic University College', 'IUC', 'Accra'),
        ('Lancaster University Ghana', 'LUG', 'Accra'),
        ('Webster University Ghana', 'WUG', 'Accra'),
        ('Ghana Baptist University College', 'GBUC', 'Kumasi'),
        ('Garden City University College', 'GCUC', 'Kumasi'),
        ('Christian Service University College', 'CSUC', 'Kumasi'),
        ('Pentecost University', 'PU', 'Accra'),
        ('Regional Maritime University', 'RMU', 'Accra'),
        ('Ghana Christian University College', 'GCUC', 'Amrahia'),
        ('Knutsford University College', 'KUC', 'Accra'),
        ('Ghana Institute of Journalism', 'GIJ', 'Accra'),
        ('BlueCrest University College', 'BUC', 'Accra'),
        ('Data Link University College', 'DUC', 'Tema'),
        ('Ghana Institute of Languages', 'GIL', 'Accra'),
        ('Ghana Institute of Management and Technology', 'GIMT', 'Accra'),
        ('African University College of Communications', 'AUCC', 'Accra'),
        ('Christ Apostolic University College', 'CAUC', 'Kumasi'),
        ('Good News Theological Seminary', 'GNTS', 'Accra'),
        ('Heritage Christian University College', 'HCUC', 'Accra'),
        ('Kings University College', 'KUC', 'Accra'),
        ('Legacy University College', 'LUC', 'Accra'),
    ]

    for name, abbr, location in universities:
        University.objects.create(name=name, abbreviation=abbr, location=location)

def reverse_func(apps, schema_editor):
    University = apps.get_model('userprofiles', 'University')
    University.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_universities, reverse_func),
    ] 