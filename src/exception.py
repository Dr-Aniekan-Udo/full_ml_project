import sys
import logging

def error_message(error,error_detail:sys):
    #let collect the exception information
    _,_,exc_tb=error_detail.exc_info()
    #get the file name which the error occured
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_display='Error occurred in python script name[{0}] in line numer [{1}] error message[{2}]'.format(file_name,exc_tb.tb_lineno,str(error))
    return error_display
    
class CustomException(Exception):
    #create a constructor
    def __init__(self,error_display,error_detail:sys):
        #use the error meage to inherit the exception class
        super().__init__(error_display)
        #call the error function and assign the parameters
        self.error_out=error_message(error_display,error_detail=error_detail)
    
    #what will be printed when error is raised
    def __str__(self):
        return self.error_out
    