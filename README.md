# Instrukcja obsługi

Heja, tutaj instrukcja

Przede wszystkim musisz pobrać instant client'a Oracle, który tak naprawdę jest tym samym co SQLDeveloper, ale bez GUI.
Dzięki temu możemy połączyć pythona z naszą bazą: https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html

Utwórz na pulpicie folder ProjektSQL. 
Następnie wypakuj z pobranego Rar'a folder "Instaclient <wersja pewnie 21.3 czy coś>" z instaclientem.
Wrzuć cały powyższy folder do folderu ProjektSQL.
W folderze ProjektSQL wykonaj komende: git clone https://github.com/tomaszpiescikowski/SQLWebApp.git

Zanim zrobisz cokolwiek, przeczytaj:

No i teraz masz już nasz projekt. Poogarniaj pliki, w środku jest parę komentarzy z instrukcjami.
Pierwsze co robisz po ściągnięciu, tworzysz virtual enviroment.
Pycharm powie ci żeby dodać interpreter, więc klikasz że chcesz dodać nowy, wybierasz pythona 3.10 (zaktualizuj jak nie masz).
Następnie wchodzisz w terminalu do folderu venv/Scripts i uruchamiasz komende ./activate.ps1
Teraz masz aktywne wirtualne środowisko.
W folderze znajduje się plik requrements.txt
Wykonaj komende python -m pip install -r requirements.txt
Teraz masz zaistalowane wszystkie potrzebne aktualnie biblioteki i mamy dokładnie takie same środowiska.

Teraz możesz już produkować kodzik. Aktualizujemy wszystko przez gita.
WAŻNE:
zauważ że na naszym projekcie nie ma folderu venv - nie wrzucamy go.
więc ostrożnie z dodawaniem zmian, żeby się nic nie popsuło.
jak zrobisz zmiany w pliku, dodajesz go do stage'a -> git add <plik>
jak już masz wszystkie zmiany -> git commit -m "komentarz zmian"
na końcu -> git push

  
Serwer odpala się w pliku run.py, tam masz więcej instrukcji.


