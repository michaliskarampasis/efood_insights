# import libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify


###############################

####### Graphs for EDA #######

##############################


# 1.User Demographics

# function for barplots
def barplot_for_orders_per_class(object_cols,orders_eda, value, kind_of_group):
    
    #create figure
    fig = plt.figure(figsize=(15,5), dpi=100)
    fig.patch.set_facecolor('white')
    plt.style.use('classic')
    
    # create a bar plot 
    custom_palette = sns.color_palette("Reds", n_colors=len(value))[::-1]
    ax = sns.barplot(x=value.index, y=value.values,palette=custom_palette )
    
    #locate text
    for rect in ax.patches:
        ax.text(rect.get_x() + rect.get_width() / 2, 2*rect.get_height() /3, rect.get_height(), \
                horizontalalignment='center', fontsize = 11)
    
    # Add labels and title
    plt.xlabel('{}'.format(object_cols))
    plt.ylabel('Count')
    plt.title('Number of {} per Class'.format(kind_of_group))
    
    #save image
    plt.savefig('./images/eda/1.user_demographics/Number of {} per Class.png'.format(kind_of_group), bbox_inches='tight')
    
    return


# function to create plot regarding revenue per class
def plot_revenue_per_class(revenue_per_class):
    
    # create figure
    fig = plt.figure(figsize=(10,5), dpi=100, facecolor='white')
    fig.patch.set_facecolor('white')
    plt.style.use('classic')
    
    # create palette 
    custom_palette = sns.color_palette('Reds', n_colors=len(revenue_per_class.user_class_name))[::-1]
    
    # calculate the labels to be displayed, including revenue values
    labels = [f'{class_name}\n{round(revenue/1000000,2):.2f}M €' \
              for class_name, revenue in zip(revenue_per_class.user_class_name, revenue_per_class.revenue)]
    
    # create treemap
    squarify.plot(sizes = revenue_per_class.revenue, label = labels,
                  pad = 0.2, text_kwargs = {'fontsize': 10, 'color': 'black'},
                  color = sns.color_palette(custom_palette))
    
    # axis not to be displayed
    plt.axis("off")
    
    # add title
    plt.title('Total Revenue per Class in euros',fontsize=15)
    
    # save image
    plt.savefig('./images/eda/1.user_demographics/Total Revenue per Class.png', bbox_inches='tight')
        
    
    plt.show() 
    
    return

# 2.User Behavior

# function to plot info regarding devices
def barplot_devices(df_device):
    
    # create a bar plot with three bars for each device category
    fig, ax = plt.subplots(figsize=(15, 5), dpi=100, facecolor='white') 
    
    # barplot
    df_device.plot(kind='bar', ax=ax, width=0.9, color = ['royalblue','peru','red'])
    
    # define title and legend 
    plt.title('Orders, Users & Online Payments per Device')
    plt.xlabel('Device')
    plt.ylabel('Count')
    plt.legend(['Order ID', 'User ID', 'Paid Online'])
    
    # add values inside the bars
    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),\
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5), textcoords='offset points')
    
    # rotate the x-axis labels horizontally
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    
    #save image
    plt.savefig('./images/eda/2.user_behavior/Orders, Users & Online Payments per Device.png', bbox_inches='tight')
    
    plt.show()
    
    return


# function to plot payment methods
def pie_chart_payment_method(orders_eda):
    
    # create figure for pie chart
    fig, ax = plt.subplots(figsize=(15, 5), dpi=100, facecolor='white') 
    
    #define colors
    colors = ['lightgrey','red']
    
    # compute how many users pay with cash
    counts = [ orders_eda['paid_cash'].value_counts().iloc[0],  orders_eda['paid_cash'].value_counts().iloc[1]]
    labels = [f'Cash Payment:{counts[0]}', f'Online Payment:{counts[1]}']
    
    # piechart
    plt.pie(counts, labels=labels, explode = (0, 0.2), autopct='%1.1f%%', startangle=90,colors=colors)
    
    #define title
    plt.title('Payment Method Distribution')
    
    #save image
    plt.savefig('./images/eda/2.user_behavior/Payment Method Distribution.png', bbox_inches='tight')
    
    plt.show()
    
    return


