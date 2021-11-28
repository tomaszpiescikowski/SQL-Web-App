from market import app

"""
    Tutaj włączamy nasz serwer.
    Żeby wszystko działało musisz:
    - mieć włączony VPN politechniki
    - podać ścieżkę do swojego instant clienta Oracle, który ściągnęłaś
"""

if __name__ == "__main__":
    app.run(debug=True)