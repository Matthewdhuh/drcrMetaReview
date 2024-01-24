import pandas as pd
import os

def trial_dict_constructor():
    path = "./Trials"
    csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]
    trials = pd.DataFrame()
    for csv in csv_files: 
        file_path = os.path.join(path, csv)
        df = pd.read_csv(file_path)
        trials = pd.concat([trials, df], ignore_index = True)
    trials = trials.drop_duplicates(subset=['NCT Number'])
    trials = trials.reset_index(drop = True)

    def helper(keyword_array):
        total_row_count = 0
        for keyword in keyword_array:
            keyword_filter_title = trials['Study Title'].str.contains(keyword, case=False, na=False)
            keyword_filter_conditions = trials['Conditions'].str.contains(keyword, case=False, na=False)
            if keyword_filter_title.sum() > keyword_filter_conditions.sum():
                total_row_count += keyword_filter_title.sum()
            else: total_row_count += keyword_filter_conditions.sum()
        # print(f"{keyword_array}:{total_row_count}")
        return total_row_count
    DryAMD = helper(['Dry AMD', 'Dry Age', 'Nonexudative AMD', 'Nonexudative Age',
                     'Nonneovascular AMD', 'Nonneovascular age','Non-neovascular AMD', 
                     'non-neovascular age', 'dAMD', 'early amd', 'early age'])
    WetAMD = helper(['Wet AMD', 'Wet age', 'Exudative AMD', 'Exudative age',
                      'Neovascular AMD', 'Neovascular age', 'wAMD', 'Advanced AMD', 'Advanced age', 
                      'nAMD', 'late AMD', 'late age'])
    DME = helper(['Diabetic Macular Edema', 'DME'])
    DR = helper(['Diabetic Retinopathy'])
    VMT = helper(['Vitreomacular Traction', 'VMT'])
    MH = helper(['Macular Hole'])
    RR = helper(['Radiation Retinopathy'])
    ERM = helper(['Epiretinal Membrane'])
    pubmed_dictionary = {'DR': DR, 'DME': DME, 'ERM': ERM, 'VMT': VMT, 
                        'RR': RR, 'MH': MH, 'Wet AMD': WetAMD, 'Dry AMD': DryAMD}
    return pubmed_dictionary

if __name__ == '__main__':
  pubmed_dictionary = trial_dict_constructor()
  print(pubmed_dictionary)