# function to plot time series regarding payment methods
def time_series_payment_methods(df_device_per_date):
    
    # Create the time series plot
    plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
    plt.plot(df_device_per_date.index, df_device_per_date['paid_online'], label='Paid Online', marker='o',color='red')
    plt.plot(df_device_per_date.index, df_device_per_date['paid_cash_v2'], label='Paid Cash', marker='o',color='grey')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Payment Methods Over Time')
    plt.legend(loc = 'lower right')
    plt.grid(True)
    
    # rotate x-axis labels for better readability
    plt.xticks(rotation=45)  
    
    # ensure all elements fit in the plot
    plt.tight_layout()  
    
    # save image
    plt.savefig('./images/eda/2.user_behavior/Payment Methods Over Time.png', bbox_inches='tight')
    
    
    plt.show()
    
    return


# function to plot time series regarding deviation of payment methods
def time_series_payment_methods_deviation(df_device_per_date):
    
    # Create the time series plot
    plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
    plt.plot(df_device_per_date.index, df_device_per_date['dev'], label='Deviation', marker='o',color='black')
    plt.xlabel('Date')
    plt.ylabel('Percentage (%) ')
    plt.title('Deviation of Cash from Online Payments (%)')
    plt.legend()
    plt.grid(True)
    
    # rotate x-axis labels for better readability
    plt.xticks(rotation=45)  
    
    # ensure all elements fit in the plot
    plt.tight_layout()  
    
    # save image
    plt.savefig('./images/eda/2.user_behavior/Deviation of Cash from Online Payments (%).png', bbox_inches='tight')
    
    plt.show()
    
    return

# 3.User Retention and Engagement

# function to plot comparison of repeaters and non repeaters
def compare_repeaters_monthly(repeaters_df_monthly):
    
    # create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10), dpi=100, facecolor='white')
    
    # define parameters
    x = np.arange(len(repeaters_df_monthly.index))
    width = 0.3
    
    # bar plots
    rects1a = ax1.bar(x - width / 2, repeaters_df_monthly.one_time_customers_revenue, width, label='One-Time Customers',color='silver')
    rects1b = ax1.bar(x + width / 2, repeaters_df_monthly.repeaters_revenue, width, label='Repeaters',color='lightcoral')
    
    rects2a = ax2.bar(x - width / 2, repeaters_df_monthly.one_time_customers_orders, width, label='One-Time Customers',color='silver')
    rects2b = ax2.bar(x + width / 2, repeaters_df_monthly.repeaters_orders, width, label='Repeaters',color='lightcoral')
    
    
    # function to add labels to the bars
    def add_labels(rects, ax):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
        return
            
    # set the x-tick labels with the months
    months = repeaters_df_monthly.index.to_list()
    ax1.set_xticks(x)
    ax1.set_xticklabels(months)
    ax2.set_xticks(x)
    ax2.set_xticklabels(months)
    
    # add labels to the bars in the first subplot
    add_labels(rects1a, ax1)
    add_labels(rects1b, ax1)
    
    # add labels to the bars in the second subplot
    add_labels(rects2a, ax2)
    add_labels(rects2b, ax2)
    
    # define titles
    ax1.set_title('Monthly Revenue ~ Repeaters vs Non Repeaters')
    ax2.set_title('Monthly Orders ~ Repeaters vs Non Repeaters')
    
    # define legend
    ax1.legend(loc='upper right',bbox_to_anchor=(1.01, 1.3))
    
    plt.tight_layout()
    
    # save image
    plt.savefig('./images/eda/3.user_retention_and_engagement/Repeaters vs Non Repeaters.png', bbox_inches='tight')
    
    plt.show()
    
    return

# 4. Order Trends

