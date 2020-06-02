"""
Roller coaster challenge project for data visualization from Codecademy
Project completed by Kevin Sullivan

Seaborn is used to plot over matplotlib for aesthetic reason
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load rankings data here:


rankings_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
rankings_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# write function to plot rankings over time for 1 roller coaster here:
def plot_coaster_rank(coaster_name, park_name, rankings):
    #create a dataframe with the rollercoaster name at a given park
    df = rankings[rankings.Name == coaster_name]
    df= df[df.Park == park_name]
    
    sns.lineplot(data = df,
                 x = 'Year of Rank',
                 y = 'Rank',
                 markers = False)
    plt.title('Ranking of %s Over Time' % coaster_name)
    plt.xlabel('Year')
    plt.show()

plt.clf()

#plot_coaster_rank('El Toro', 'Six Flags Great Adventure', rankings_wood)

# write function to plot rankings over time for 2 roller coasters here:

def plot_two_coasters_rank(coaster_1, park_1, coaster_2, park_2, rankings):
    #use the query method to get a dataframe with both coasters
    df = rankings.query('(Name == @coaster_1 and Park == @park_1) or (Name == @coaster_2 and Park == @park_2)')
    sns.lineplot(data = df,
                 x = 'Year of Rank',
                 y = 'Rank',
                 hue = 'Name',
                 markers = False)

    plt.title('Ranking of %s and %s Over Time' % (coaster_1, coaster_2))
    plt.xlabel('Year')
    plt.legend()
    plt.show()

#plot_two_coasters_rank('El Toro', 'Six Flags Great Adventure', 'The Beast', 'Kings Island', rankings_wood)





plt.clf()

# write function to plot top n rankings over time here:

#aviding this task for now because the instructions are unclear. May need to start with a given year as parameter to initialize


plt.clf()

# load roller coaster data here:

roller_coasters = pd.read_csv('roller_coasters.csv')

# write function to plot histogram of column values here:

def plot_distribution(col, coasters):
    ax = sns.kdeplot(coasters[col],
                shade = True,
                legend = False)
    plt.title('Distribution of Roller Coaster %s' % col.capitalize())
    sns.despine(left = True)
    ax.set_yticks([])
    plt.ylabel('Frequency')
    plt.xlabel(col.capitalize())
    plt.show()

#plot_distribution('speed', roller_coasters)


plt.clf()

# write function to plot inversions by coaster at a park here:

def plot_inversions(park_name, coasters):
    #check to ensure the park input exists
    if park_name not in coasters.park.tolist():
        print('Error! No such park')
        return 'Error! No such park'
   
    #creates a dataframe for all the coasters in a given park with inversions
    park_data = coasters[coasters.park == park_name]
    park_data = park_data[park_data.num_inversions != 0]
    coaster_names = park_data.name.tolist()
    x_vals = [x for x in range(len(coaster_names))]

    fig = plt.subplot()
    ax = sns.barplot(x = x_vals,
                y = park_data.num_inversions,
                ci = None)
    ax.set_xticks(x_vals)
    ax.set_xticklabels(coaster_names)
    plt.xticks(rotation = -30)
    plt.setp( ax.xaxis.get_majorticklabels(), rotation=-30, ha="left", rotation_mode="anchor") 
    plt.subplots_adjust(bottom = 0.35)
    plt.title('Number of Inversions for Each Coaster at %s' % park_name)
    plt.ylabel('Inversions')
    plt.show()

#user_park = input('Choose a theme park: ')
#plot_inversions(user_park, roller_coasters)





plt.clf()

# write function to plot pie chart of operating status here:

def compare_operating(coasters):
    
    #create the fraction of operational versus permanently closed
    total_status = coasters.status.value_counts()
    op_frac = float(total_status['status.operating']) / (total_status['status.operating'] + total_status['status.closed.definitely'])
    closed_frac = float(total_status['status.closed.definitely']) / (total_status['status.operating'] + total_status['status.closed.definitely'])

    plt.pie([op_frac, closed_frac],
            autopct = '%d%%',
            labels = ['Operating', 'Permanently Closed'])
    plt.axis('equal')
    plt.title('Comparrison of Operational and Permanently Closed Roller Coasters')
    plt.show()

#compare_operating(roller_coasters)




plt.clf()

# write function to create scatter plot of any two numeric columns here:

def scatter_data(col1, col2, coasters):
    sns.scatterplot(x = coasters[col1],
                    y = coasters[col2])
    plt.xlabel(col1.capitalize())
    plt.ylabel(col2.capitalize())
    plt.title('%s vs. %s' % (col1.capitalize(), col2.capitalize()))
    plt.show()

scatter_data('speed', 'height', roller_coasters)

print(roller_coasters[roller_coasters.height > 200])





plt.clf()
