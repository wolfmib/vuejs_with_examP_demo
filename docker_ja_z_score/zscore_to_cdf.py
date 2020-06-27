
import scipy.stats as st

import argparse




def analyzer_input_args():
    parser = argparse.ArgumentParser(description='JA Actuary Tool Parameters')
    parser.add_argument('--input_zscore',type=float,default= 1,help="Default Z-Score is 1, return CDF !!")

    #Get Args:
    args = parser.parse_args()
    return args



if __name__ == "__main__":

    my_args = analyzer_input_args()

    print("Your input Zcore is   = ",my_args.input_zscore)
    input("Press Enter\n")

    get_cdf_value = st.norm.cdf(my_args.input_zscore)

    print("The cdf        is    = ",get_cdf_value)

