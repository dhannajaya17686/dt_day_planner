class Backend_core_module():
    
    def db_creator(db_name:str)->bool:
        #other blocks go here
        return True

    def db_checker(db_name:str)->bool:
        #the code blocks go here
        return True
    
    def resources_checker(image_path:str)->bool:
        #the code block goes here
        return True

    def normal_mode_table_creator(db_name:str,table_name:str,date:str,hour_list:list)->bool:
        #the code block goes here
        return True

    def advanced_mode_creator(db_name:str,table_name:str,date:str,hour_list:list)->bool:
        #the code block goes here
        return True

    def normal_mode_submitter(db_name:str,date:str,activity_dic:dict)->bool:
        #the code block goes here
        return True

    def advanced_mode_submitter(db_name:str,date:str,activity_dic:dict)->bool:
        #the code block goes here
        return True
    
    def normal_mode_show(db_name:str,date:str)->list:
        pass

    def advanced_mode_show(db_name:str,date:str)->list:
        pass

    