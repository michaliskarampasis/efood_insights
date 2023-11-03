# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

################################

####### Recommend Users #######

###############################

# 1.Order Frequency

# function to plot the distribution of orders
def distribution_of_orders_per_segment(order_freq_month,order_freq_dow,order_freq_hour):
    
    # create a figure with one column and three rows
    fig, axs = plt.subplots(3, 1, figsize=(15, 24), dpi=100, facecolor='white')
    
    # Create the first heatmap
    sns.heatmap(order_freq_month, cmap='YlGnBu', annot=True, fmt='d', cbar=True, linewidths=0.5, ax=axs[0])
    axs[0].set_title('Orders per Month per Segment')
    axs[0].set_xlabel('Segment')
    axs[0].set_ylabel('Month')
    
    # Create the second heatmap
    sns.heatmap(order_freq_dow, cmap='YlGnBu', annot=True, fmt='d', cbar=True, linewidths=0.5, ax=axs[1])
    axs[1].set_title('Orders per Day of the Week per Segment')
    axs[1].set_xlabel('Segment')
    axs[1].set_ylabel('Day of the Week')
    
    # Create the third heatmap
    sns.heatmap(order_freq_hour, cmap='YlGnBu', annot=True, fmt='d', cbar=True, linewidths=0.5, ax=axs[2])
    axs[2].set_title('Orders per Hour per Segment')
    axs[2].set_xlabel('Segment')
    axs[2].set_ylabel('Hour')
    
    # Adjust the spacing between subplots
    plt.tight_layout()
    
    # save the image
    plt.savefig('./images/recommend_users/1.order_frequency/Order Frequency per Segment.png', bbox_inches='tight')
    
    # Show the plot
    plt.show()
    
    return   

# 3. Segments vs Repeaters

# plot comparison of repeaters per segment regarding total number of users
def plot_repeaters_per_segment_users(segments_repeaters):
    
    # create a bar plot with three bars for each device category
    fig, ax = plt.subplots(figsize=(15, 5), dpi=100, facecolor='white') 
    
    # barplot
    segments_repeaters.plot(kind='bar', ax=ax, width=0.9, color = ['indianred','teal','orange'])
    
    # define title and legend 
    plt.title('Total Number of Repeaters per Month per Segment')
    plt.xlabel('Month')
    plt.ylabel('Total Repeaters')
    plt.legend(['frequent_breakfast_users', 'high_breakfast_spending_users', 'recent_breakfast_order_users'],\
               loc='lower left',bbox_to_anchor=(-0.01, 1.1))
    
    # add values inside the bars
    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),\
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
    
    # rotate the x-axis labels horizontally
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    
    #save image
    plt.savefig('./images/recommend_users/3.segments_vs_repeaters/Total Number of Repeaters per Month per Segment.png',\
                bbox_inches='tight')
    
    plt.show()
    
    return

# plot comparison of repeaters per segment regarding total orderd
def plot_repeaters_per_segment_orders(orders_segments_repeaters):
    
    # create a bar plot with three bars for each device category
    fig, ax = plt.subplots(figsize=(15, 5), dpi=100, facecolor='white') 
    
    # barplot
    orders_segments_repeaters.plot(kind='bar', ax=ax, width=0.9, color = ['indianred','teal','orange'])
    
    # define title and legend 
    plt.title('Total Orders per Month per Segment ~ Repeaters')
    plt.xlabel('Month')
    plt.ylabel('Total Orders')
    plt.legend(['frequent_breakfast_users', 'high_breakfast_spending_users', 'recent_breakfast_order_users'],\
               loc='lower left',bbox_to_anchor=(-0.01, 1.1))
    
    # add values inside the bars
    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),\
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
    
    # rotate the x-axis labels horizontally
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    
    #save image
    plt.savefig('./images/recommend_users/3.segments_vs_repeaters/Total Orders per Month per Segment ~ Repeaters.png',\
                bbox_inches='tight')
    
    plt.show()
    
    return

# 4. Segments per Location

# function to plot total orders per city & per location
def heatmap_orders_per_city_per_location(order_freq_hour):
    
    # create figure size
    plt.figure(figsize=(15, 6), dpi=100, facecolor='white')  
    
    # create the heatmap
    sns.heatmap(order_freq_hour, annot=True, fmt='g', cmap='Blues', cbar=True, linewidths=0.5)
    
    # define titles and labels
    plt.title('Order Counts by City')
    plt.xlabel('Order Count')
    plt.ylabel('City')
    
    # save image
    plt.savefig('./images/recommend_users/4.segments_per_location/Total Orders per City per Segment ~ Repeaters.png',\
                bbox_inches='tight')
    
    plt.show()
    
    return
