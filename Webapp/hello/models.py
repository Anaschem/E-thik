from django.db import models

class Contact(models.Model):
    # Définition des choix pour le champ Types_machine
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

    société = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prénom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    téléphone = models.CharField(max_length=15)
    code_postal = models.CharField(max_length=10, blank=True, null=True)
    ville = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    types_de_machines = models.CharField(max_length=100, choices=CHOIX_DISTRIBUTEURS, default='autres')
    j_accepte_d_etre_contacte = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prénom}"
