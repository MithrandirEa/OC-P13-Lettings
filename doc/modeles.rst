Modèles de données
-------------------

Application ``lettings``
~~~~~~~~~~~~~~~~~~~~~~~~~

Modèle ``Address``
^^^^^^^^^^^^^^^^^^

Représente une adresse postale associée à une location.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Champ
     - Description
   * - ``number``
     - Numéro de rue (entier positif, max 9999)
   * - ``street``
     - Nom de la rue (max 64 caractères)
   * - ``city``
     - Ville (max 64 caractères)
   * - ``state``
     - État / région (exactement 2 caractères)
   * - ``zip_code``
     - Code postal (entier positif, max 99999)
   * - ``country_iso_code``
     - Code ISO du pays (exactement 3 caractères)

Modèle ``Letting``
^^^^^^^^^^^^^^^^^^

Représente un bien immobilier mis en location.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Champ
     - Description
   * - ``title``
     - Titre de la location (max 256 caractères)
   * - ``address``
     - Clé étrangère unique (OneToOne) vers le modèle ``Address``

Application ``profiles``
~~~~~~~~~~~~~~~~~~~~~~~~~

Modèle ``Profile``
^^^^^^^^^^^^^^^^^^

Représente les informations étendues d'un utilisateur Django.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Champ
     - Description
   * - ``user``
     - Clé étrangère unique (OneToOne) vers le modèle ``User``
   * - ``favorite_city``
     - Ville favorite de l'utilisateur (optionnel, max 64 car.)

Schéma des relations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   User (Django built-in)
     └── Profile  (OneToOne)

   Address
     └── Letting  (OneToOne)
