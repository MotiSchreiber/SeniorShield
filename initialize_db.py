import subprocess

# Define MySQL command
mysql_cmd = [
    'docker', 'exec', '-i', 'mysql', 'mysql', '-u', 'your_username', '-pyour_password', 'your_database'
]
def main():
    # Read SQL file
    sql_file = 'people_data.sql'
    with open(sql_file, 'r') as file:
        sql_statements = file.read()

    # Execute MySQL command with SQL file contents as input
    try:
        subprocess.run(mysql_cmd, input=sql_statements, text=True, check=True)
        print("SQL file executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing SQL file: {e}")
