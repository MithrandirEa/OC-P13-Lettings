Architecture des applications
------------------------------

Application principale — ``oc_lettings_site``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L'application principale orchestre le projet. Elle contient :

- la page d'accueil (``/``) ;
- la configuration globale dans ``settings.py`` ;
- le routage principal dans ``urls.py``, qui délègue aux deux sous-applications ;
- les templates de base (``base.html``, ``index.html``, ``404.html``, ``500.html``).

Routes principales
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - URL
     - Description
   * - ``/``
     - Page d'accueil du site
   * - ``/admin/``
     - Interface d'administration Django
   * - ``/lettings/``
     - Liste des locations
   * - ``/lettings/<id>/``
     - Détail d'une location
   * - ``/profiles/``
     - Liste des profils
   * - ``/profiles/<username>/``
     - Détail d'un profil

Application ``lettings``
~~~~~~~~~~~~~~~~~~~~~~~~~

Gère l'affichage des biens immobiliers disponibles à la location.

Vues
^^^^

- ``index(request)`` : retourne la liste de toutes les locations
  (template ``lettings/index.html``).
- ``letting(request, letting_id)`` : retourne le détail d'une location
  identifiée par son ``id`` (template ``lettings/letting.html``).

Application ``profiles``
~~~~~~~~~~~~~~~~~~~~~~~~~

Gère l'affichage des profils utilisateurs.

Vues
^^^^

- ``index(request)`` : retourne la liste de tous les profils
  (template ``profiles/index.html``).
- ``profile(request, username)`` : retourne le détail du profil d'un utilisateur
  identifié par son ``username`` (template ``profiles/profile.html``).
