most_visited=df['client'].value_counts()[:n]
    top_n_visited_clients=pd.DataFrame({'client':most_visited.index, 'views':most_visited.values})
    plt.rcdefaults()
    fig, ax = plt.subplots()
    
  
    ax.barh(top_n_visited_clients['client'].tolist(), top_n_visited_clients['views'].tolist(), align='center')
    # ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('most visited clients')
    ax.set_title('What are the top n\'th visited clients?')
    plt.show()
    
    
    
    
 top_endpoints= logs_df['request'].value_counts()[:n]
    top_n_freq_endpoints = pd.DataFrame({'client':top_endpoints.index, 'frequent':top_endpoints.values})
    fig1, ax1 = plt.subplots()
    ax1.pie(top_n_freq_endpoints['frequent'].tolist(), labels=top_n_freq_endpoints['client'].tolist(), autopct='%1.1f%%',
        startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    
    
logs_df['request'] = logs_df['request'].str.replace(r"['?'].*['.']", '.',regex=True)
    #print(logs_df['request'])
    number_of_all_images = logs_df['request'].str.count(r"(/image)").sum()
    number_of_corect_formatted_images = logs_df['request'].str.count(r"(/image).*(jpg)").sum()
    number_of_corect_formatted_images = number_of_corect_formatted_images+logs_df['request'].str.count(r"(/image).*(jpeg)").sum()
    number_of_corect_formatted_images = number_of_corect_formatted_images+logs_df['request'].str.count(r"(/image).*(png)").sum()
    number_of_corect_formatted_images = number_of_corect_formatted_images+logs_df['request'].str.count(r"(/image).*(webp)").sum()
    real_img_percentage=number_of_corect_formatted_images / number_of_all_images
    print(number_of_all_images)
    print(number_of_corect_formatted_images)
    print(real_img_percentage)
    
    
status_codes = logs_df['status'].value_counts()[:]
    frequencies_of_status_code=pd.DataFrame({'status_code':status_codes.index, 'frequency':status_codes.values})
    status_codes_list=frequencies_of_status_code['status_code'].tolist()
    
    plt.bar(frequencies_of_status_code['status_code'].tolist(),frequencies_of_status_code['frequency'].tolist(),width=10)
    plt.ylabel('Frequency')
    plt.xlabel('Status codes')
    plt.title('Status codes frequencies')
    #plt.xticks(np.arange(min(list(status_codes_frequencies['frequency'])), max(list(status_codes_frequencies['frequency']))+1, 10))
    plt.show()
    print(frequencies_of_status_code)
    
    
    
status_and_datetimes = logs_df[{"datetime","status"}]
    status_and_datetimes["datetime"] = pd.to_datetime(status_and_datetimes['datetime']).dt.hour
    errors_freq_df.columns.name = 'hour'
    
    errors_freq_df['4xx'] = status_and_datetimes['status'].transform(lambda x:x//100 ==4).groupby(status_and_datetimes["datetime"]).agg('sum')
    errors_freq_df['5xx'] = status_and_datetimes['status'].transform(lambda x:x//100 ==5).groupby(status_and_datetimes["datetime"]).agg('sum')
    #errors_freq_df.index.names = ['hour']
    errors_freq_df.index.name = None
    display(errors_freq_df)
    
    
    
all_groups=logs_df.groupby(['client' , 'user_agent'] , observed=True)
    all_groups_df=all_groups.head(50)
    user_agent_details_df['Browser family']=all_groups_df['user_agent'].apply(lambda x:parse(x).browser.family)
    user_agent_details_df['OS family']=all_groups_df['user_agent'].apply(lambda x:parse(x).os.family)
    user_agent_details_df['Is_bot']=all_groups_df['user_agent'].apply(lambda x:parse(x).is_bot)
    user_agent_details_df['Is_pc']=all_groups_df['user_agent'].apply(lambda x:parse(x).is_pc)
    display(user_agent_details_df)
    
    
rows_length=sample_df.shape[0]
    number_of_rows_with_size_zero= sample_df[sample_df['size'] == 0].shape[0]
    percentage=number_of_rows_with_size_zero/rows_length
    print(rows_length)
    print(number_of_rows_with_size_zero)
    print(percentage)
    #print(sample_df[sample_df['size'] == 0]['request'])
    sample_df.hist(bins=n_bins, column='size')