from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    # Définition des choix pour le champ Types_de_machines
    CHOIX_DISTRIBUTEURS = [
        ('autres', 'Autres'),
        ('casiers', 'Casiers'),
        ('circuits_courts', 'Circuits courts'),
        ('distributeur_pains', 'Distributeur pains'),
        ('distributeur_epicerie', 'Distributeur épicerie'),
        ('distributeur_boisson_snacking', 'Distributeur boisson et snacking'),
        ('distributeur_traiteur', 'Distributeur traiteur'),
        ('distributeur_cbd', 'Distributeur CBD'),
        ('distributeur_charcuterie', 'Distributeur charcuterie'),
        ('distributeur_salle_sport', 'Distributeur Salle Sport'),
        ('distributeur_viandes', 'Distributeur Viandes'),
        ('distributeur_fromages', 'Distributeur Fromages'),
        ('distributeur_non_alimentaire', 'Distributeur non alimentaire'),
        ('frigo_connecte', 'Frigo connecté'),
    ]

    types_de_machines = forms.ChoiceField(label="Types de machines", choices=CHOIX_DISTRIBUTEURS)

    class Meta:
        model = Contact
        fields = ['société', 'nom', 'prénom', 'email', 'téléphone', 'code_postal', 'ville', 'message', 'types_de_machines', 'j_accepte_d_etre_contacte']
