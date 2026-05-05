Installation et développement local
-------------------------------------

Prérequis
~~~~~~~~~

- Compte GitHub avec accès en lecture à ce dépôt
- Git CLI
- SQLite3 CLI
- Python 3.6 ou supérieur

Cloner le dépôt
~~~~~~~~~~~~~~~

.. code-block:: bash

   cd /path/to/put/project/in
   git clone https://github.com/MithrandirEa/OC-P13-Lettings.git
   cd OC-P13-Lettings

Créer et activer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**macOS / Linux :**

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate

**Windows (PowerShell) :**

.. code-block:: powershell

   python -m venv venv
   .\venv\Scripts\Activate.ps1

Installer les dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install -r requirements.txt

Variables d'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~

Créez un fichier ``.env`` à la racine du projet en vous basant sur l'exemple ci-dessous :

.. code-block:: ini

   SECRET_KEY=votre_clé_secrète_django
   SENTRY_DSN=votre_dsn_sentry         # optionnel
   ENVIRONMENT=development              # ou "production"
   APP_VERSION=0.1.0

Lancer le serveur de développement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python manage.py runserver

Rendez-vous ensuite sur http://localhost:8000.

Linting
~~~~~~~

.. code-block:: bash

   flake8

Tests
~~~~~

.. code-block:: bash

   pytest

Pour générer un rapport de couverture :

.. code-block:: bash

   pytest --cov=. --cov-report=html

Le rapport HTML est généré dans le dossier ``htmlcov/``.

Panel d'administration
~~~~~~~~~~~~~~~~~~~~~~

Accessible à l'adresse http://localhost:8000/admin.

- Utilisateur : ``admin``
- Mot de passe : ``Abc1234!``

Base de données (SQLite3)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sqlite3 oc-lettings-site.sqlite3

Commandes utiles depuis le shell SQLite3 :

.. code-block:: sql

   .tables
   .quit

Créez un compte administrateur avec : ``python manage.py createsuperuser``