# function to plot order trends in monthly level
def plot_order_trends_monthly(orders_per_month,pivot_dayofweek,pivot_hour):
    
    # create a figure
    fig, (ax1, ax2,ax3) = plt.subplots(3, 1, figsize=(15, 25), dpi=100, facecolor='white')
    
    # plot the first bar plot
    x = np.arange(len(orders_per_month.columns))
    ax1.bar(x - 0.4/2, orders_per_month.loc['August'], width=0.35, label='August',color='firebrick')
    ax1.bar(x + 0.4/2, orders_per_month.loc['September'], width=0.35, label='September',color='dimgrey')
    
    # define title for the first subplot
    ax1.set_title('Total Orders per Month')
    ax1.set_ylabel('Orders')
    
    # add values at the bars for the first subplot
    for p in ax1.patches:
        ax1.annotate(str(int(p.get_height())), (p.get_x() + p.get_width() / 2., p.get_height()),\
                    ha='center', va='center', fontsize=16, color='white', xytext=(0, -120), textcoords='offset points')
    
    # add labels to the first subplot
    months = orders_per_month.columns.to_list()
    ax1.set_xticks(x)
    ax1.set_xticklabels(months, rotation=0)
    
    # plot the second bar plot 
    x = np.arange(len(pivot_dayofweek.columns))
    ax2.bar(x - 0.35/2, pivot_dayofweek.loc['August'], width=0.35, label='August',color='firebrick')
    ax2.bar(x + 0.35/2, pivot_dayofweek.loc['September'], width=0.35, label='September',color='dimgrey')
    
    # define x labels for the second subplot
    ax2.set_xticks(x)
    ax2.set_xticklabels(pivot_dayofweek.columns)
    
    # define title and hide the legend for the second subplot
    ax2.set_title('Total Orders per Month per Days of Week')
    ax2.set_xlabel('Days of week')
    ax2.set_ylabel('Orders')
    ax2.legend(loc = 'upper left',bbox_to_anchor=(-0.01, 1.25))
    
    # plot the third bar plot
    x = np.arange(len(pivot_hour.columns))
    ax3.plot(x, pivot_hour.loc['August'], label='August', marker='o', linestyle='-',color='firebrick', linewidth=3)
    ax3.plot(x, pivot_hour.loc['September'], label='September', marker='o', linestyle='-',color='dimgrey', linewidth=3)
    
    # define x labels for the third subplot
    ax3.set_xticks(x)
    ax3.set_xticklabels(pivot_hour.columns)
    
    # define title and hide the legend for the third subplot
    ax3.set_title('Total Orders per Month per Hour')
    ax3.set_xlabel('Hour')
    ax3.set_ylabel('Orders')
    ax3.legend(loc = 'upper left',bbox_to_anchor=(-0.01, 1.25))
    
    plt.tight_layout()
    
    # save image
    plt.savefig('./images/eda/4.order_trends/Total Orders per time.png', bbox_inches='tight')
    
    plt.show()
    
    return

# 5. Location Analysis

# function to compare locations by counting orders
def heatmap_orders_per_city(orders_per_city):
    
    # create figure size
    plt.figure(figsize=(8, 6), dpi=100, facecolor='white')  
    
    # create the heatmap
    sns.heatmap(orders_per_city, annot=True, fmt='g', cmap='Blues')
    
    # define titles and labels
    plt.title('Order Counts by City')
    plt.xlabel('Order Count')
    plt.ylabel('City')
    
    # save image
    plt.savefig('./images/eda/5.location_analysis/Total Orders per City.png', bbox_inches='tight')
    
    plt.show()
    
    return


# function to plot the comparison of locations per hour
def heatmap_orders_per_city_per_hour(heatmap_data):
    
    # create the heatmap
    plt.figure(figsize=(15, 5), dpi=100, facecolor='white')
    sns.heatmap(heatmap_data.T, annot=False, fmt=".2f", cmap="Blues")
    
    # define labels and title
    plt.xlabel('Hour')
    plt.ylabel('City')
    plt.title('Hourly Distribution of Orders per Location')
    
    # save the image
    # save image
    plt.savefig('./images/eda/5.location_analysis/Hourly Distribution of Orders per Location.png', bbox_inches='tight')
    
    plt.show()
    
    return


# function to plot the comparison between location and avg delivery cost
def location_vs_delivery_costs(orders_per_city,orders_per_city_del_cost):
    
    # create the time series plot
    fig, ax1 = plt.subplots(figsize=(20, 10), dpi=100, facecolor='white')
    
    # set distinct colors for "Orders" and "Delivery Cost"
    orders_color = 'blue'
    delivery_cost_color = 'red'
    
    # barplot
    ax1.bar(orders_per_city.index, orders_per_city['order_id'], \
            label='Orders', color=orders_color, alpha=0.7)
    ax1.set_xlabel('City')
    ax1.set_ylabel('Orders', color=orders_color)  # Set the label and color for the primary y-axis
    ax1.tick_params(axis='y', labelcolor=orders_color)  # Set the color of the y-axis ticks
    
    # create a secondary y-axis for lineplot
    ax2 = ax1.twinx()
    ax2.plot(orders_per_city_del_cost.index, orders_per_city_del_cost['delivery_cost'],\
            label='Avg Delivery Cost', color=delivery_cost_color, marker='o', linestyle='-', alpha=0.7, linewidth=2)
    
    ax2.set_ylabel('Avg Delivery Cost', color=delivery_cost_color)  # Set the label and color for the secondary y-axis
    ax2.tick_params(axis='y', labelcolor=delivery_cost_color)  # Set the color of the y-axis ticks
    
    #define title
    plt.title('Total Orders ~ Location vs Avg Delivery Cost')
    plt.legend().remove()
    
    # rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    
    # ensure all elements fit in the plot
    plt.tight_layout()
    
    # save the image
    plt.savefig('./images/eda/5.location_analysis/Total Orders ~ Location vs Avg Delivery Cost.png', bbox_inches='tight')
    
    plt.show()
    
    return

