import os
import xlrd
import random
import collections
import sys
import copy
import json
from datetime import date
import datetime
import argparse
import numpy as np
import time
from itertools import takewhile
import matplotlib.pyplot as plt
import re

## Easy Math
def Moyenne(input_list,round_number):
    return round((sum(input_list)/len(input_list)),round_number)


def python_sys_check_version():
    # major = 3 python3,   
    # major = 2 python2,
    major ,minor, micro, _, _ = sys.version_info
    msg = "[python_sys_check_version]: Current you are using python (%d, %d, %d)\n"%(major,minor,micro)
    return major, msg

## System Running Control related:

class read_excel_agent():
    def __init__(self):
        self.name = "read_excel_agent"
    
    def __column_len__(self,sheet,index):
        col_values = sheet.col_values(index)
        col_len = len(col_values)
        for _ in takewhile(lambda x: not x, reversed(col_values)):
            col_len -= 1
        return col_len

    def __row_len__(self,sheet,row_index):
        row_values = sheet.row_values(row_index)
        row_len   = len(row_values)
        for _ in takewhile(lambda x: not x, reversed(row_values)):
            row_len -=1
        return row_len

    
    # ---------------------- Keywords from Left to Rgith ------------------------------------------
    # Je mettre les mots dans la cell_value(0, 0-20), a row = 0 (left_to_right)
    def show_les_key_mots_de_gauche_a_droite(self,input_sheet):
        # Cherche les mots dans la row=0
        row_len = self.__row_len__(input_sheet,0)
        msg = "[ana_system: show_les_key_mots_de_gauche_à_droite]: Key words list:\n"

        # Cherche avec Regular expression:
        # Format -> any_key_words:
        for index in range(row_len):
            any_value = input_sheet.cell_value(0,index)

            # Regular Expression
            re_pattern    = r'.*:'
            changed_value = re.findall(re_pattern,any_value)
            if changed_value:
                msg += "%s\n"%changed_value[0]
            else:
                pass
        msg += "\n\n"
        return msg 

    #### About obtenir_value_par_norm_dans_tout_le_col():
        # ----------  input_sheet ----------------------------------
        # col_0    |  col_2   |   col_3           
        # -----------------------------------------
        # keymot1  |  keymot2 |  input_norm=keymot3
        # ------      ------      -------
        #  value1  |  value2  |  value3
        # ------------------------------------
        # 
        # [System]: Obtenir return_value = value3
    def obtenir_value_par_norm_dans_tout_le_col(self,input_sheet,input_norm,optional_format=False):
        # Cherche les mots dans la col=0
        row_len = self.__row_len__(input_sheet, 0)
        msg = "ana_system: show_les_key_mots:\n"
   
        # Cherche avec Regular expression: 
        # Format->   any_key_words:
        for index in range(row_len):
            any_value = input_sheet.cell_value(0,index)
            
            # Regular Expression
            re_pattern = r'.*:'
            changed_value = re.findall(re_pattern,any_value)
      
            # March ou non:
            if changed_value:
                if changed_value[0] == input_norm:
                    msg          += "Match: %s\n"%changed_value[0]
                    return_value  = input_sheet.cell_value(1,index)

                    # Format changer par optional_format
                    if optional_format == "int":
                        msg            += "Changed to int:\n"
                        return_value    = int(float(return_value))
                        return return_value, msg
                    elif optional_format == "float":
                        msg            += "Changed to float:\n"
                        return_value    = float(return_value)
                        return return_value, msg
                    elif optional_format == False:
                        msg            += "Default value is string:\n"
                        return return_value, msg
                    else:
                        print("[obtenir_value_par_norm][Error]: Only support 'int','float' et default 'str', meet wrong input option %s"%optional_format)
            else:
                pass
                
        
        print("[obtenir_value_par_norm][Error]: Can't find the norm {%s} in {%s} sheet"%(input_norm,input_sheet))
        return 543, msg

    #### About obtenir_value_par_norm_dans_tout_le_col():
        # ----------  input_sheet ----------------------------------
        # col_0    |  col_2   |   col_3
        # -----------------------------------------
        # keymot1  |  keymot2 |  input_norm=keymot3
        # ------      ------      -------
        #  value1  |  value2  |  value3
        #  value1- |  value2- |  value3-
        #  vlaue11 |  value22 |  vlaue33
        #          |          |  value333
        # ------------------------------------
        #
        # Auto search value_size = 4 
        # [System]: Obtenir return_value_list = [ value3, value3-, value33, value333 ] 
    def obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(self, input_sheet, input_norm,optional_format=False):
        
        # Return value list
        return_value_list = []

        # Current python running vresion,  2 et 3 , il a la convert to int, float method different..
        current_python_version , _version_msg = python_sys_check_version()

        # Cherche les mots dans la col=0
        row_len = self.__row_len__(input_sheet, 0)
        msg = "ana_system: show_les_key_mots:\n"
        msg += _version_msg
   
        # Cherche avec Regular expression: 
        # Format->   any_key_words:
        for key_mot_index in range(row_len):
            any_value = input_sheet.cell_value(0,key_mot_index)
            
            # Regular Expression
            re_pattern = r'.*:'
            changed_value = re.findall(re_pattern,any_value)
      
            # March ou non:
            if changed_value:
                if changed_value[0] == input_norm:
                    msg          += "Match: %s\n"%changed_value[0]

                    # Auto Chercher Size et Obtenir list ici:
                    total_len_for_this_col = self.__column_len__(input_sheet, key_mot_index)
                    msg += "Size = (%d, %d)\n"%(1,total_len_for_this_col-1)
                  
                    for value_index in range(1,total_len_for_this_col):
                        tem_value  = input_sheet.cell_value(value_index,key_mot_index)
                        return_value_list.append(tem_value)

                    # Format changer par optional_format
                    if optional_format == "int":
                        msg            += "Changed to int list :\n"
                        if current_python_version == 3:   # Python3
                            return_value_list = list(map(float,return_value_list))
                            return_value_list = list(map(int,return_value_list))
                        elif current_python_version == 2: # Python2
                            return_value_list = map(float,return_value_list)
                            return_value_list = map(int,return_value_list)
                        return return_value_list, msg
                    elif optional_format == "float":
                        msg            += "Changed to float list:\n"
                        if current_python_version == 3:   # Python3
                            return_value_list = list(map(float,return_value_list))
                        elif current_python_version == 2: # Python2
                            return_value_list = map(float,return_value_list)
                        return return_value_list, msg
                    elif optional_format == False:
                        msg            += "Default value is string list:\n"
                        return return_value_list, msg
                    else:
                        print("[obtenir_value_par_norm][Error]: Only support 'int','float' et default 'str', meet wrong input option %s"%optional_format)
            else:
                pass
                
        
        print("[obtenir_value_par_norm][Error]: Can't find the norm {%s} in {%s} sheet"%(input_norm,input_sheet))
        return 543, msg
    
    #### About obtenir_value_par_norm_by_input_table_ragne_dans_la_col_direction
    def obtenir_value_par_norm_by_input_table_ragne_dans_la_col_direction(self,input_sheet,input_norm,numbers_of_rows,numbers_of_cols,optional_format=False):
        # On enregistre chaque ligne(row) pour lister
        value_list_in_each_row_list = []

        def __obtenir_tem_value_list_in_each_row(input_sheet,start_row,start_col,end_col,optional_format=False):
            tem_value_list_in_each_row = []
            for any_col_index in range(start_col,end_col):
                tem_value = input_sheet.cell_value(start_row,any_col_index)
                if optional_format == 'int':
                    tem_value = int(float(tem_value))
                elif optional_format == "float":
                    tem_value = float(tem_value)
                elif optional_format == False:
                    pass
                else:
                    print("[__obtenir_tem_value_list_in_each_row]: Only support 'int','float', et default 'str', meet wrong format %s"%optional_format)
                tem_value_list_in_each_row.append(tem_value)
            return tem_value_list_in_each_row

        # Chercher les mots dans la row=0
        row_len = self.__row_len__(input_sheet,0)
        msg = "ana_system: show_les_key_mots:\n"

        # Loop match key_mots:
        for any_col_index in range(row_len):
            any_value = input_sheet.cell_value(0,any_col_index)

            # Regular Expression
            re_pattern = r'.*:'
            changed_value = re.findall(re_pattern, any_value)

            # Match ou non:
            if changed_value:
                if changed_value[0] == input_norm:
                    msg          += "Match: %s\n"%changed_value[0]
                    # Obtenir values par row et row:
                    for any_row_length in range(numbers_of_rows):
                        start_row = 1 + any_row_length
                        start_col = any_col_index + 1
                        end_col   = start_col     + numbers_of_cols

                        tem_value_list_in_each_row = __obtenir_tem_value_list_in_each_row(input_sheet,start_row,start_col,end_col,optional_format=optional_format)
                        value_list_in_each_row_list.append(tem_value_list_in_each_row)
                        msg += "Add the one row_list: %s\n"%tem_value_list_in_each_row
                    
                    msg += "Final value_list_in_each_row_list: %s\n"%value_list_in_each_row_list
                    return value_list_in_each_row_list, msg 
            else:
                pass
        
        print("[obtenir_value_par_norm_by_input_table_range_dans_la_row_direction][Error]: Can't find the norm {%s} in {%s} sheet"%(input_norm,input_sheet))
        return 543, msg
    
    #-----------------------------------------------------------------------------------------------
    



    # ----------------------  Keywords from Top to Botton ------------------------------------------
    # Je mettre les mots dans la  cell_value(0-13, 0), a col=0
    def show_les_key_mots(self,input_sheet):

        # Cherche les mots dans la col=0
        col_len = self.__column_len__(input_sheet,0)
        msg = "[ana_system: show_les_key_mots]: Key words list:\n"

        # Cherche avec Regular expression: 
        # Format->   any_key_words:
        for index in range(col_len):
            any_value = input_sheet.cell_value(index,0)
         
            # Regular Expression
            re_pattern = r'.*:'
            changed_value = re.findall(re_pattern,any_value)
            if changed_value:
                msg += "%s\n"%changed_value[0]
            else:
                pass
        msg +="\n\n"
        return msg

    #### About obtenir_value_par_norm: 
        # Related Functions: 
        #   - show_les_key_mots 
        #   - obtenir_value_par_norm
        #   - obtenir_value_par_norm_by_input_table_range_dans_la_row_direction
        # 
        # Comment en faire "obtenir_value_par_norm":
        #    -----------input_sheet-------------
        #    col_0       |  col_1
        #    -----------------------
        #    key_mot_1:  | value 1
        #    ...
        #    key_mot_n:  | vvalue n
        #    -------------------------------
        #     
        #    input_norm = key_mot,  
    def obtenir_value_par_norm(self,input_sheet,input_norm,optional_format=False):
        # Cherche les mots dans la col=0
        col_len = self.__column_len__(input_sheet, 0)
        msg = "ana_system: show_les_key_mots:\n"

        # Cherche avec Regular expression: 
        # Format->   any_key_words:
        for index in range(col_len):
            any_value = input_sheet.cell_value(index,0)
         
            # Regular Expression
            re_pattern = r'.*:'
            changed_value = re.findall(re_pattern,any_value)

            # March ou non:
            if changed_value:
                if changed_value[0] == input_norm:
                    msg          += "Match: %s\n"%changed_value[0]
                    return_value  = input_sheet.cell_value(index,1)

                    # Format changer par optional_format
                    if optional_format == "int":
                        msg            += "Changed to int:\n"
                        return_value    = int(float(return_value))
                        return return_value, msg
                    elif optional_format == "float":
                        msg            += "Changed to float:\n"
                        return_value    = float(return_value)
                        return return_value, msg
                    elif optional_format == False:
                        msg            += "Default value is string:\n"
                        return return_value, msg
                    else:
                        print("[obtenir_value_par_norm][Error]: Only support 'int','float' et default 'str', meet wrong input option %s"%optional_format)
            else:
                pass
                     
        print("[obtenir_value_par_norm][Error]: Can't find the norm {%s} in {%s} sheet"%(input_norm,input_sheet))
        return 543, msg

    #### Abount obtenir_value_par_norm_by_input_table_range_dans_la_row_direction()
        # Par example
        # key_mot | col1 | col2 | col3
        #    --------------------------------
        #    row1 | v11  |  v12 | v12
        #    row2 | v21  |  v22 | v23
        #    --------------------------------
        #  numbers_of_rows = 2,  numbers_of_cols = 3 ,input_norm = key_mot
    def obtenir_value_par_norm_by_input_table_range_dans_la_row_direction(self,input_sheet,input_norm,numbers_of_rows,numbers_of_cols,optional_format=False):
        
        # On enregistre chaque ligne(row) pour lister
        value_list_in_each_row_list = []
        
        def __obtenir_tem_value_list_in_each_row(input_sheet,start_row,start_col,end_col,optional_format=False):
            tem_value_list_in_each_row = []
            for any_col_index in range(start_col,end_col):
                tem_value = input_sheet.cell_value(start_row,any_col_index)
                if optional_format == 'int':
                    tem_value = int(float(tem_value))
                elif optional_format == "float":
                    tem_value = float(tem_value)
                elif optional_format == False:
                    pass
                else:
                    print("[__obtenir_tem_value_list_in_each_row]: Only support 'int','float', et default 'str', meet wrong format %s"%optional_format)
                tem_value_list_in_each_row.append(tem_value)
            return tem_value_list_in_each_row
        
        # Cherche les mots dans la col=0
        col_len = self.__column_len__(input_sheet, 0)
        msg = "ana_system: show_les_key_mots:\n"

        
        for any_row_index in range(col_len):
            any_value = input_sheet.cell_value(any_row_index,0)
         
            # Regular Expression
            re_pattern = r'.*:'
            changed_value = re.findall(re_pattern,any_value)

            # March ou non:
            if changed_value:
                if changed_value[0] == input_norm:
                    msg          += "Match: %s\n"%changed_value[0]

                    # Obtenir values par row et row:
                    for any_row_length in range(numbers_of_rows):
                        start_row = any_row_index + any_row_length + 1 
                        start_col = 1 
                        end_col   = 1 + numbers_of_cols

                        tem_value_list_in_each_row = __obtenir_tem_value_list_in_each_row(input_sheet,start_row,start_col,end_col,optional_format=optional_format)
                        value_list_in_each_row_list.append(tem_value_list_in_each_row)
                        msg += "Add the one row_list: %s\n"%tem_value_list_in_each_row
                             
                    msg += "Final value_list_in_each_row_list: %s\n"%value_list_in_each_row_list
                    return value_list_in_each_row_list , msg
            else:
                pass
                     
        print("[obtenir_value_par_norm_by_input_table_range_dans_la_row_direction][Error]: Can't find the norm {%s} in {%s} sheet"%(input_norm,input_sheet))
        return 543, msg
    # -----------------------------------------------------------------------------------------------
    

