# Simouse - Simulateur de Souris

Ce projet est une application Python qui empêche la mise en veille de l'ordinateur en simulant des activités utilisateur (mouvements de souris, clics, et frappes clavier). L'application dispose d'une interface graphique moderne et personnalisable.

## Fonctionnalités

- **Mouvement de souris simulé :** La souris se déplace entre des coordonnées définies.
- **Simulation de clics :** Clics automatiques à intervalles réguliers.
- **Simulation de frappes clavier :** Appui simulé sur la touche `Shift` pour garantir que l'ordinateur détecte une activité.
- **Interface graphique moderne :** Conçue avec Tkinter et des boutons stylisés.
- **Personnalisation :** Possibilité de définir les coordonnées de départ, les coordonnées de fin, et la vitesse des mouvements.
- **Arrêt via Échap :** La simulation peut être arrêtée par le bouton Stop ou en appuyant sur la touche `Échap`.

## Installation

### Prérequis
- Python 3.7 ou plus.
- Les bibliothèques suivantes doivent être installées :
  ```bash
  pip install pyautogui
  ```

### Lancer le script Python
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/alexballow/simouse.git
   ```
2. Accédez au dossier du projet :
   ```bash
   cd simouse
   ```
3. Lancez le script :
   ```bash
   python simouse
   ```

### Compiler en exécutable

Vous pouvez utiliser **PyInstaller** pour créer un fichier exécutable pour partager l'application sans besoin d'installer Python.

1. Installez PyInstaller :
   ```bash
   pip install pyinstaller
   ```
2. Compilez le script en exécutable :
   ```bash
   pyinstaller --onefile --windowed --icon=simouse.ico --add-data "simouse.ico;." simouse.py
   ```
3. L'exécutable se trouvera dans le dossier `dist/`.

## Utilisation

1. **Définir les paramètres :**
   - Coordonnées de départ (X, Y).
   - Coordonnées de fin (X, Y).
   - Vitesse des mouvements (en secondes).

2. **Démarrer la simulation :** Cliquez sur le bouton `Start`.

3. **Arrêter la simulation :**
   - Cliquez sur le bouton `Stop`.
   - Ou appuyez sur la touche `Échap`.

## Dépendances

- **Tkinter :** Interface graphique native de Python.
- **PyAutoGUI :** Permet de simuler les mouvements de souris, clics, et frappes clavier.

## Structure du projet

```plaintext
simulateur-de-souris/
├── simouse.py              # Script principal
├── simouse.ico             # Icône personnalisée
└── README.md               # Documentation
```

## Contribution

Les contributions sont les bienvenues !

1. Forkez le projet.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b ma-branche
   ```
3. Faites vos modifications et commitez-les :
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. Poussez votre branche :
   ```bash
   git push origin ma-branche
   ```
5. Créez une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

## Crédits de l'icône

L'icône utilisée dans ce projet est issue de [Icon-Icons](https://icon-icons.com/fr/icone/le-rat-la-souris-animal/85282) et créée par l'auteur **Vincent Le Moign**. Elle est distribuée sous la licence "Free for commercial use". Veuillez consulter leurs conditions d'utilisation pour plus d'informations.




