Description du projet
---------------------

Orange County Lettings est un site web développé avec le framework Django permettant de
consulter des locations immobilières et des profils d'utilisateurs.

Le projet est découpé en trois applications Django indépendantes :

- **oc_lettings_site** : application principale gérant la page d'accueil, la configuration et le routage global.
- **lettings** : application gérant la liste et le détail des locations.
- **profiles** : application gérant la liste et le détail des profils utilisateurs.

Technologies utilisées
~~~~~~~~~~~~~~~~~~~~~~

- **Python** 3.6+
- **Django** 6.0
- **SQLite3** (base de données)
- **Sentry** (monitoring des erreurs en production)
- **pytest** (tests automatisés)
- **flake8** (analyse statique du code)
- **Sphinx** (documentation)