class start_end_class:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.size = 0
    def set_start(self, input_start):
        self.start = input_start
        self.__calculate_size__()
    def set_end(self, input_end):
        self.end = input_end
        self.__calculate_size__()
    def __calculate_size__(self):
        self.size = int(self.end-self.start + 1)

    def les_information(self):
        msg = "start_end_class:\n"
        msg += "self.start = %d\n"%self.start
        msg += "self.end   = %d\n"%self.end
        msg += "self.size  = %d\n"%self.size
        return msg


# Comment en faire:  Dans la main:   get_main_args = analyzer_input_args()
#                                    input_excel_name = get_main_args.input_ecelname etc..
def analyzer_input_args():
    parser = argparse.ArgumentParser(description='Game Simulation Parameters')
    parser.add_argument('--input_excelname', type=str,default="default", help="Default name: 'setting.xlsx'")
    parser.add_argument('--setting_runs', type=int,default=50000, help="[Jason]: Default 50000 runs")
    parser.add_argument('--setting_fg_times', type=int,default=5, help="[Jason]: Default 5 runs")

    parser.add_argument('--output_folder', type=str,default='output', help="Default: current path")
    parser.add_argument('--show_info', type=bool, default=False,help="Default: False, setting 'True' to printout info")
    parser.add_argument('--debug_mode', type=bool, default=False,help="Default: False, setting 'True' to printout debug detail information via print method in code")
    parser.add_argument('--show_estimate_time', type=bool,default=False, help="Estimate the processing cnts")
    parser.add_argument('--draw_line', type=int,default=False, help="SLOT Sumulator Used Only")
    parser.add_argument('--draw_fig', type=bool,default=False, help="Draw support fig.png during running")
    parser.add_argument('--unit_test', type=bool,default=False, help="Initial the unit_test for specific funciton in each project")
    parser.add_argument('--unit_test__case_number', type=int, default=0, help="Unit_test_case_number: You must set --unit_test True first.")


    #Get Args:
    args = parser.parse_args()
    return args

