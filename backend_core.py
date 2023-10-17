import sqlite3 as sql
import os
from PyQt6.QtCore import QDate
import datetime
class Backend_core_module:
    """
    This class represents the core module of the day planner application's backend.

    Attributes:
    - DATABASE_NAME (str): The name of the SQLite database used to store data.
    - HOUR_LIST (list of str): A list of strings representing the 24 hours of a day.
    - IMAGE_PATH (str): The path to the directory where the images used by the application are stored.
    - IMAGE_DASH (str): The path to the image used as the background for the application's dashboard.
    - IMAGE_ICON (str): The path to the image used as the application's icon.
    - IMAGES_DASH_URL (str): The URL to the website where the dashboard image is hosted.
    - IMAGES_ICON_URL (str): The URL to the website where the icon image is hosted.
    - NORMAL_MODE_TABLE_NAME (str): The name of the table used to store data in normal mode.
    - DAY_COLUMN (str): The name of the column used to store the date in the database.
    - ADVANCED_MODE_TABLE_NAME (str): The name of the table used to store data in advanced mode.
    """
    
    def __init__(self) -> None:
        """
        Initializes an instance of the Backend_core_module class.
        """
        self.DATABASE_NAME="day_planner.db"
        self.HOUR_LIST=[f"hour_{i}_00" for i in range (24)]
        self.HOUR_LIST_RAW=[f"{i}:00" for i in range (24)]
        self.IMAGE_PATH="images"
        self.IMAGE_DASH="images/dashboard_image.png"
        self.IMAGE_ICON="images/time.png"
        self.IMAGES_DASH_URL="https://img.icons8.com/nolan/96/time.png"
        self.IMAGES_ICON_URL="https://img.icons8.com/nolan/64/time.png"
        self.NORMAL_MODE_TABLE_NAME="normal_mode"
        self.DAY_COLUMN="date"
        self.ADVANCED_MODE_TABLE_NAME="advanced_mode"
        self.ACTIVITY_TABLE_NAME="activity_list"
        self.ACTIVITY_TABLE_COL= "activity"
        self.db_connection=sql.connect(self.DATABASE_NAME)
        self.db_cursor=self.db_connection.cursor()
        self.normal_mode_activity_dict={}
        self.advanced_mode_activity_dict={}  


    def images_dir_creator(self)->bool:
        """Creates a directory for storing images.

        Returns:
            bool: True if directory creation is successful.
        """
        os.mkdir(self.IMAGE_PATH)
        return True
    
    def images_resource_downloader_icon(self)->bool:
        """Downloads an image resource from a URL and saves it in the image directory.

        Returns:
            bool: True if image download and save is successful.
        """
        from requests import get
        self.request1=get(self.IMAGES_ICON_URL)
        self.request1_filename=os.path.basename(self.IMAGES_ICON_URL)
        with open (f"{self.IMAGE_PATH}/{self.request1_filename}",'wb') as file1:
            file1.write(self.request1.content)
        return True
    
    def images_resource_downloader_dash(self)->bool:
        """
        Download the dashboard image resource from the specified URL and save it to the local image directory.

        Returns:
            bool: True if the image download and save operation succeeded, False otherwise.
        """
        from requests import get
        self.request2=get(self.IMAGES_DASH_URL)
        self.request2_filename=os.path.basename(self.IMAGES_DASH_URL)
        with open (f"{self.IMAGE_PATH}/dashboard_image.png",'wb') as file2:
            file2.write(self.request2.content)
        return True

    
    def db_creator(self)->bool:
        """
        Creates a connection to the database file specified by `DATABASE_NAME` and a cursor object for executing SQL commands.

        Returns:
        -------
            bool: Returns True if the connection and cursor were successfully created, False otherwise.
        """
        self.db_connection=sql.connect(self.DATABASE_NAME)
        self.db_cursor=self.db_connection.cursor()      
        return True
    
    def resources_checker(self)->bool:
        """
        Check whether all required resources exist in the local file system, and create them if they don't exist.
    
        Returns:
            bool: True if all resources exist or were created successfully, False otherwise.

        """
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
        """
        Creates a new table in the database for the normal mode.
        The table columns are the day of the week and 24 hours of the day.
        Returns True if the table was created successfully, False otherwise.
        """
        self.sql_query_normal_table_add=f"CREATE TABLE IF NOT EXISTS {self.NORMAL_MODE_TABLE_NAME}(day_id INTEGER PRIMARY KEY AUTOINCREMENT, {self.DAY_COLUMN} CHAR(50) NOT NULL,{self.HOUR_LIST[0]} VARCHAR(255), {self.HOUR_LIST[1]} VARCHAR(255), {self.HOUR_LIST[2]} VARCHAR(255), {self.HOUR_LIST[3]} VARCHAR(255), {self.HOUR_LIST[4]} VARCHAR(255), {self.HOUR_LIST[5]} VARCHAR(255), {self.HOUR_LIST[6]} VARCHAR(255), {self.HOUR_LIST[7]} VARCHAR(255), {self.HOUR_LIST[8]} VARCHAR(255), {self.HOUR_LIST[9]} VARCHAR(255), {self.HOUR_LIST[10]} VARCHAR(255), {self.HOUR_LIST[11]} VARCHAR(255), {self.HOUR_LIST[12]} VARCHAR(255), {self.HOUR_LIST[13]} VARCHAR(255), {self.HOUR_LIST[14]} VARCHAR(255), {self.HOUR_LIST[15]} VARCHAR(255), {self.HOUR_LIST[16]} VARCHAR(255), {self.HOUR_LIST[17]} VARCHAR(255), {self.HOUR_LIST[18]} VARCHAR(255), {self.HOUR_LIST[19]} VARCHAR(255), {self.HOUR_LIST[20]} VARCHAR(255), {self.HOUR_LIST[21]} VARCHAR(255), {self.HOUR_LIST[22]} VARCHAR(255), {self.HOUR_LIST[23]} VARCHAR(255))"
        self.db_cursor.execute(self.sql_query_normal_table_add)
        self.db_connection.commit()
        return True
    
    def activity_list_table_creator(self)->bool:
        self.sql_query_activity_list_add=f"CREATE TABLE IF NOT EXISTS {self.ACTIVITY_TABLE_NAME}(activity_id INTEGER PRIMARY KEY AUTOINCREMENT,{self.ACTIVITY_TABLE_COL} CHAR(50) NOT NULL)"
        self.db_cursor.execute(self.sql_query_activity_list_add)
        self.db_connection.commit()
        return True

    def activity_submitter(self,activity_name:str) -> bool :
        self.activity_table_add= f"INSERT INTO {self.ACTIVITY_TABLE_NAME} ({self.ACTIVITY_TABLE_COL}) VALUES ('{activity_name}');"
        self.db_cursor.execute(self.activity_table_add)
        self.db_connection.commit()
        return True 
    
    def activity_return_list(self)->list:
        self.activity_list=[]
        self.get_all_activities=f"SELECT * FROM {self.ACTIVITY_TABLE_NAME};"
        query_obj=self.db_cursor.execute(self.get_all_activities).fetchall()
        for items in query_obj:
            self.activity_list.append(items)
        return self.activity_list
    
    def activity_checker(self,activity_name:str)->bool :
        self.activity_check_query=f""
    
    
    
    def advanced_mode_creator(self)->bool:
        """
        Creates a new table in the database for the advanced mode.
        The table columns are the day of the week and 24 hours of the day.
        Returns True if the table was created successfully, False otherwise.
        """
        self.sql_query_advanced_table_add=f"CREATE TABLE IF NOT EXISTS {self.ADVANCED_MODE_TABLE_NAME}(day_id INTEGER PRIMARY KEY AUTOINCREMENT, {self.DAY_COLUMN} CHAR(50) NOT NULL,{self.HOUR_LIST[0]} VARCHAR(255), {self.HOUR_LIST[1]} VARCHAR(255), {self.HOUR_LIST[2]} VARCHAR(255), {self.HOUR_LIST[3]} VARCHAR(255), {self.HOUR_LIST[4]} VARCHAR(255), {self.HOUR_LIST[5]} VARCHAR(255), {self.HOUR_LIST[6]} VARCHAR(255), {self.HOUR_LIST[7]} VARCHAR(255), {self.HOUR_LIST[8]} VARCHAR(255), {self.HOUR_LIST[9]} VARCHAR(255), {self.HOUR_LIST[10]} VARCHAR(255), {self.HOUR_LIST[11]} VARCHAR(255), {self.HOUR_LIST[12]} VARCHAR(255), {self.HOUR_LIST[13]} VARCHAR(255), {self.HOUR_LIST[14]} VARCHAR(255), {self.HOUR_LIST[15]} VARCHAR(255), {self.HOUR_LIST[16]} VARCHAR(255), {self.HOUR_LIST[17]} VARCHAR(255), {self.HOUR_LIST[18]} VARCHAR(255), {self.HOUR_LIST[19]} VARCHAR(255), {self.HOUR_LIST[20]} VARCHAR(255), {self.HOUR_LIST[21]} VARCHAR(255), {self.HOUR_LIST[22]} VARCHAR(255), {self.HOUR_LIST[23]} VARCHAR(255))"
        self.db_cursor.execute(self.sql_query_advanced_table_add)
        self.db_connection.commit()
        return True

    def normal_mode_submitter(self)->bool:
        """
        Inserts the values in `self.normal_mode_activity_dict` to the advanced mode table for the selected date.
    
        Returns:
        bool: True if the insertion is successful, False otherwise.
        """
        self.normal_table_add = f"INSERT INTO {self.NORMAL_MODE_TABLE_NAME}({self.DAY_COLUMN}, {self.HOUR_LIST[0]}, {self.HOUR_LIST[1]}, {self.HOUR_LIST[2]}, {self.HOUR_LIST[3]}, {self.HOUR_LIST[4]}, {self.HOUR_LIST[5]}, {self.HOUR_LIST[6]}, {self.HOUR_LIST[7]}, {self.HOUR_LIST[8]}, {self.HOUR_LIST[9]}, {self.HOUR_LIST[10]}, {self.HOUR_LIST[11]}, {self.HOUR_LIST[12]}, {self.HOUR_LIST[13]}, {self.HOUR_LIST[14]}, {self.HOUR_LIST[15]}, {self.HOUR_LIST[16]}, {self.HOUR_LIST[17]}, {self.HOUR_LIST[18]}, {self.HOUR_LIST[19]}, {self.HOUR_LIST[20]}, {self.HOUR_LIST[21]}, {self.HOUR_LIST[22]}, {self.HOUR_LIST[23]}) VALUES ('{self.normal_mode_activity_dict['tomorrow_date']}', '{self.normal_mode_activity_dict[0]}', '{self.normal_mode_activity_dict[1]}', '{self.normal_mode_activity_dict[2]}', '{self.normal_mode_activity_dict[3]}', '{self.normal_mode_activity_dict[4]}', '{self.normal_mode_activity_dict[5]}', '{self.normal_mode_activity_dict[6]}', '{self.normal_mode_activity_dict[7]}', '{self.normal_mode_activity_dict[8]}', '{self.normal_mode_activity_dict[9]}', '{self.normal_mode_activity_dict[10]}', '{self.normal_mode_activity_dict[11]}', '{self.normal_mode_activity_dict[12]}', '{self.normal_mode_activity_dict[13]}', '{self.normal_mode_activity_dict[14]}', '{self.normal_mode_activity_dict[15]}', '{self.normal_mode_activity_dict[16]}', '{self.normal_mode_activity_dict[17]}', '{self.normal_mode_activity_dict[18]}', '{self.normal_mode_activity_dict[19]}', '{self.normal_mode_activity_dict[20]}', '{self.normal_mode_activity_dict[21]}', '{self.normal_mode_activity_dict[22]}', '{self.normal_mode_activity_dict[23]}');"
        self.db_cursor.execute(self.normal_table_add)
        self.db_connection.commit()
        return True

    def advanced_mode_submitter(self) -> bool:
        """
        Inserts the values in `self.advanced_mode_activity_dict` to the advanced mode table for the selected date.
    
        Returns:
            bool: True if the insertion is successful, False otherwise.
        """
        self.advanced_table_add = f"INSERT INTO {self.ADVANCED_MODE_TABLE_NAME}({self.DAY_COLUMN}, {self.HOUR_LIST[0]}, {self.HOUR_LIST[1]}, {self.HOUR_LIST[2]}, {self.HOUR_LIST[3]}, {self.HOUR_LIST[4]}, {self.HOUR_LIST[5]}, {self.HOUR_LIST[6]}, {self.HOUR_LIST[7]}, {self.HOUR_LIST[8]}, {self.HOUR_LIST[9]}, {self.HOUR_LIST[10]}, {self.HOUR_LIST[11]}, {self.HOUR_LIST[12]}, {self.HOUR_LIST[13]}, {self.HOUR_LIST[14]}, {self.HOUR_LIST[15]}, {self.HOUR_LIST[16]}, {self.HOUR_LIST[17]}, {self.HOUR_LIST[18]}, {self.HOUR_LIST[19]}, {self.HOUR_LIST[20]}, {self.HOUR_LIST[21]}, {self.HOUR_LIST[22]}, {self.HOUR_LIST[23]}) VALUES ('{self.advanced_mode_activity_dict['selected_date']}', '{self.advanced_mode_activity_dict[0]}', '{self.advanced_mode_activity_dict[1]}', '{self.advanced_mode_activity_dict[2]}', '{self.advanced_mode_activity_dict[3]}', '{self.advanced_mode_activity_dict[4]}', '{self.advanced_mode_activity_dict[5]}', '{self.advanced_mode_activity_dict[6]}', '{self.advanced_mode_activity_dict[7]}', '{self.advanced_mode_activity_dict[8]}', '{self.advanced_mode_activity_dict[9]}', '{self.advanced_mode_activity_dict[10]}', '{self.advanced_mode_activity_dict[11]}', '{self.advanced_mode_activity_dict[12]}', '{self.advanced_mode_activity_dict[13]}', '{self.advanced_mode_activity_dict[14]}', '{self.advanced_mode_activity_dict[15]}', '{self.advanced_mode_activity_dict[16]}', '{self.advanced_mode_activity_dict[17]}', '{self.advanced_mode_activity_dict[18]}', '{self.advanced_mode_activity_dict[19]}', '{self.advanced_mode_activity_dict[20]}', '{self.advanced_mode_activity_dict[21]}', '{self.advanced_mode_activity_dict[22]}', '{self.advanced_mode_activity_dict[23]}');"
        self.db_cursor.execute(self.advanced_table_add)
        self.db_connection.commit()
        return True
            
    def normal_mode_show(self)->list:
        """
        Retrieves all the records from the NORMAL_MODE_TABLE_NAME table for the current date and returns them as a list.

        Returns:
        -------
        list:
            A list of tuples containing the records for the current date. Each tuple contains the values for a single row in the table.
        """
        self.normal_result_list=[]
        self.normal_view_all=f"SELECT * FROM {self.NORMAL_MODE_TABLE_NAME} WHERE {self.DAY_COLUMN}='{QDate.currentDate().toString('yyyy-MM-dd')}';"
        query_obj=self.db_cursor.execute(self.normal_view_all)
        for items in query_obj:
            converted_item=list(items)
            self.normal_result_list.append(converted_item)
        return self.normal_result_list
    
    def today_activities_show(self)->list:
        """
        Retrieves all the records from the NORMAL_MODE_TABLE_NAME table for the current date and returns them as a list.

        Returns:
        -------
        list:
            A list of tuples containing the records for the current date. Each tuple contains the values for a single row in the table.
        """
        self.today_result_list=[]
        self.today_view_all=f"SELECT * FROM {self.ADVANCED_MODE_TABLE_NAME} WHERE {self.DAY_COLUMN}='{QDate.currentDate().toString('yyyy-MM-dd')}';"
        query_obj=self.db_cursor.execute(self.today_view_all)
        for items in query_obj:
            converted_item=list(items)
            self.today_result_list.append(converted_item)
        return self.today_result_list

    def tomorrow_checker(self):
        current_date = QDate.currentDate()
        tomorrow_date = current_date.addDays(1)
        tomorrow_datetime = datetime.datetime(tomorrow_date.year(), tomorrow_date.month(), tomorrow_date.day())
        self.tomorrow_string = tomorrow_datetime.strfti
        self.tomorrow_check=f"SELECT * from {self.NORMAL_MODE_TABLE_NAME} WHERE {self.DAY_COLUMN}='{self.tomorrow_string}';"      
        self.db_cursor.execute(self.tomorrow_check)
        self.db_connection.commit()
        self.results=self.db_cursor.fetchall()
        if self.results:
            return True
        else:
            return False
        
    
    def tomorrow_remover(self):
        self.tomorrow_remover_exec=f"DELETE FROM {self.NORMAL_MODE_TABLE_NAME} WHERE {self.DAY_COLUMN}='{self.tomorrow_string}';"
        self.db_cursor.execute(self.tomorrow_remover_exec)
        self.db_connection.commit()
        return True

    def advanced_mode_show(db_name:str,date:str,self)->list:
        pass
    """
    def test_table_creator(self):
        test=f"CREATE TABLE IF NOT EXISTS test (day_id INTEGER PRIMARY KEY AUTOINCREMENT, {self.DAY_COLUMN} CHAR(50) NOT NULL,{self.HOUR_LIST[0]} VARCHAR(255))"
        self.db_cursor.execute(test)
        self.db_connection.commit()
        return True
    def test_table_submitter(self):
        test_sub = f"INSERT INTO test({self.DAY_COLUMN}, {self.HOUR_LIST[0]}) VALUES ('{self.normal_mode_activity_dict['tomorrow_date']}', '{self.normal_mode_activity_dict[0]}');"
        self.db_cursor.execute(test_sub)
        self.db_connection.commit()
        return True
    """

x=Backend_core_module()
x.activity_submitter("Sleep")
print(x.activity_return_list())