# 6. Promotions and Discounts


# function to plot and compare coupons vs discounts
def compare_coupons_with_discounts(orders_having_offer,orders_having_discount):
    
    # create figure
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 10), dpi=300,  facecolor='white')
    
    # plot order for offers
    orders_having_offer['order_id'].plot(kind='bar', ax=axes[0, 0], title='Orders vs Offers',color='royalblue')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].set_xticklabels(orders_having_offer.index, rotation=0)
    
    # plot users for offers
    orders_having_offer['user_id'].plot(kind='bar', ax=axes[0, 1], title='User vs Offers',color='peru')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].set_xticklabels(orders_having_offer.index, rotation=0)
    
    # plot revenue for offers
    orders_having_offer['revenue'].plot(kind='bar', ax=axes[0, 2], title='Revenue vs Offers',color='green')
    axes[0, 2].set_ylabel('Revenue')
    axes[0, 2].set_xticklabels(orders_having_offer.index, rotation=0)
    
    # plot order for discount
    orders_having_discount['order_id'].plot(kind='bar', ax=axes[1, 0], title='Orders vs Discount',color='royalblue')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].set_xticklabels(orders_having_discount.index, rotation=0)
    
    # plot users for discount
    orders_having_discount['user_id'].plot(kind='bar', ax=axes[1, 1], title='User vs Discount',color='peru')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].set_xticklabels(orders_having_discount.index, rotation=0)
    
    # plot revenue for sicount
    orders_having_discount['revenue'].plot(kind='bar', ax=axes[1, 2], title='Revenue vs Discount',color='green')
    axes[1, 2].set_ylabel('Revenue')
    axes[1, 2].set_xticklabels(orders_having_discount.index, rotation=0)
    
    # adjust spacing between subplots
    plt.tight_layout()
    
    # Save the image
    plt.savefig('./images/eda/6.promotions_and_discounts/Offers vs Discount.png', bbox_inches='tight')
    
    plt.show()
    
    return    


# 7.Revenue Analysis

# scatterplot to visualize monthly distribution of revenue
def monthly_distribution_of_revenue(revenue):
    
    # create a figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10), dpi=100,facecolor='white')
    
    # create scatterplot
    sns.scatterplot(x=revenue['revenue'][revenue.month=='August'],\
                         y=revenue['dayofmonth'][revenue.month=='August'],color='firebrick',ax=ax1)
    # define labels
    ax1.set_xlabel('Revenue')
    ax1.set_ylabel('Day of Month')
    # define title
    ax1.set_title('Revenue of August per Day of Month ~ August')
    
    # create scatterplot
    sns.scatterplot(x=revenue['revenue'][revenue.month=='September'],\
                         y=revenue['dayofmonth'][revenue.month=='September'],color='dimgrey',ax=ax2)
    # define labels
    ax2.set_xlabel('Revenue')
    ax2.set_ylabel('Day of Month')
    # define title
    ax2.set_title('Revenue of September per Day of Month ~ September')
    
    # save the image
    plt.savefig('./images/eda/7.revenue_analysis/Revenue per Day of Month  ~ August vs September.png', bbox_inches='tight')
    
    plt.show()
    
    return


# function to plot time series regarding revenue
def time_series_revenue(revenue_daily):
    
    # create the time series plot
    plt.figure(figsize=(10, 6), dpi=100, facecolor='white')
    plt.plot(revenue_daily.date, revenue_daily['revenue'], marker='o',color='green')
    
    # define parameters
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.title('Daily Revenue')
    
    # set grid
    plt.grid(True)
    
    # rotate x-axis labels for better readability
    plt.xticks(rotation=45)  
    
    # ensure all elements fit in the plot
    plt.tight_layout()  
    
    # save the image
    plt.savefig('./images/eda/7.revenue_analysis/Daily Revenue.png', bbox_inches='tight')
    
    plt.show()
    
    return


# weekly distribution of revenue
def weekly_heatmap_revenue(heatmap_data):
    
    # create the heatmap
    plt.figure(figsize=(15, 5), dpi=100, facecolor='white')
    sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="Greens")
    
    # define labels and title
    plt.xlabel('Day of the Week')
    plt.ylabel('Month')
    plt.title('Revenue Heatmap')
    
    # save the image
    plt.savefig('./images/eda/7.revenue_analysis/Weekly Revenue Heatmap.png', bbox_inches='tight')
    
    plt.show()
    
    return


