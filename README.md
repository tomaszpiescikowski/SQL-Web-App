# Ogólna instrukcja obsługi projektu

Przede wszystkim musisz pobrać instant client'a Oracle, który tak naprawdę jest tym samym co SQLDeveloper, ale bez GUI.
Dzięki temu możemy połączyć pythona z naszą bazą: https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html

1. Utwórz na pulpicie folder *ProjektSQL*.

2. Następnie wypakuj z pobranego Rar'a folder *"Instaclient <wersja pewnie 21.3 czy coś>"* z instaclientem.

3. Wrzuć cały powyższy folder do folderu *ProjektSQL*.

4. W folderze *ProjektSQL* wykonaj komende: 

    `git clone https://github.com/tomaszpiescikowski/SQLWebApp.git`

### Następne kroki
- Stwórz wirtualne środowisko w python'ie

- W folderze znajduje się plik ***requirements.txt***

- Wykonaj komende `python -m pip install -r requirements.txt`

Teraz masz zaistalowane wszystkie potrzebne aktualnie biblioteki i mamy dokładnie takie same środowiska.


# Instrukcja obsługi funkcji moich funkcji SQL


![](important/Screenshot_2.png)

## **Ważne rzeczy**

Jak już odpalisz projekt, to możesz zobaczyć jak działają funkcje. 

***Uruchom server w run.py***, a potem przejdź do zakładki python console na dole.

Powyżej masz screena z rzeczami, które trzeba wpisać. Ogólnie jak wprowadza się jakieś zmiany, to trzeba zresetować tą konsole pythonową i jeszcze raz importować te rzeczy. 

A po co w ogóle ta konsola? 
- Po to, żeby można było testować te funkcje na bieżąco, bo narazie nie mamy interfejsu graficznego itp. Więc warto tego używać. 

No i zmień sobie ustawienia clienta w ***\_\_init\_\_.py*** na swoje dane, żeby ***działać się na swoim koncie***. 

Możesz mieć równocześnie otwarty SQLDeveloper i sobie sprawdzać, że rzeczywiście wszystko się zmienia i działa jak należy. Te funkcje są oczywiście to dopracowania, ale póki co fajnie działają jaka komunikacja z bazą. 

