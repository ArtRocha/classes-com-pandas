import pandas as pd
import os
from pandasTest import TSV

tsv_path={
    'register':'/home/arthur/TestesPython/classes/Treated_Experiment_Register_Updated.tsv',
    'usefull_data':'/home/arthur/TestesPython/classes/2021.07.27-20.24.13_UsefullData.tsv',
    'process_date':'2021.07.27-20.24.13'
}

register = TSV(tsv_path)

test = register.meanStd_by_region(column='Generic Segmentation',region='Pericellular',YMforce='YM_Fmax0400pN',force='400pN')
test2 = register.meanStd_by_region(column='Generic Segmentation',region='Nucleus',YMforce='YM_Fmax0400pN',force='400pN')
test3 = register.meanStd_by_region(column='Generic Segmentation',region='Cytoplasm',YMforce='YM_Fmax0400pN',force='400pN')





