import sqlite3
import pandas as pd 
from config import DB_NAME

def export_multiverse_report():

    try:
        conn = sqlite3.connect(DB_NAME)
        df = pd.read_sql_query("SELECT * FROM characters", conn)
        conn.close()

    except Exception as e:
        print(f"DATABASE ERROR {e}")
        return
    
    if df.empty:
        print("⚠️ The Vault is empty. Run main.py first to gather data.")
        return
    
    species_count = df["species"].value_counts().reset_index()
    status_count = df["status"].value_counts().reset_index()

    try:
        with pd.ExcelWriter("Multiverse_Report.xlsx",engine = 'openpyxl') as writer:
            df.to_excel(writer,sheet_name="Raw_Data", index=False)
            species_count.to_excel(writer,sheet_name='Species_Demographics',index=False)
            status_count.to_excel(writer,sheet_name='Life_Status', index=False)
            print("✅ SUCCESS: Report locked and saved as Multiverse_Report.xlsx" )
    except ModuleNotFoundError:
        print("⚠️ Missing openpyxl. Run this in terminal: pip install openpyxl")

if __name__ == "__main__":
    export_multiverse_report()
