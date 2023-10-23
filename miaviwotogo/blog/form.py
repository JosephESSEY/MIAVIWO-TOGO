from django import forms
from .models import Article, Profile, Categorie


# option = (
#         ('Agronomie', 'Agronomie'), ('Biologie', 'Biologie'), ('Business', 'Business'), ('Chimie', 'Chimie'), ('Comptabilité', 'Comptabilité'), ('Droit', 'Droit'), ('Economie', 'Economie'),
#         ('Finance', 'Finance'), ('GRH', 'GRH'), ('Geographie', 'Geographie'), ('Histoire', 'Histoire'), ('Informatique', 'Informatique'), ('Langues', 'Langues'),
#         ('Médecine', 'Médecine'), ('Maths', 'Maths'), ('Physique', 'Physique'), ('Statistique', 'Statistique'), 
#     )

option= Categorie.objects.all().values_list('name', 'name')

choice_list = []

for item in option:
    choice_list.append(item)



class BlogForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['contenu', 'domaine', 'is_draft', 'image']


        widgets = {
            'domaine': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
            }
        labels = {
            'is_draft': "Enregistrer comme brouillon",
            'image': "Photo de couverture"
        }
       


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['website', 'bio', 'image']


        



        
    