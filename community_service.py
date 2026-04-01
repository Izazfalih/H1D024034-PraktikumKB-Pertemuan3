import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# INPUT (Antecedent)
informasi = ctrl.Antecedent(np.arange(0, 101), 'informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101), 'persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101), 'sarpras')
# OUTPUT (Consequent)
kepuasan = ctrl.Consequent(np.arange(0, 401), 'kepuasan')

# FUZZY SET INPUT
# INFORMASI
informasi['tidak memuaskan'] = fuzz.trimf(informasi.universe, [0, 60, 75])
informasi['cukup memuaskan'] = fuzz.trimf(informasi.universe, [60, 75, 90])
informasi['memuaskan'] = fuzz.trimf(informasi.universe, [75, 90, 100])

# PERSYARATAN
persyaratan['tidak memuaskan'] = fuzz.trimf(persyaratan.universe, [0, 60, 75])
persyaratan['cukup memuaskan'] = fuzz.trimf(persyaratan.universe, [60, 75, 90])
persyaratan['memuaskan'] = fuzz.trimf(persyaratan.universe, [75, 90, 100])

# PETUGAS
petugas['tidak memuaskan'] = fuzz.trimf(petugas.universe, [0, 60, 75])
petugas['cukup memuaskan'] = fuzz.trimf(petugas.universe, [60, 75, 90])
petugas['memuaskan'] = fuzz.trimf(petugas.universe, [75, 90, 100])

# SARPRAS
sarpras['tidak memuaskan'] = fuzz.trimf(sarpras.universe, [0, 60, 75])
sarpras['cukup memuaskan'] = fuzz.trimf(sarpras.universe, [60, 75, 90])
sarpras['memuaskan'] = fuzz.trimf(sarpras.universe, [75, 90, 100])

# FUZZY SET OUTPUT
kepuasan['tidak memuaskan'] = fuzz.trimf(kepuasan.universe, [0, 50, 75])
kepuasan['kurang memuaskan'] = fuzz.trimf(kepuasan.universe, [50, 75, 100])
kepuasan['cukup memuaskan'] = fuzz.trapmf(kepuasan.universe, [100, 150, 250, 275])
kepuasan['memuaskan'] = fuzz.trapmf(kepuasan.universe, [250, 275, 325, 350])
kepuasan['sangat memuaskan'] = fuzz.trimf(kepuasan.universe, [325, 350, 400])

# RULE (contoh representatif)
rule1 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['kurang memuaskan'])
rule2 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule3 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['cukup memuaskan'])
rule4 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule5 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule6 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['cukup memuaskan'])
rule7 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule8 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule9 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule10 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule11 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule12 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['cukup memuaskan'])
rule13 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule14 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule15 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule16 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule17 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule18 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule19 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule20 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule21 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule22 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule23 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule24 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule25 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule26 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule27 = ctrl.Rule(informasi['tidak memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule28 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule29 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule30 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['cukup memuaskan'])
rule31 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule32 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule33 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule34 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule35 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule36 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule37 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule38 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule39 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule40 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule41 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule42 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule43 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule44 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule45 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule46 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule47 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule48 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule49 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule50 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule51 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule52 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule53 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['sangat memuaskan'])
rule54 = ctrl.Rule(informasi['cukup memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule55 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule56 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['cukup memuaskan'])
rule57 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule58 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule59 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule60 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule61 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule62 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule63 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule64 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['cukup memuaskan'])
rule65 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule66 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
rule67 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule68 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule69 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule70 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule71 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['sangat memuaskan'])
rule72 = ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule73 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule74 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['cukup memuaskan'], kepuasan['memuaskan'])
rule75 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule76 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['tidak memuaskan'], kepuasan['memuaskan'])
rule77 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['cukup memuaskan'], kepuasan['sangat memuaskan'])
rule78 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])
rule79 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak memuaskan'], kepuasan['sangat memuaskan'])
rule80 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup memuaskan'], kepuasan['sangat memuaskan'])
rule81 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat memuaskan'])

# SISTEM
sistem_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16,
rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, 
rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, 
rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, 
rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81])

sistem = ctrl.ControlSystemSimulation(sistem_ctrl)

# INPUT DATA SOAL
sistem.input['informasi'] = 80
sistem.input['persyaratan'] = 60
sistem.input['petugas'] = 50
sistem.input['sarpras'] = 90

# PROSES
sistem.compute()

# OUTPUT
print(f"Nilai Kepuasan: {sistem.output['kepuasan']:.2f}")

# Visualisasi
informasi.view()
persyaratan.view()
petugas.view()
sarpras.view()
kepuasan.view()

kepuasan.view(sim=sistem)

# Tampilkan semua jendela grafik (non-blocking)
plt.show(block=False)

# Tahan jendela terminal agar tidak langsung tertutup
input("\nTekan Enter pada terminal untuk keluar dan menutup semua grafik...")
plt.close('all')