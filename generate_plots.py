import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create report_assets directory if it doesn't exist
if not os.path.exists('report_assets'):
    os.makedirs('report_assets')

# Load datasets - note the space in 'matches .csv'
matches = pd.read_csv('matches .csv')
deliveries = pd.read_csv('deliveries.csv')
points_table = pd.read_csv('points_table.csv')

# Set style
sns.set(style="whitegrid")

# 1. Wicket Types Distribution
plt.figure(figsize=(10, 6))
wicket_types = deliveries['wicket_type'].value_counts()
sns.barplot(x=wicket_types.values, y=wicket_types.index, palette="mako")
plt.title("Wicket Types Distribution - World Cup 2023", fontsize=15)
plt.xlabel("Count")
plt.ylabel("Wicket Type")
plt.tight_layout()
plt.savefig('report_assets/wicket_types.png')
plt.close()

# 2. Top 10 Batsmen (Total Runs)
plt.figure(figsize=(10, 6))
# Column names in deliveries.csv: striker, runs_off_bat
top_batsmen = deliveries.groupby('striker')['runs_off_bat'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette="viridis")
plt.title("Top 10 Run Scorers - World Cup 2023", fontsize=15)
plt.xlabel("Total Runs")
plt.ylabel("Batsman")
plt.tight_layout()
plt.savefig('report_assets/top_batsmen.png')
plt.close()

# 3. Top 10 Bowlers (Wickets)
plt.figure(figsize=(10, 6))
# Filter out non-wicket events
wickets = deliveries[deliveries['wicket_type'].notna() & (~deliveries['wicket_type'].isin(['run out', 'retired hurt', 'obstructing the field', 'retired out']))]
top_bowlers = wickets.groupby('bowler').size().sort_values(ascending=False).head(10)
sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette="flare")
plt.title("Top 10 Wicket Takers - World Cup 2023", fontsize=15)
plt.xlabel("Wickets taken")
plt.ylabel("Bowler")
plt.tight_layout()
plt.savefig('report_assets/top_bowlers.png')
plt.close()

# 4. Toss Impact (Bat First vs Chasing)
matches['winner_runs'] = matches['winner_runs'].fillna(0)
matches['winner_wickets'] = matches['winner_wickets'].fillna(0)
bat_first_wins = matches[matches['winner_runs'] > 0].shape[0]
bowl_first_wins = matches[matches['winner_wickets'] > 0].shape[0]

plt.figure(figsize=(7, 7))
plt.pie([bat_first_wins, bowl_first_wins], labels=["Bat First (Defending)", "Chasing (Bowling First)"], 
        autopct="%1.1f%%", startangle=90, colors=['#ff9999','#66b3ff'])
plt.title("Bat First vs Chasing Wins - World Cup 2023")
plt.tight_layout()
plt.savefig('report_assets/toss_impact.png')
plt.close()

# 5. Points Table Visualization
plt.figure(figsize=(10, 6))
points_table = points_table.sort_values('Points', ascending=False)
sns.barplot(x='Points', y='Team', data=points_table, palette="coolwarm")
plt.title("Final Points Table Standings - ICC World Cup 2023", fontsize=15)
plt.xlabel("Points")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig('report_assets/points_table.png')
plt.close()

# 6. Net Run Rate (NRR) Visualization
plt.figure(figsize=(10, 6))
# Column name in points_table.csv: Net Run Rate
points_table_nrr = points_table.sort_values('Net Run Rate', ascending=False)
sns.barplot(x='Net Run Rate', y='Team', data=points_table_nrr, palette="magma")
plt.title("Net Run Rate (NRR) by Team - World Cup 2023", fontsize=15)
plt.xlabel("Net Run Rate")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig('report_assets/nrr_distribution.png')
plt.close()

# 7. Boundaries Distribution (Fours vs Sixes)
fours = (deliveries['runs_off_bat'] == 4).sum()
sixes = (deliveries['runs_off_bat'] == 6).sum()
plt.figure(figsize=(7, 7))
plt.pie([fours, sixes], labels=["Fours", "Sixes"], autopct="%1.1f%%", startangle=90, colors=['#ffcc99','#99ff99'])
plt.title("Boundaries Distribution (Fours vs Sixes)")
plt.tight_layout()
plt.savefig('report_assets/boundaries_distribution.png')
plt.close()

# 8. Runs Distribution (Batting vs Extras)
batting_runs = deliveries['runs_off_bat'].sum()
extras = deliveries['extras'].sum()
plt.figure(figsize=(7, 7))
plt.pie([batting_runs, extras], labels=["Batting Runs", "Extras"], autopct="%1.1f%%", startangle=90, colors=['#ff9999','#66b3ff'])
plt.title("Runs Distribution (Batting vs Extras)")
plt.tight_layout()
plt.savefig('report_assets/runs_distribution.png')
plt.close()

# 9. Most Toss Wins by Team
plt.figure(figsize=(10, 6))
toss_wins = matches['toss_winner'].value_counts()
sns.barplot(x=toss_wins.values, y=toss_wins.index, palette="viridis")
plt.title("Most Toss Wins - ICC World Cup 2023", fontsize=15)
plt.xlabel("Toss Wins")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig('report_assets/toss_wins.png')
plt.close()

print("All plots generated successfully in report_assets folder.")