def analyzer_get_tem_file_name_format_by_time():
    tem_file_name_format = str(date.today()) + '-' + str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + "---" + str(datetime.datetime.now().microsecond)
    return tem_file_name_format

class analyzer_output_agent():
    def __init__(self):
        self.default_output_file_name = ""
        self.output_folder = "./"
        self.show_info = False
        self.debug_mode = False
        self.output_flag_by_excel = False
        self.output_folder_flag_by_args = False
    # [Johnny]: C'est mieux pour utiliser set_oo_function pour setting internal variable.
    def set_show_info(self,input_show_info):
        self.show_info = input_show_info
        return self.show_info
    def set_debug_mode(self,input_debug_mode):
        self.debug_mode = input_debug_mode
        return self.debug_mode
    def set_output_folder(self,input_output_folder):
        self.output_folder = "./" + str(input_output_folder) + "/"
        self.output_folder_flag_by_args = True
        return self.output_folder
    def set_default_output_file_name(self,input_file_name):
        self.default_output_file_name = input_file_name
    def set_output_flag_by_excel(self,input_flag):
        self.output_flag_by_excel = input_flag
    def obtenir_info(self):
        msg  = ""
        msg += "self.show_info                    =  %s\n"%self.show_info
        msg += "self.debug_mode                   =  %s\n"%self.debug_mode
        msg += "self.output_folder                =  %s\n"%self.output_folder
        msg += "self.default_output_file_name     =  %s\n"%self.default_output_file_name

        msg += "self.output_flag_by_excel         =  %s\n" % self.output_flag_by_excel
        msg += "self.output_folder_flag_by_args   =  %s\n" % self.output_folder_flag_by_args
        return msg


    # method:
    #          self.output_agent(msg)
    #          self.output_agent(msg,debug_mode_tag =1)
    #          self.output_agent(msg,other_file_name = "other_file_name")

    def output_agent(self,msg,debug_mode_tag = 0 , other_file_name = "Default"):

        
        # Afficher debug ou non
        if debug_mode_tag == 0:
            if self.show_info == True:
                print(msg)
            # Save msg to output file ou non
            if self.output_flag_by_excel == True:
                if other_file_name == "Default":
                    self.log(msg, self.default_output_file_name)
                else:
                    self.log(msg, other_file_name)
            else:
                pass
        elif debug_mode_tag == 1:
            if self.debug_mode == True: print(msg)
                  
        

    def log(self,msg,file_name):

        # Case1: Default output_folder: current pwd
        # Case2: Nouvelle output_folder
        file = open(self.output_folder+file_name+'.txt', 'a', encoding='UTF-8')
        # Écrire 
        file.writelines(msg+"\n")
        # Fermer
        file.close()

