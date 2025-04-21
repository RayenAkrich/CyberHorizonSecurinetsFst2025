🗺️ Schéma de la Topologie

           ┌───────────────────────────┐
           │       Control Plane       │
           │  (AMF, SMF, Auth, UDM)    │
           │       10.10.0.0/24        │
           └─────────┬───┬───┬─────────┘
                     │   │   │
       ┌─────────────┘   │   └────────────┐
       │                 │                │
┌────────────┐     ┌──────────────┐  ┌──────────────┐
│ Manar 1    │     │ Centre Ville │  │ Centre Urbain│
│ Base Station│ │ Base Station │  │ Base Station        │
│ 10.10.0.11 │     │ 10.10.0.13   │  │ 10.10.0.12   │
└─────┬──────┘     └─────┬────────┘  └─────┬────────┘
      │                    │               │
      ▼                    ▼               ▼
 10.10.10.0/24        10.10.11.0/24     10.10.12.0/24
  (UE Devices)         (UE Devices)      (UE Devices)
  Smartphones,         Smartphones,      Smartphones,
  Tablets, Laptops     Tablets           TVs, Tablets

                 ↑
                 │ GTP-U Tunnels 🚇
                 │
            ┌────┴────┐
            │  UPF     │
            │10.10.0.21│
            └─────────┘

📌 Composants Clés

UE (User Equipment) : Smartphones, tablettes, laptops connectés aux gNB.

gNB (Base Stations) : Trois antennes couvrant chacun un sous-réseau UE.

Control Plane :

AMF : gestion de l’accès et mobilité

SMF : gestion de session et IP

Auth Server : vérification d’identité

UDM : stockage des profils abonnés

User Plane (UP) : UPF gère le transport des données via GTP-U.

🎯 Points de révision

Connexion UE → gNB : signalisation NAS vers l’AMF.

Authentification : AMF ↔ Auth Server ↔ UDM.

Création de session : SMF attribue IP au UE.

Tunnel GTP-U : UPF ↔ gNB pour le transport des données utilisateur.

gNB : Antenne / Station de Bases 