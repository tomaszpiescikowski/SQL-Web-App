from market import app

"""
    Tutaj włączamy nasz serwer.
    Żeby wszystko działało:
    - trzeba mieć włączony VPN politechniki
    - należy podać ścieżkę do swojego instant clienta Oracle
"""

if __name__ == "__main__":
    app.run(debug=True)