class analyzer_estimate_run_time_monitor():

    def __init__(self):
        self.start_time = time.time()

    def get_passed_time(self):
        passed_time = (time.time() - self.start_time)
        return passed_time

class analyzer_slot_summary_agent_v1():

    def __init__(self):
        self.main_rtp_list          = []
        self.main_hit_rate_list     = []
        self.summary_msg            = ""
        self.main_rtp_average       = 0.0
        self.main_hit_rate_average  = 0.0


    def show_parameters(self):
        msg  = ""
        msg += "self.main_rtp_list      = %s\n"%self.main_rtp_list
        msg += "self.main_hit_rate_list = %s\n"%self.main_hit_rate_list
        return msg

    def append(self,tem_rtp,tem_hit_rate):
        self.main_rtp_list.append(tem_rtp)
        self.main_hit_rate_list.append(tem_hit_rate)
    
    def faire_summary(self):

        def analyzer_get_average(input_list):
            total_value = 0
            for any_value in input_list:
                total_value += any_value

            return float(total_value / len(input_list))
        
        self.main_rtp_average      = analyzer_get_average(self.main_rtp_list)
        self.main_hit_rate_average = analyzer_get_average(self.main_hit_rate_list)


        self.summary_msg = "\nFinal_Summary:\n"
        self.summary_msg += "平均RTP    =        %2.4f      \n" %self.main_rtp_average
        self.summary_msg += "平均中獎率 =        %2.4f      \n" %self.main_hit_rate_average
        self.summary_msg += "\n\n------------------------------------參考資料-------------------------------------\n\n"
        for i in range(len(self.main_rtp_list)):
            self.summary_msg += "The  [%2d]th running:   rtp=     %2.4f     ,  中獎率=     %2.4f\n" % (i, self.main_rtp_list[i], self.main_hit_rate_list[i])
        
        return self.summary_msg

    def write_summary(self,  input_file_name,output_folder = None):
        file_name = input_file_name + str(date.today()) + '-' + str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute)
        if output_folder == None:
            file = open(file_name+".txt", "a", encoding="UTF-8")
            file.writelines(self.summary_msg+"\n")

        else:
            folder = output_folder
            file = open("./"+folder+"/"+file_name+'.txt', 'a', encoding='UTF-8')
            file.writelines(self.summary_msg+"\n")
        file.close()

