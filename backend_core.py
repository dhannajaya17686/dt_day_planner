import sqlite3 as sql
import os
from PyQt6.QtCore import QDate
class Backend_core_module():
    def __init__(self)->None:
        self.DATABASE_NAME="day_planner.db"
        self.HOUR_LIST=[str(i) for i in range (24)]
        self.IMAGE_PATH="images"
        self.IMAGE_DASH="images/dashboard_image.png"
        self.IMAGE_ICON="images/time.png"
        self.IMAGES_DASH_URL="https://openclipart.org/image/400px/234619"
        self.IMAGES_ICON_URL="https://img.icons8.com/nolan/64/time.png"
        self.NORMAL_MODE_TABLE_NAME="normal_mode"
        self.DAY_COLUMN="date"
        self.ADVANCED_MODE_TABLE_NAME="advanced_mode"

    def images_dir_creator(self)->bool:
        os.mkdir(self.IMAGE_PATH)
        return True
    
    def images_resource_downloader_icon(self)->bool:
        from requests import get
        self.request1=get(self.IMAGES_ICON_URL)
        self.request1_filename=os.path.basename(self.IMAGES_ICON_URL)
        with open (f"{self.IMAGE_PATH}/{self.request1_filename}",'wb') as file1:
            file1.write(self.request1.content)
        return True
    
    def images_resource_downloader_dash(self)->bool:
        from requests import get
        self.request2=get(self.IMAGES_DASH_URL)
        self.request2_filename=os.path.basename(self.IMAGES_DASH_URL)
        with open (f"{self.IMAGE_PATH}/dashboard_image.png",'wb') as file2:
            file2.write(self.request2.content)
        return True

    
    def db_creator(self)->bool:
        self.db_connection=sql.connect(self.DATABASE_NAME)
        self.db_cursor=self.db_connection.cursor()      
        return True
    
    def resources_checker(self)->bool:
        if  not os.path.isdir(self.IMAGE_PATH):
            self.images_dir_creator()
        if not os.path.isfile(self.IMAGE_ICON):
            self.images_resource_downloader_icon()
        if not os.path.isfile(self.IMAGE_DASH):
            self.images_resource_downloader_dash()            
        if not os.path.isfile(self.DATABASE_NAME):
            self.db_creator()
        return True

    def normal_mode_table_creator(self)->bool:
        self.sql_query_normal_table_add=f"CREATE TABLE IF NOT EXISTS {self.NORMAL_MODE_TABLE_NAME}(day_id INTEGER PRIMARY KEY AUTOINCREMENT, {self.DAY_COLUMN} CHAR(50) NOT NULL,{self.HOUR_LIST[0]} VARCHAR(255), {self.HOUR_LIST[1]} VARCHAR(255), {self.HOUR_LIST[2]} VARCHAR(255), {self.HOUR_LIST[3]} VARCHAR(255), {self.HOUR_LIST[4]} VARCHAR(255), {self.HOUR_LIST[5]} VARCHAR(255), {self.HOUR_LIST[6]} VARCHAR(255), {self.HOUR_LIST[7]} VARCHAR(255), {self.HOUR_LIST[8]} VARCHAR(255), {self.HOUR_LIST[9]} VARCHAR(255), {self.HOUR_LIST[10]} VARCHAR(255), {self.HOUR_LIST[11]} VARCHAR(255), {self.HOUR_LIST[12]} VARCHAR(255), {self.HOUR_LIST[13]} VARCHAR(255), {self.HOUR_LIST[14]} VARCHAR(255), {self.HOUR_LIST[15]} VARCHAR(255), {self.HOUR_LIST[16]} VARCHAR(255), {self.HOUR_LIST[17]} VARCHAR(255), {self.HOUR_LIST[18]} VARCHAR(255), {self.HOUR_LIST[19]} VARCHAR(255), {self.HOUR_LIST[20]} VARCHAR(255), {self.HOUR_LIST[21]} VARCHAR(255), {self.HOUR_LIST[22]} VARCHAR(255), {self.HOUR_LIST[23]} VARCHAR(255))"
        self.db_cursor.execute(self.sql_query_normal_table_add)
        self.db_connection.commit()
        return True

    def advanced_mode_creator(self)->bool:
        self.sql_query_advanced_table_add=f"CREATE TABLE IF NOT EXISTS {self.ADVANCED_MODE_TABLE_NAME}(day_id INTEGER PRIMARY KEY AUTOINCREMENT, {self.DAY_COLUMN} CHAR(50) NOT NULL,{self.HOUR_LIST[0]} VARCHAR(255), {self.HOUR_LIST[1]} VARCHAR(255), {self.HOUR_LIST[2]} VARCHAR(255), {self.HOUR_LIST[3]} VARCHAR(255), {self.HOUR_LIST[4]} VARCHAR(255), {self.HOUR_LIST[5]} VARCHAR(255), {self.HOUR_LIST[6]} VARCHAR(255), {self.HOUR_LIST[7]} VARCHAR(255), {self.HOUR_LIST[8]} VARCHAR(255), {self.HOUR_LIST[9]} VARCHAR(255), {self.HOUR_LIST[10]} VARCHAR(255), {self.HOUR_LIST[11]} VARCHAR(255), {self.HOUR_LIST[12]} VARCHAR(255), {self.HOUR_LIST[13]} VARCHAR(255), {self.HOUR_LIST[14]} VARCHAR(255), {self.HOUR_LIST[15]} VARCHAR(255), {self.HOUR_LIST[16]} VARCHAR(255), {self.HOUR_LIST[17]} VARCHAR(255), {self.HOUR_LIST[18]} VARCHAR(255), {self.HOUR_LIST[19]} VARCHAR(255), {self.HOUR_LIST[20]} VARCHAR(255), {self.HOUR_LIST[21]} VARCHAR(255), {self.HOUR_LIST[22]} VARCHAR(255), {self.HOUR_LIST[23]} VARCHAR(255))"
        self.db_cursor.execute(self.sql_query_advanced_table_add)
        self.db_connection.commit()
        return True

    def normal_mode_submitter(self,activity_dic:dict)->bool:
        self.normal_table_add=f"INSERT INTO {self.NORMAL_MODE_TABLE_NAME}({self.DAY_COLUMN}, {self.HOUR_LIST[0]}, {self.HOUR_LIST[1]}, {self.HOUR_LIST[2]}, {self.HOUR_LIST[3]}, {self.HOUR_LIST[4]}, {self.HOUR_LIST[5]}, {self.HOUR_LIST[6]}, {self.HOUR_LIST[7]}, {self.HOUR_LIST[8]}, {self.HOUR_LIST[9]}, {self.HOUR_LIST[10]}, {self.HOUR_LIST[11]}, {self.HOUR_LIST[12]}, {self.HOUR_LIST[13]}, {self.HOUR_LIST[14]}, {self.HOUR_LIST[15]}, {self.HOUR_LIST[16]}, {self.HOUR_LIST[17]}, {self.HOUR_LIST[18]}, {self.HOUR_LIST[19]}, {self.HOUR_LIST[20]}, {self.HOUR_LIST[21]}, {self.HOUR_LIST[22]}, {self.HOUR_LIST[23]}) VALUES ({activity_dic['tomorrow_date']}, {activity_dic[0]}, {activity_dic[1]}, {activity_dic[2]}, {activity_dic[3]}, {activity_dic[4]}, {activity_dic[5]}, {activity_dic[6]}, {activity_dic[7]}, {activity_dic[8]}, {activity_dic[9]}, {activity_dic[10]}, {activity_dic[11]}, {activity_dic[12]}, {activity_dic[13]}, {activity_dic[14]}, {activity_dic[15]}, {activity_dic[16]}, {activity_dic[17]}, {activity_dic[18]}, {activity_dic[19]}, {activity_dic[20]}, {activity_dic[21]}, {activity_dic[22]}, {activity_dic[23]});"
        self.db_cursor.execute(self.normal_table_add)
        self.db_connection.commit()
        return True

    def advanced_mode_submitter(self,activity_dic:dict)->bool:
        self.advanced_table_add=f"INSERT INTO {self.ADVANCED_MODE_TABLE_NAME}({self.DAY_COLUMN}, {self.HOUR_LIST[0]}, {self.HOUR_LIST[1]}, {self.HOUR_LIST[2]}, {self.HOUR_LIST[3]}, {self.HOUR_LIST[4]}, {self.HOUR_LIST[5]}, {self.HOUR_LIST[6]}, {self.HOUR_LIST[7]}, {self.HOUR_LIST[8]}, {self.HOUR_LIST[9]}, {self.HOUR_LIST[10]}, {self.HOUR_LIST[11]}, {self.HOUR_LIST[12]}, {self.HOUR_LIST[13]}, {self.HOUR_LIST[14]}, {self.HOUR_LIST[15]}, {self.HOUR_LIST[16]}, {self.HOUR_LIST[17]}, {self.HOUR_LIST[18]}, {self.HOUR_LIST[19]}, {self.HOUR_LIST[20]}, {self.HOUR_LIST[21]}, {self.HOUR_LIST[22]}, {self.HOUR_LIST[23]}) VALUES ({activity_dic['selected_date']}, {activity_dic[0]}, {activity_dic[1]}, {activity_dic[2]}, {activity_dic[3]}, {activity_dic[4]}, {activity_dic[5]}, {activity_dic[6]}, {activity_dic[7]}, {activity_dic[8]}, {activity_dic[9]}, {activity_dic[10]}, {activity_dic[11]}, {activity_dic[12]}, {activity_dic[13]}, {activity_dic[14]}, {activity_dic[15]}, {activity_dic[16]}, {activity_dic[17]}, {activity_dic[18]}, {activity_dic[19]}, {activity_dic[20]}, {activity_dic[21]}, {activity_dic[22]}, {activity_dic[23]});"
        self.db_cursor.execute(self.normal_table_add)
        self.db_connection.commit()
        return True
    
    def normal_mode_show(self)->list:
        self.normal_result_list=[]
        self.normal_view_all=f"SELECT * FROM {self.NORMAL_MODE_TABLE_NAME} WHERE {self.DAY_COLUMN}={QDate.currentDate().toString('yyyy-MM-dd')}"
        query_obj=self.db_cursor.execute(self.normal_view_all)
        for items in query_obj:
            converted_item=list(items)
            self.normal_result_list.append(converted_item)
        return self.normal_result_list


    def advanced_mode_show(db_name:str,date:str,self)->list:
        pass
