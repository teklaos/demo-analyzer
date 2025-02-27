import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    # Amount of each race represented in the dataset
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = df.loc[df['sex'] == 'Male']['age'].mean()

    # Percentage of people who have a Bachelor's degree
    percentage_bachelors = df.loc[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100

    # People with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[
        (df['education'] == 'Bachelors') |
        (df['education'] == 'Masters') |
        (df['education'] == 'Doctorate')
    ]
    lower_education = df.loc[
        (df['education'] != 'Bachelors') &
        (df['education'] != 'Masters') &
        (df['education'] != 'Doctorate')
    ]

    # Percentage with salary >50K
    higher_education_rich = higher_education.loc[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] * 100
    lower_education_rich = lower_education.loc[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100

    # Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of the people who work the minimum number of hours per week
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    # Percentage with salary >50K
    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100

    # Country with the highest percentage of people that earn >50K
    highest_earning_country = (df.loc[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df.loc[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100).max()

    # The most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
