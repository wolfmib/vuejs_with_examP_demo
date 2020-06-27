
import scipy.stats as st

import argparse




def analyzer_input_args():
    parser = argparse.ArgumentParser(description='JA Actuary Tool Parameters')
    parser.add_argument('--input_cdf',type=float,default= 1,help="Default cdf is 0.95, return z-score !!")

    #Get Args:
    args = parser.parse_args()
    return args



if __name__ == "__main__":

    my_args = analyzer_input_args()

    print("Your input cdf is   = ",my_args.input_cdf)
    input("Press Enter\n")

    get_zscore_value = st.norm.ppf(my_args.input_cdf)

    print("The z-score   is    = ",get_zscore_value)



