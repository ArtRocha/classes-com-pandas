import pandas as pd
import os


class TSV:
    def __init__(self,tsv_path):
        self.register_file_df = pd.read_csv(tsv_path['register'],sep='\t',header=[0,1,2,3])
        self.usefull_data_df =pd.read_csv(tsv_path['usefull_data'],sep='\t')
        self.id = tsv_path['process_date']                
        
    
    def meanStd_by_region(self,column,region,YMforce,force):
        interesting_values = self.usefull_data_df.loc[self.usefull_data_df[column]==region]
        index = self.register_file_df.loc[(self.register_file_df['Process Date'].values==self.id)].index[0]
        mean = interesting_values[YMforce].mean()
        std = interesting_values[YMforce].std()
        self.register_file_df.at[index, [("Generic Segmentation (Young_Module)", force,region,"Mean")]] = mean
        self.register_file_df.at[index, [("Generic Segmentation (Young_Module)", force,region,"Std")]] = std
        print(mean,std)
        return self.register_file_df.to_csv('testoso2.tsv',sep='\t')
    
    def get_mean_and_std_general(self,column):
        mean = self.interesting_values[column].mean()
        std = self.interesting_values[column].std()
        return mean,std



