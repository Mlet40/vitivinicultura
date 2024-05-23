from models.vinho import Vinho

def get_vinhos():
    # Lista fictícia de vinhos
    vinhos = [
        Vinho("Château Margaux", "Tinto", 2015),
        Vinho("Casillero del Diablo", "Branco", 2018),
        Vinho("Santa Rita 120", "Rosé", 2020)
    ]
    return [vinho.to_dict() for vinho in vinhos]