class analyzer_slot_summary_agent_v2():

    def __init__(self):
        self.main_rtp_list = []
        self.main_hit_rate_list = []
        self.main_name_list  =[]
        self.summary_msg = ""
        self.main_rtp_average = 0.0
        self.main_hit_rate_average = 0.0

    def show_parameters(self):
        msg = ""
        msg += "self.main_rtp_list      = %s\n" % self.main_rtp_list
        msg += "self.main_hit_rate_list = %s\n" % self.main_hit_rate_list
        return msg

    def append_v2(self, input_name ,tem_rtp, tem_hit_rate):
        self.main_rtp_list.append(tem_rtp)
        self.main_hit_rate_list.append(tem_hit_rate)
        self.main_name_list.append(input_name)

    def faire_summary(self):

        def analyzer_get_average(input_list):
            total_value = 0
            for any_value in input_list:
                total_value += any_value

            return float(total_value / len(input_list))

        self.main_rtp_average = analyzer_get_average(self.main_rtp_list)
        self.main_hit_rate_average = analyzer_get_average(
            self.main_hit_rate_list)

        self.summary_msg = "\nFinal_Summary:\n"
        self.summary_msg += "平均RTP    =        %2.4f      \n" % self.main_rtp_average
        self.summary_msg += "平均中獎率 =        %2.4f      \n" % self.main_hit_rate_average
        self.summary_msg += "\n\n------------------------------------參考資料-------------------------------------\n\n"
        for i in range(len(self.main_rtp_list)):
            self.summary_msg += "[%10s]:   rtp=     %5.6f     ,   中獎率=     [%2.4f]\n" % (
                self.main_name_list[i], self.main_rtp_list[i], self.main_hit_rate_list[i])

        return self.summary_msg

    def write_message(self, input_msg  ,input_file_name, output_folder=None):
        file_name = input_file_name + str(date.today()) + '-' + str(
            datetime.datetime.now().hour) + str(datetime.datetime.now().minute)
        if output_folder == None:
            file = open(file_name+".txt", "a", encoding="UTF-8")
            file.writelines(input_msg+"\n")

        else:
            folder = output_folder
            file = open("./"+folder+"/"+file_name +
                        '.txt', 'a', encoding='UTF-8')
            file.writelines(input_msg+"\n")
        file.close()


class analyzer_cow_cow_summary_agent_v1():
    def __init__(self):
        self.name = "analyzer_cow_cow_summary_agent_v1"
        self.description = "Il est utilisé pour calculer la distribution d'événements"
    
    def obtenir_title_v1(self,input_list,input_dict):
        msg = "-----------------------------------------------------------------------------------------------------------------------------------------\n"
        msg += "輸入卡片               "
        for k in input_dict:
            msg += "[{:^2s}]  ".format(k)
        msg += "\n"

        msg +="{:^10s} ".format(str(input_list))
        for k in input_dict:
            msg +="[{:^2s}]    ".format(str(input_dict[k]))


        msg += "\n-----------------------------------------------------------------------------------------------------------------------------------------"
        msg += "\n\n"
        return msg

    def obtenir_title_v2(self, input_list, input_dict):
        msg = "-----------------------------------------------------------------------------------------------------------------------------------------\n"
        msg += "輸入卡片: %s\n"%input_list
        for k in input_dict:     
            msg += "[{:^8s}]:".format(k)

            if k == "牛牛": msg += " "
            if k == "四炸": msg += " "
            if k == "牛1":  msg += "  "
            if k == "牛2":  msg += "  "
            if k == "牛3":  msg += "  "
            if k == "牛4":  msg += "  "
            if k == "牛5":  msg += "  "
            if k == "牛6":  msg += "  "
            if k == "牛7":  msg += "  "
            if k == "牛8":  msg += "  "
            if k == "牛9":  msg += "  "
            if k == "無牛": msg += " "
            msg += "  [{:^1s}]".format(str(input_dict[k]))
            msg += "\n"
        msg += "\n"
        msg += "\n-----------------------------------------------------------------------------------------------------------------------------------------"
        msg += "\n\n"
        return msg

class analyzer_brag_summary_agent_v1():
    def __init__(self):
        self.name = "analyzer_cow_cow_summary_agent_v1"
        self.description = "Il est utilisé pour calculer la distribution d'événements"
    
    def obtenir_title_v1(self,input_list,input_dict):
        msg = "-----------------------------------------------------------------------------------------------------------------------------------------\n"
        msg += "輸入卡片               "
        for k in input_dict:
            msg += "[{:^2s}]  ".format(k)
        msg += "\n"

        msg +="{:^10s} ".format(str(input_list))
        for k in input_dict:
            msg +="[{:^2s}]    ".format(str(input_dict[k]))


        msg += "\n-----------------------------------------------------------------------------------------------------------------------------------------"
        msg += "\n\n"
        return msg

    def obtenir_title_v2(self, input_list, input_dict):
        msg = "-----------------------------------------------------------------------------------------------------------------------------------------\n"
        msg += "輸入卡片: %s\n"%input_list
        for k in input_dict:     
            msg += "[{:^8s}]:".format(k)

            if k == "豹子": msg += " "
            if k == "同花順": msg += " "
            if k == "金花":  msg += "  "
            if k == "順子":  msg += "  "
            if k == "對子":  msg += "  "
            if k == "高牌":  msg += "  "
            if k == "特殊":  msg += "  "
            msg += "  [{:^1s}]".format(str(input_dict[k]))
            msg += "\n"
        msg += "\n"
        msg += "\n-----------------------------------------------------------------------------------------------------------------------------------------"
        msg += "\n\n"
        return msg


################################# Static ###########################################


class analyzer_static_class():
    def __init__(self, input_code_name, input_ui_name="None"):
        self.code_name = input_code_name
        self.cnts = 0
        self.ui_name = input_ui_name

    def augmenter(self):
        self.cnts += 1

    def obtenir_des_informations(self):
        return self.code_name, self.cnts, self.ui_name


