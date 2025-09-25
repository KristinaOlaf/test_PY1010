# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 16:29:17 2025

@author: G022322
"""

#  Antatt kjørelengde per år
km_per_år = 10000

#  Kostnader for elbil
forsikring_elbil = 5000
trafikkavgift = 8.38 * 365  #  Gjelder begge biltyper
strømpris_per_km = 0.2 * 2.00  #  0.2 kwh/km * 2 kr/kwh
bom_elbil = 0.1

totalkostnad_elbil = (forsikring_elbil + trafikkavgift + (strømpris_per_km+ bom_elbil)* km_per_år)

# Kostnader for benisinbil
forsikring_bensinbil = 7500
bensinpris_per_km = 1.0
bom_bensinbil = 0.3

totalkostnad_bensinbil = (forsikring_bensinbil + trafikkavgift + (bensinpris_per_km + bom_bensinbil)* km_per_år)

#  Kostnadsdifferanse

kostnadsdifferanse = totalkostnad_bensinbil - totalkostnad_elbil

#  Presentere resultatene
print(F"Årlige totalkostnader for elbil: {totalkostnad_elbil:.2f} kr")
print (f"årlige totalkostnader for bensinbil: {totalkostnad_bensinbil:.2f} kr")
print(f"årlig kostnadsdifferanse (bensinbil - elbil): {kostnadsdifferanse:.2f} kr")
