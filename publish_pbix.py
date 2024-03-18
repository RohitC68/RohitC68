from powerbiclient import Report, PowerBIClient
import os

# Set Power BI credentials from environment variables
username = os.environ.get('PB_USERNAME')
password = os.environ.get('PB_PASSWORD')

# Set workspace ID
workspace_id = "4218b6e2-e5e1-4ea3-b02b-856785b13af3"

# Set path to .pbix file
pbix_file_path = "sales dashboard for capstone project.pbip"

# Authenticate with Power BI service
client = PowerBIClient()
client.authenticate(username, password)

# Publish .pbix file to Power BI service
report = Report()
report.publish(workspace_id, pbix_file_path)