class analyzer_static_monitor_agent_v1():

    def __init__(self):

        self.name = "analyzer_static_monitor_agent_v1"
        self.analyzer_static_class_list = []
        self.class_number = 0
        self.analyzer_static_class_dictionary = {}
        self.inverse_analyzer_static_class_dictionary = {}
        print("[System]: 啟用 analyzer_static_monitor_agent_v1! ")
    
    
    def append_class(self, input_code_name, input_ui_name="None"):
        if input_ui_name == "None":
            tem_analyzer_static_class = analyzer_static_class(input_code_name)
        else:
            tem_analyzer_static_class = analyzer_static_class(
                input_code_name, input_ui_name)

        self.analyzer_static_class_list.append(tem_analyzer_static_class)
        self.class_number += 1
        self.__updatedict__()


    def __updatedict__(self):
        self.analyzer_static_class_dictionary = { index: any_class.ui_name for index, any_class in enumerate(self.analyzer_static_class_list)}
        self.inverse_analyzer_static_class_dictionary = {v:k for k,v in self.analyzer_static_class_dictionary.items()}

    def __total_cnts__(self):
        cnts = 0
        for any_class in self.analyzer_static_class_list:
            cnts += any_class.cnts
        return cnts


    def increase_cnts(self, input_code_name):
        check_twice = 0
        msg = ""
        for any_class in self.analyzer_static_class_list:
            if any_class.code_name == input_code_name:
                any_class.augmenter()
                check_twice += 1

        if check_twice > 1:  # over twice
            msg = "[Analyzer_Static_Monitor_Agent]: Error, happen twice when increasing the cnts !"
            print(msg)

        return msg

    def increase_cnts_by_index(self, input_index):
        self.analyzer_static_class_list[input_index].augmenter()

    def get_cnts_by_name(self, input_name):
        if_find_any = 0
        for any_class in self.analyzer_static_class_list:
            if any_class.code_name == input_name:
                if_find_any = 1
                return any_class.cnts
        if if_find_any == 0:
            print("[Agent][Error]: Can't find any class match the name %s" %
                  input_name)

    def get_cnts_by_index(self, input_index):
        return self.analyzer_static_class_list[input_index].cnts

    def show_cnts(self):
        msg = "[Static Monitor Agent] Monitor Numbers = %d\n" % self.class_number
        for index, any_class in enumerate(self.analyzer_static_class_list):
            msg += "Class:Index: [{:^2d}] Name: [{:^25s}], cnts: [{:^6d}],      UI_Name: [{:^15s}]       \n"\
                .format(index, any_class.code_name, any_class.cnts, any_class.ui_name)
        return msg

    # Example: The probability to calculate, get GoldenShark or Cow_Cow distribution. 
        # Check show_probab ility_by_input_cnts for another way to show probability.
    def show_probability(self):
        total_cnts = self.__total_cnts__()
        msg = "[Static Monitor Agent] Monitor Numbers = %d\n" % self.class_number
        for index, any_class in enumerate(self.analyzer_static_class_list):
            prob = any_class.cnts / total_cnts
            msg += "Class:Index: [{:^2d}] Name: [{:^25s}], 發生次數: [{:^6d}],  機率: [{:^1.6f}]      UI_Name: [{:^20s}]       \n"\
                .format(index, any_class.code_name, any_class.cnts, prob,any_class.ui_name)
        return msg

    # Example: The probability to claculate G1_3line, S1_4line with total_run_counts.
        # Check show_probab ility for another way to show probability.
    def show_probability_by_input_cnts(self,input_cnts):
        total_cnts = input_cnts
        msg = "[Static Monitor Agent] Monitor Numbers = %d\n" % self.class_number
        for index, any_class in enumerate(self.analyzer_static_class_list):
            prob = any_class.cnts / total_cnts
            msg += "Class:Index: [{:^2d}] Name: [{:^25s}], 發生次數: [{:^6d}],  機率: [{:^1.6f}]      UI_Name: [{:^20s}]       \n"\
                .format(index, any_class.code_name, any_class.cnts, prob,any_class.ui_name)
        return msg
        
    def show_probability_v1_with_input_total_cnts(self,input_total_cnts):
        msg  = "[Static Monitor Agent: show_probability_v1_with_input_total_cnts] Monitor Numbers = %d\n" % self.class_number
        msg += "總共運行次數: %d\n"%input_total_cnts
        total_cnts = input_total_cnts
        for index, any_class in enumerate(self.analyzer_static_class_list):
            prob = any_class.cnts / total_cnts
            msg += "Class:Index: [{:^2d}] Name: [{:^25s}], 發生次數: [{:^6d}],  機率: [{:^1.6f}]      UI_Name: [{:^20s}]       \n"\
                .format(index, any_class.code_name, any_class.cnts, prob, any_class.ui_name)
        return msg

    def show_class_dictionary(self):
        msg = ""
        for v in self.analyzer_static_class_dictionary:
            msg += "[static_monitor_agent]: Index: [%d],  Name: [%s]\n" % (
                v, self.analyzer_static_class_dictionary[v])
        return msg


############################### Data Virtualization #############################

