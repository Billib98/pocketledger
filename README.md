# pocketledger

Piccola libreria Python per registrare movimenti e riassumerli. È la
**sandbox** dell'AI Development Hub: serve per provare l'hub su un progetto
minuscolo, con test veloci. Non ha valore in sé.

## Uso dei test

```
python -m venv .venv
.venv\Scripts\activate        # Windows PowerShell
pip install -e . pytest
python -m pytest -q
```

Stato iniziale atteso: 12 test passano. Nel codice c'è un bug voluto che i
test attuali non rilevano (vedi `tasks/tasks.md`, task 2).
