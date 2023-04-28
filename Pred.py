import streamlit as st
from keras.models import load_model
import pandas as pd
import numpy as np

def load():
        model = load_model(fr"model/best_moedl_fold1_86%.h5")
        return model


def predcit_page():
        st.title("Multiple Sclerosis Prediction")

        st.write(""" #### Patient Parameters """)

        col1, col2, col3 = st.columns([2,2, 1])
        with col1:
                PATHO_ASSOC_SEP_RéMITTENTE = float(st.checkbox("Pathologie Associées: SEP Rémittente"))
                pathologie_associées_SEP_RR = float(st.checkbox("Pathologie Associées: SEP Récurrente"))
                S_fourmillements = float(st.checkbox("Symptômes: Fourmillements"))
                S_trouble_de_léquilibre = float(st.checkbox("Symptômes: Trouble de l'équilibre"))
                S_baisse_de_lacuité_visuelle_de_loeil_droit = float(st.checkbox("Symptômes: Baisse de l'Acuité Visuelle de l'Oeil Droit"))
                S_baisse_de_lacuité_visuelle_de_loeil_gauche = float(st.checkbox("Symptômes: Baisse de l'Acuité Visuelle de l'Oeil Gauche"))
                S_faiblesse_musculaire_de_lhémicorps_droit = float(st.checkbox("Symptômes: Faiblesse Musculaire de l'Hémicorps Droit"))
                S_faiblesse_musculaire_de_lémicorps_gauche = float(st.checkbox("Symptômes: Faiblesse Musculaire de l'Emicorps Gauche"))
                S_perte_de_la_sensibilité_fine = float(st.checkbox("Symptômes: Perte de la Sensibilité Fine"))
                S_trouble_de_language = float(st.checkbox("Symptômes: trouble de language"))
                S_vision_double = float(st.checkbox("Symptômes: Vision Double"))
                S_paresthésis = float(st.checkbox("Symptômes: Paresthésis"))
                CR_IRM_lésion_démyélinisantes_sus_tentoriel = float(st.checkbox("Compte Rendu IRM: Lésion Démyélinisantes sus Tentoriel"))
                CR_IRM_lésions_démyélinisantes_du_cordon_médullaire = float(st.checkbox("Compte Rendu IRM: Lésions Démyélinisantes du Cordon Médullaire"))
        with col2:
                EX_NEURO_synrome_pyramidale_4_membre_àl_hémicap_droit = float(st.checkbox("Examen Neurologique: Syndrome Pyramidale 4 membre à l'Hémicap Droit"))
                EX_NEURO_syndrome_cérébelleux_stato_cinétique = float(st.checkbox("Examen Neurologique: Syndrome Cérébelleux Stato Cinétique"))
                EX_NEURO_bien_orienter_dans_le_temps_dans_l_espace_conscience_et_coopérative = float(st.checkbox("Examen Neurologique: Bien Orienter dans le temps dans l'Espace Conscience et Coopérative"))
                EX_NEURO_atteinte_des_fonctions_cognitives = float(st.checkbox("Examen Neurologique: Atteinte des Fonctions Cognitives"))
                EX_NEURO_syndrome_cordonal_postérieur = float(st.checkbox("Examen Neurologique: Syndrome Cordonal Postérieur"))
                EX_NEURO_SD_vestibulaire = float(st.checkbox("Examen Neurologique: Syndrome Vestibulaire"))
                EX_NEURO_hypoesthésie_de_l_hémicorps_gauche = float(st.checkbox("Examen Neurologique: Hypoesthésie de l'Hémicorps Gauche") )
                EX_NEURO_syndrome_médullaire_des_2_membres_inferieurs = float(st.checkbox("Examen Neurologique: Syndrome Médullaire des 2 Membres Inferieurs"))
                EX_NEURO_paire_cranienen =  float(st.checkbox("Examen Neurologique: Paire Cranienen"))
                ASPECT_LCR_clair = float(st.checkbox("ASPECT LCR: Clair"))
        with col3:

                Index__IgG =  st.number_input("Index IgG", min_value=0.0, max_value=5.0, step=0.01)
                Glycorachie = st.number_input("Glycorachie", min_value=0.0, max_value=6.0, step=0.01)
                Protéinorachie =  st.number_input("Protéinorachie", min_value=0.0, max_value=4.0, step=0.01)
                EDSS1 =  st.number_input("EDSS1", min_value=0.0, max_value=9.0, step=0.5)
                EDSS2 = st.number_input("EDSS2", min_value=0.0, max_value=9.0, step=0.5)

        ok = st.button("Predict Relapse Time", type="primary")
        Clusters = {0:"2 Weeks", 1:"1 Month", 2:"3 Months" , 3:"6 Months" ,4:"1 Year" ,5:"Over a year"}
        model = load()
        if ok:
                predict = model.predict([[PATHO_ASSOC_SEP_RéMITTENTE,pathologie_associées_SEP_RR,S_fourmillements,S_trouble_de_léquilibre,S_baisse_de_lacuité_visuelle_de_loeil_droit,S_baisse_de_lacuité_visuelle_de_loeil_gauche,S_faiblesse_musculaire_de_lhémicorps_droit,S_faiblesse_musculaire_de_lémicorps_gauche,S_perte_de_la_sensibilité_fine,S_trouble_de_language,S_vision_double,S_paresthésis,CR_IRM_lésion_démyélinisantes_sus_tentoriel,CR_IRM_lésions_démyélinisantes_du_cordon_médullaire,EX_NEURO_synrome_pyramidale_4_mmbr_àl_hémicap_droit,EX_NEURO_syndrome_cérébelleux_stato_cinétique,EX_NEURO_bien_orienter_dans_le_temps_dans_l_espace_conscience_et_coopérative,EX_NEURO_atteinte_des_fonctions_cognitives,EX_NEURO_syndrome_cordonal_postérieur,EX_NEURO_SD_vestibulaire,EX_NEURO_hypoesthésie_de_l_hémicorps_gauche,EX_NEURO_syndrome_médullaire_des_2_membres_inferieurs,EX_NEURO_paire_cranienen,ASPECT_LCR_clair,Index__IgG,Glycorachie,Protéinorachie,EDSS1,EDSS2]])
                pred = np.argpartition(predict[0], -2)[-2:]
                if (pred[0] > pred [1]) | (predict[0][pred[1]] > predict[0][pred[0]]) :
                        A = f'{Clusters[pred[1]]} ({round(predict[0][pred[1]]*100, 2)} %)'
                        B = f'{Clusters[pred[0]]} ({round(predict[0][pred[0]]*100, 2)} %)'
                        st.write(f"The Relapse Time Estimation is:\n\n {A} \n\n {B}")
                else :
                        C = f'{Clusters[pred[1]]} ({round(predict[0][pred[1]]*100, 2)} %)'
                        st.write(f"The Relapse Time Estimation is:\n\n {C}")
        