class analyzer_plot_agent_v1():
    def __init__(self):
        self.name = "analyzer_plot_agent_v1"
    
    def draw(self,input_list,option_xlabel="X-Axis",option_ylabel="Y-Axis",option_title=False,option_average=False,option_custom_option=False,option_save_fig=False):

        # Font:
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 14,
                }

        # Set Size:
        plt.figure(figsize=[10, 8])

        # Plot
        # Plot Option example  's' for draw square '*' for star
        if option_custom_option:
            plt.plot(input_list, option_custom_option)
        else:
            plt.plot(input_list)


        plt.plot(input_list)


        plt.xlabel(option_xlabel,fontdict=font)
        plt.ylabel(option_ylabel,fontdict=font)
        
        # Option Titile
        if option_title: plt.title(option_title,fontdict=font)

        # Option average line:
        if option_average: 
            average_value = Moyenne(input_list,option_average)
            average_list = [average_value for _ in range(len(input_list))]
            plt.plot(average_list,'r--',label="Average")
            plt.legend(loc='upper left')

            #Plot txt, 
            text_x_pos        = len(input_list) / 2
            text_y_pos        = ((max(input_list) - average_value) * 0.8 )+ average_value
            input_str             = "Average = %.4f"%average_value
            plt.text(text_x_pos,text_y_pos,'%s'%input_str,fontdict=font)

        # Plot ou save
        if option_save_fig:
            self.__save_fig(plt, option_save_fig)
        else:
            plt.show()

    def draw_bar(self,input_list,input_label_list,option_xlabel="X-Axis",option_ylabel="Y-Axis",option_title=False,option_save_fig=False,option_xticks=[4,20]):

        # Font:
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 14,
                }
        
        # Set option_xticks = [fontsize, rotation]
        option_xticks_font_at_0     = option_xticks[0]
        option_xticks_rotation_at_1 = option_xticks[1]

        # Set Size:
        plt.figure(figsize=[10, 8])

        # Check both size:
        if len(input_list) == len(input_label_list):
            pass
        else:
            print("Error: the two list is not the same size. (input_list, input_label_list) = (%d, %d)"%(len(input_list),len(input_label_list)))

        # Obtenir x_index 
        x_index = np.arange(len(input_label_list))

        # Draw Bar
        plt.bar(x_index, input_list)
        plt.xticks(x_index,input_label_list,fontsize=option_xticks_font_at_0,rotation=option_xticks_rotation_at_1)

        plt.xlabel(option_xlabel,fontdict=font)
        plt.ylabel(option_ylabel,fontdict=font)
        
        # Option Titile
        if option_title: plt.title(option_title,fontdict=font)

        if option_save_fig:
            self.__save_fig(plt, option_save_fig)
        else:
            plt.show()

    def draw_hist(self, input_list,input_bins,option_xlabel="X-Axis", option_ylabel="Y-Axis", option_title="Histogram_Chart",option_font_size=15,option_save_fig=False):
        # Font:
        font = {'family': 'serif',
               'color':  'darkred',
               'weight': 'normal',
               'size': option_font_size,
               }

        # Set size et plot histogram
        plt.figure(figsize=[10,8])
        plt.hist(input_list,bins=input_bins,color='#0504aa',alpha=0.7,rwidth=0.85)
        
        # Set les information
        plt.grid(axis='y', alpha=0.75)
        plt.xticks(fontsize=option_font_size)
        plt.yticks(fontsize=option_font_size)
        plt.title(option_title,fontdict=font)
        plt.xlabel(option_xlabel,fontdict=font)
        plt.ylabel(option_ylabel,fontdict=font)

        if option_save_fig:
            self.__save_fig(plt,option_save_fig)
        else:
            plt.show()

    def draw_double_bar(self,input_1_list,input_2_list,input_label_list,input_width=0.25,option_xlabel="X-Axis",option_ylabel="Y-Axis",option_title=False,option_legend_list=False,option_save_fig=False):
        # Font:
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 14,
                }

        # Set Size:
        plt.figure(figsize=[10, 8])

        # Check both size:
        if len(input_1_list) == len(input_label_list) and len(input_2_list) == len(input_label_list):
            pass
        else:
            print("Error: the two list is not the same size. (input_list, input_label_list) = (%d, %d)"%(len(input_1_list),len(input_label_list)))

        # Obtenir x_index 
        x_index = np.arange(len(input_label_list))

        # Draw Multi Bar
        

        plt.bar(x_index, input_1_list,color='b',align='center',width=input_width)
        plt.bar(x_index+0.2, input_2_list,color='goldenrod',align='center',width=input_width)
        plt.xticks(x_index,input_label_list,fontsize=7,rotation=30)

        plt.xlabel(option_xlabel,fontdict=font)
        plt.ylabel(option_ylabel,fontdict=font)

        # Legend
        if option_legend_list:
            plt.legend(option_legend_list,loc=2)
        else:
            pass
        
        # Option Titile
        if option_title: plt.title(option_title,fontdict=font)

        # Plot ou Save
        if option_save_fig:
            self.__save_fig(plt, option_save_fig)
        else:
            plt.show()

    def draw_x_y(self,input_list_x,input_list_y,option_xlabel="X-Axis",option_ylabel="Y-Axis",option_title=False,option_save_fig=False):
        # Font:
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 14,
                }
        # Set Size:
        plt.figure(figsize=[10, 8])

        # Plot
        plt.plot(input_list_x,input_list_y)
        plt.xlabel(option_xlabel,fontdict=font)
        plt.ylabel(option_ylabel,fontdict=font)
        
        # Option Titile
        if option_title: plt.title(option_title,fontdict=font)
        
        # Plot ou Save
        if option_save_fig:
            self.__save_fig(plt, option_save_fig)
        else:
            plt.show()

    def draw_two_line(self,data_1, data_2, option_xlabel="X-Axis",option_data1_ylabel='Data-1: Y-Axis',option_data2_ylabel='Data-2: Y-Axis', option_title=False, option_data1_average=False,option_save_fig=False):
        
        # Font:
        font = {'family': 'serif',
                'weight': 'normal',
                'size': 14,
                }

        # Set Size:
        plt.figure(figsize=[10, 8])

        # Créer Data 1 and Fig Structure
        fig, ax1 = plt.subplots()

        data_1_color = 'tab:red'
        ax1.set_xlabel(option_xlabel,fontdict=font)
        ax1.set_ylabel(option_data1_ylabel,color=data_1_color,fontdict=font)
        ax1.plot(data_1,color=data_1_color)

        # Créer Data 2 accord la Data 1's template
        ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis

        data_2_color = 'tab:blue'
        ax2.set_ylabel(option_data2_ylabel,color=data_2_color)
        ax2.plot(data_2,color=data_2_color)

        fig.tight_layout() # otherwise, the right y-label is slightly clipped

        # Option Title
        if option_title: plt.title(option_title,fontdict=font)

        # Option average line in data1:
        if option_data1_average:
            average_value = Moyenne(data_1,option_data1_average)
            average_list = [average_value for _ in range(len(data_1))]
            plt.plot(average_list,'r--',label="Average")
            plt.legend(loc='upper left')

            #Plot txt, 
            text_x_pos        = len(data_1) / 2
            text_y_pos        = ((max(data_1) - average_value) * 0.8 )+ average_value
            input_str             = "Average = %.4f"%average_value
            plt.text(text_x_pos,text_y_pos,'%s'%input_str,fontdict=font)

        # Plot ou Save
        if option_save_fig:
            self.__save_fig(plt, option_save_fig)
        else:
            plt.show()

    # Use for general save_fig operation.
    def __save_fig(self, plt, save_norm):
        file_norm = save_norm + ".png"
        plt.savefig(file_norm)
        plt.close('all')

    # Possible to remove the following saving function in the future !
    def save_x_y(self,norm_de_file ,input_list_x, input_list_y, option_xlabel="X-Axis", option_ylabel="Y-Axis", option_title=False,option_output_folder=False):
        # Font:
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 14,
                }

        # Plot
        plt.plot(input_list_x,input_list_y)
        plt.xlabel(option_xlabel,fontdict=font)
        plt.ylabel(option_ylabel,fontdict=font)
        
        # Option Titile
        if option_title: plt.title(option_title,fontdict=font)

        # Enregistrer avec option_output_folder: Default output/oooxxxxx.png
        if option_output_folder:
            file_norm = option_output_folder + "/" + norm_de_file + ".png"
        else:
            file_norm = "output/" + norm_de_file + ".png"

        plt.savefig(file_norm)
        plt.close('all')
    def save_fig_avec_deux_line(self,data_1, data_2, norm_de_file,option_xlabel="X-Axis",option_data1_ylabel='Data-1: Y-Axis',option_data2_ylabel='Data-2: Y-Axis', option_title=False, option_data1_average=False,option_output_folder=False):
        
        # Font:
        font = {'family': 'serif',
                'weight': 'normal',
                'size': 14,
                }
        
        label_data1 = option_data1_ylabel
        label_data2 = option_data2_ylabel


        # Créer Data 1 and Fig Structure
        fig, ax1 = plt.subplots()

        # Option Title
        if option_title: plt.title(option_title,fontdict=font)

        data_1_color = 'tab:red'
        ax1.set_xlabel(option_xlabel,fontdict=font)
        ax1.set_ylabel(option_data1_ylabel,color=data_1_color,fontdict=font)
        ax1.plot(data_1,label=label_data1,color=data_1_color)

        # Créer Data 2 accord la Data 1's template
        ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis

        data_2_color = 'tab:blue'
        ax2.set_ylabel(option_data2_ylabel,color=data_2_color)
        ax2.plot(data_2,label=label_data2,color=data_2_color)

        fig.tight_layout() # otherwise, the right y-label is slightly clipped

        

        # Option average line in data1:
        if option_data1_average:
            average_value = Moyenne(data_1,option_data1_average)
            average_list = [average_value for _ in range(len(data_1))]
            plt.plot(average_list,'r--',label="Average")
            plt.legend(loc='upper left')

            #Plot txt, 
            text_x_pos        = len(data_1) / 2
            text_y_pos        = ((max(data_1) - average_value) * 0.8 )+ average_value
            input_str             = "Average = %.4f"%average_value
            plt.text(text_x_pos,text_y_pos,'%s'%input_str,fontdict=font)
        
        # Enregistrer avec option_output_folder: Default output/oooxxxxx.png
        if option_output_folder:
            file_norm = option_output_folder + "/" + norm_de_file + ".png"
        else:
            file_norm = "output/" + norm_de_file + ".png"
        
        
        plt.savefig(file_norm)
        plt.close('all')
    def savefig(self,input_list,save_norm,option_xlabel="X-Axis",option_ylabel="Y-Axis",option_title=False):
        label_legen = save_norm + "_run"
        plt.plot(input_list,label=label_legen)
        plt.xlabel(option_xlabel)
        plt.ylabel(option_ylabel)
        
        if option_title: plt.title(option_title)
        file_norm = save_norm + ".png"
        plt.savefig(file_norm)
        plt.close('all')
    def savefig_with_limit_range(self,input_list,input_range,save_norm,option_xlabel="X-Axis",option_ylabel="Y-Axis",option_title=False):


        # make new list depend on limit_range
        new_limited_list = copy.deepcopy(input_list[0:input_range+1])

        label_legen = save_norm + "_run"
        plt.plot(new_limited_list, label=label_legen)
        plt.xlabel(option_xlabel)
        plt.ylabel(option_ylabel)
        
        if option_title: plt.title(option_title)
        file_norm = save_norm + ".png"
        plt.savefig(file_norm)
        plt.close('all')
    # ------------------------------------End ------------------------------------------------