# 8.Delivery Cost

# function to plot top 10 correlated variables with delivery cost
def top_10_related_to_delivery_cost(top_10_correlated_columns):
    
    # create a figure for the heatmap
    fig = plt.figure(figsize=(8, 6), dpi=100, facecolor='white')
    fig.patch.set_facecolor('white')
    
    # create a heatmap for the correlation of 'delivery_cost' with the top 10 columns
    sns.heatmap(top_10_correlated_columns, annot=True)
    
    # set the title
    plt.title('Top 10 Correlated Variables with Delivery Cost')
    
    # show the plot
    plt.show()
    
    return


# function to compare delivery cost with orders per class 
def delivery_cost_vs_orders_per_class(delivery_costs_classes):
    
    # create the time series plot
    fig, ax1 = plt.subplots(figsize=(15, 8), dpi=100, facecolor='white')
    
    # set distinct colors for "Orders" and "Delivery Cost"
    orders_color = 'blue'
    delivery_cost_color = 'red'
    
    # barplot
    ax1.bar(delivery_costs_classes.index, delivery_costs_classes['order_id'], \
            label='Orders', color=orders_color, alpha=0.7)
    ax1.set_xlabel('Classes')
    ax1.set_ylabel('Orders', color=orders_color)  
    ax1.tick_params(axis='y', labelcolor=orders_color)  
    
    # create a secondary y-axis for lineplot
    ax2 = ax1.twinx()
    ax2.plot(delivery_costs_classes.index, delivery_costs_classes['delivery_cost'],\
            label='Avg Delivery Cost', color=delivery_cost_color, marker='o', linestyle='-', alpha=0.7)
    
    ax2.set_ylabel('Avg Delivery Cost', color=delivery_cost_color)  
    ax2.tick_params(axis='y', labelcolor=delivery_cost_color)  
    
    # define title
    plt.title('Orders vs Avg Delivery Cost per Class')
    plt.legend().remove()
    
    # rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    
    # ensure all elements fit in the plot
    plt.tight_layout()
    
    # save the image
    plt.savefig('./images/eda/8.delivery_costs/Orders vs Avg Delivery Cost per Class.png', bbox_inches='tight')
    
    plt.show()
    
    return


# function to plot cuisine preferencies
def cuisine_preference_vs_revenue(cuisine):
    
    # create a figure
    fig,ax = plt.subplots(figsize=(15, 6), dpi=100, facecolor='white')
    
    # plot the second bar plot 
    x = np.arange(len(cuisine.index))
    ax.bar(x - 0.35/2, cuisine.total_orders, width=0.35, label='Orders',color='royalblue')
    ax.bar(x + 0.35/2, cuisine.total_users, width=0.35, label='Users',color='peru')
    
    # create a second set of axes to overlay the revenue data
    ax2 = ax.twinx()
    # plot the revenue data on the second set of axes
    ax2.plot(x, cuisine['avg_revenue'], color='green', marker='o', label='Avg Revenue')
    
    # define x labels for the second subplot
    ax.set_xticks(x)
    ax.set_xticklabels(cuisine.index)
    
    # define title and show the legend for both plots
    ax.set_title('Total Orders, Total Users and Avg Revenue per Cuisine')
    ax.set_xlabel('Cuisine')
    ax.set_ylabel('Count')
    ax2.set_ylabel('Avg Revenue')
    ax.legend(loc='upper left',bbox_to_anchor=(-0.01, 1.2))
    ax2.legend(loc='upper right',bbox_to_anchor=(0.15, 1.3))
    
    # save the image
    plt.savefig('./images/eda/9.vertical_and_cuisine_preferences/Total Orders, Total Users and Avg Revenue per Cuisine.png', \
                bbox_inches='tight')
    
    # preview
    plt.show()
    
    return


# heatmap to describe the hourly distribution of orders per cousine
def hourly_distribution_of_orders_per_cuisine(data_heatmap,hours,cuisines):
    
    # create the time series plot
    fig, ax1 = plt.subplots(figsize=(15, 8), dpi=100, facecolor='white')
    
    # Create a heatmap
    sns.heatmap(data_heatmap, cmap='YlGnBu', xticklabels=cuisines, yticklabels=hours)
    
    # Add labels and title
    plt.xlabel('Cuisine')
    plt.ylabel('Hour')
    plt.title('Hourly Distribution of Orders per Cuisine')
    
    # save the image
    plt.savefig('./images/eda/9.vertical_and_cuisine_preferences/Hourly Total Orders by Cuisine.png', bbox_inches='tight')
    
    # Show the plot
    plt.show()
    
    return