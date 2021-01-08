# Auto Attendance loop for Leonard Devinci

Ce script permet de rester au aguet sur un appel de présence du portail Leonard de Vinci.
Tant que l'appel n'est pas lancé il tournera en boucle et s'arrêtera une fois la possibilité de se mettre présent.

Le script va checker l'appel pour chaque cours de la journée et print si t'es déjà présent ou si l'appel n'est toujours pas ouvert.

## Requirements 

python3 et pip3

## Dependances

```
pip install selenium
apt install firefox-geckodriver
```

Pour les windows dermerdez-vous :)

## Lauch the script

Ne pas oublier de mettre ses identifiants
```
emailDevinci = '##########'
mdp = '#######'
```
Puis
```
cd LDV-attendance/
python3 autoconnect.py
```

Feel free to improve the script