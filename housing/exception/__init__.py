import os
import sys


class HousingException(Exception):

    def __init__(self, error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        ## self.error_message=error_message
        self.error_message=HousingException.get_detailes_error_message(error_message=error_message,
                                                                       error_detail=error_detail)


    @staticmethod
    def get_detailes_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message : Exception object
        error_detail: object of sys module
        """
        _,_ ,exec_tb=error_detail.exc_info()
        file_name = exec_tb.tb_frame.f_code.co_filename
        line_number=exec_tb.tb_lineno
        error_message=f"Error occured in script :[{file_name}] at line number : [{line_number}] error message: [{error_message}]"

        return error_message
    
    def __str__(self):
        """
        if we print(HousingException()) it will return 
        the print statement of class, 
        how this object should be visible in print statement
        """
        return self.error_message
    
    def __repr__(self) -> str:
        """
        if we call HousingException() it will return 
        the representation of class or object of this class,
        how this object should be visible without print statement
        """
        return HousingException.__init__.str()