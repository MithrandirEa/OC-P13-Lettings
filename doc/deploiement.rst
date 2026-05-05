Déploiement et CI/CD
---------------------

Pipeline CI/CD
~~~~~~~~~~~~~~

Le projet utilise un pipeline d'intégration et de déploiement continu.
Les grandes étapes sont :

1. **Linting** : vérification de la qualité du code avec ``flake8``.
2. **Tests** : exécution de la suite de tests avec ``pytest`` et mesure de la couverture.
3. **Build Docker** : construction d'une image Docker de l'application.
4. **Push Docker Hub** : publication de l'image sur Docker Hub.
5. **Déploiement** : mise en production sur la plateforme cible.

Le pipeline se déclenche automatiquement à chaque push sur les branches suivantes :

- ``master`` / ``main`` : déploiement complet en production.
- Autres branches : uniquement linting et tests.

Variables d'environnement requises en production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``SECRET_KEY``
     - Clé secrète Django (ne jamais exposer)
   * - ``DEBUG``
     - Doit être ``False`` en production
   * - ``ALLOWED_HOSTS``
     - Liste des domaines autorisés
   * - ``SENTRY_DSN``
     - DSN Sentry pour le monitoring des erreurs
   * - ``ENVIRONMENT``
     - Valeur ``production``
   * - ``APP_VERSION``
     - Version de l'application déployée

Monitoring des erreurs — Sentry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sentry est intégré au projet pour capturer et surveiller les erreurs en production.
Il est configuré dans ``oc_lettings_site/settings.py`` via la variable d'environnement
``SENTRY_DSN``.

En l'absence de cette variable, Sentry est désactivé (utile en développement local).

Lancer l'application avec Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker pull <votre-image>:latest
   docker run -p 8000:8000 \
       -e SECRET_KEY=... \
       -e SENTRY_DSN=... \
       -e ENVIRONMENT=production \
       <votre-image>:latest
