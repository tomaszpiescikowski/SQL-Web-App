# Ogólna instrukcja obsługi projektu

## Heja, tutaj instrukcja napisana w języku ***markdown***

Przede wszystkim musisz pobrać instant client'a Oracle, który tak naprawdę jest tym samym co SQLDeveloper, ale bez GUI.
Dzięki temu możemy połączyć pythona z naszą bazą: https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html

1. Utwórz na pulpicie folder *ProjektSQL*.

2. Następnie wypakuj z pobranego Rar'a folder *"Instaclient <wersja pewnie 21.3 czy coś>"* z instaclientem.

3. Wrzuć cały powyższy folder do folderu *ProjektSQL*.

4. W folderze *ProjektSQL* wykonaj komende: 

    `git clone https://github.com/tomaszpiescikowski/SQLWebApp.git`

### **Zanim zrobisz cokolwiek, przeczytaj:**

No i teraz masz już nasz projekt. Poogarniaj pliki, w środku jest parę komentarzy z instrukcjami.

- Pierwsze co robisz po ściągnięciu, tworzysz ***virtual enviroment***.

- Pycharm powie ci żeby dodać interpreter, więc klikasz że chcesz dodać nowy, wybierasz ***pythona 3.10 (zaktualizuj jak nie masz)***.

- Następnie wchodzisz w terminalu do folderu ***venv/Scripts*** i uruchamiasz komende ***./activate.ps1***

- Teraz masz *aktywne wirtualne środowisko*.
 
- W folderze znajduje się plik ***requirements.txt***

- Wykonaj komende `python -m pip install -r requirements.txt`

Teraz masz zaistalowane wszystkie potrzebne aktualnie biblioteki i mamy dokładnie takie same środowiska.

Teraz możesz już produkować kodzik. Aktualizujemy wszystko przez gita.

### **Ważne:**

Zauważ że na naszym projekcie nie ma folderu *venv* - **nie wrzucamy go**.

Ostrożnie z dodawaniem zmian, żeby się nic nie popsuło.
Jak zrobisz zmiany w pliku, dodajesz go do stage'a -> `git add <plik>`

Jak już masz wszystkie zmiany -> `git commit -m "<komentarz zmian>"`
na końcu -> `git push`


-------------

# Instrukcja obsługi funkcji moich funkcji SQL


![](important/Screenshot_2.png)

## **Ważne rzeczy**

Jak już odpalisz projekt, to możesz zobaczyć jak działają te moje funkcje. 

***Uruchom server w run.py***, a potem przejdź do zakładki python console na dole.

Powyżej masz screena z rzeczami, które trzeba wpisać. Ogólnie jak wprowadza się jakieś zmiany, to trzeba zresetować tą konsole pythonową i jeszcze raz importować te rzeczy. 

A po co w ogóle ta konsola? 
- Po to, żeby można było testować te funkcje na bieżąco, bo narazie nie mamy interfejsu graficznego itp. Więc warto tego używać. 

No i zmień sobie ustawienia clienta w ***\_\_init\_\_.py*** na swoje dane, żeby ***bawić się na swoim koncie***. 

Możesz mieć równocześnie otwarty SQLDeveloper i sobie sprawdzać, że rzeczywiście wszystko się zmienia i działa jak należy. Te funkcje są oczywiście to dopracowania, ale póki co fajnie działają jaka komunikacja z bazą. 

