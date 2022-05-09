# scp root@145.14.157.41:/root/web/bierrallye_webpage/backend/db/registered.db .

import pandas as pd
import sqlite3 as lite
from pathlib import Path

file = Path(__file__).parent / 'registered.db'
conn = lite.connect(file)

query = "select * from teams"
df = pd.read_sql(query, conn)
df['Spieler 1'] = df['first_name_player_1'] + ' ' + df['last_name_player_1']
df['Spieler 2'] = df['first_name_player_2'] + ' ' + df['last_name_player_2']
df = df.rename(columns={
    'contact': 'Kontakt',
    'channel': 'Kontakt Art',
    'drink_pref_player_1': 'Getränk 1',
    'drink_pref_player_2': 'Getränk 2',
    'start_block': 'Startblock',
    'registration_date': 'Anmeldedatum'
})
df = df.drop(columns=[
    'first_name_player_1',
    'last_name_player_1',
    'first_name_player_2',
    'last_name_player_2',
])
df = df.reindex(columns=['Kontakt', 'Kontakt Art', 'Spieler 1', 'Getränk 1',
                            'Spieler 2', 'Getränk 2', 'Startblock'])

csv_path = Path(__file__).parent  / 'registrierte_nutzer.csv'
df.to_csv(csv_path, index=False)
