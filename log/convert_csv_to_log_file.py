import pandas as pd

# Read the CSV file with specified columns
df = pd.read_csv('./log/logging.csv', usecols=['number','sys_created_on','sys_created_by','opened_at','resolved_at','reopened_time','activity_due','closed_at','closed_by','due_date','sla_due','contact_type','category','urgency','short_description','priority','state','escalation'])

# Write to text log file with specific formatting
with open('./log/logging.log', 'w') as file:
    for index, row in df.iterrows():
        formatted_row = ','.join([
            f'{col}={val}' if isinstance(val, (str, pd.Timestamp)) else f'{col}={val:.2f}' if isinstance(val, float) else f'{col}={val}'
            for col, val in zip(df.columns, row)
        ])
        file.write(formatted_row + '\n')