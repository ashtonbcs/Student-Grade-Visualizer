import pandas as pd
import matplotlib.pyplot as plt
print("Hello a CSV file of 20 random generated students and they're grades have been loaded")
# Initialize the menu.
# Press q or Q at anytime to end the program
class Menu:
    def __init__(self):
        try:
            print("Grade Visualizer!")
            print('1. Display Grades')
            print('2. Filter Data')
            print('3. Visualize Data')
            print('4. Exit')
            self.choice = input('Enter your choice: ').strip()

            if self.choice not in {'1', '2', '3', '4', 'q', 'Q'}:
                raise ValueError

            if self.choice == 'q' or self.choice == 'Q':
                print("Goodbye!")
                exit()

        except ValueError:
            print("Invalid input. Try again.")
            self.choice = input('Enter your choice: ').strip()
class Data:
    def __init__(self):
      global df
      df = pd.read_csv('Student_grades_corrected.csv')

    # The user can display the grades outright without filtering
    def gradedislpay(self):
        print(df)

    # Allow the user to choose between a numerous amount of ways to filter the data
    def filterdata(self):
        try:
            filter = input('How would you like to filter your data? Ex. all, mean, std, by topic, min, etc. ').lower()
            if filter not in {'all', 'mean', 'std', 'min', 'max', 'functions','limits','trigonometry','q','Q'}:
                raise ValueError
            if filter == 'q' or filter == 'Q':
                print('Goodbye!')
                exit()

            if filter == 'all':
                print(df.describe())
            # Sort the data by the chosen topic in ascending order
            elif 'grade' in filter:
                sorted_df = df.sort_values(by='Grade', ascending=False)
                print(sorted_df[['Name', 'Grade']])

            elif 'functions' in filter:
                sorted_df = df.sort_values(by=['Functions'], ascending=False)
                print(sorted_df[['Name', 'Functions']])

            elif 'limits' in filter:
                sorted_df = df.sort_values(by=['Limits'], ascending=False)
                print(sorted_df[['Name', 'Limits']])

            elif 'mean' in filter:
                topic = input('would you like the mean for grades of the whole dataset? If so press enter! If not please specify the topic: ').lower().strip()
                if topic == 'q' or filter == 'Q':
                    print('Goodbye!')
                    exit()
                elif topic == "":
                    df['AverageScores'] = df[['Functions','Trigonometry','Limits']].mean(axis=1)
                    print(df[['Name','AverageScores']])
                    print('\nAverage Scores for each student across the three topics')
                elif 'grade' in topic:
                    print(df[['Name', 'Grades']])
                    print('\nClass mean (Grades):', df['Grades'].mean())
                elif 'function' in topic:
                    print(df[['Name', 'Functions']])
                    print('\nclass mean (Functions):', df['Functions'].mean())
                elif 'trig' in topic:
                    print(df[['Name', 'Trigonometry']])
                    print('\nclass mean (Trigonometry):', df['Trigonometry'].mean())
                elif 'limits' in topic:
                    print(df[['Name', 'Limits']])
                    print('\nclass mean (Limits):', df['Limits'].mean())


            elif filter == 'std':
                topic = input('Would you like the std for grades of the overall dataset? If so press enter! if not please specify the topic: ').lower().strip()
                if topic == 'q' or filter == 'Q':
                    print('Goodbye!')
                    exit()
                elif topic == '':
                    df['Std'] = df[['Functions','Trigonometry','Limits']].std(axis=1)
                    print(df[['Name','Std']])
                    print('\nStandard Deviation for each student across the three topics')
                elif 'grade' in topic:
                    print(df[['Name', 'Grades']])
                    print('\nclass std (Grades):', df['Grades'].std())
                elif 'function' in topic:
                    print(df[['Name', 'Functions']])
                    print('\nclass std (Functions):', df['Functions'].std())
                elif 'trig' in topic:
                    print(df[['Name', 'Trigonometry']])
                    print('\nclass std (Trigonometry):', df['Trigonometry'].std())
                elif 'limits' in topic:
                    print(df[['Name', 'Limits']])
                    print('\nclass std (Limits):', df['Limits'].std())


            elif 'min' in filter:
                topic = input('Would you like the minimum of the grade of the whole data set? if so press enter! if not please specify the topic: ').lower().strip()
                if topic == 'q' or filter == 'Q':
                    print('Goodbye!')
                    exit()
                elif topic == '':
                    print(df.loc[df['Grade'].idxmin()])
                elif 'limit' in topic:
                    print(df.loc[df['Limits'].idxmin()])
                elif 'function' in topic:
                    print(df.loc[df['Functions'].idxmin()])
                elif 'trigonometry' in topic:
                    print(df.loc[df['Trigonometry'].idxmin()])


            elif 'max' in filter:
                topic = input('Would you like the maximum of the grade of the whole data set? if so press enter! if not please specify the topic: ').lower().strip()
                if topic == 'q' or filter == 'Q':
                    print('Goodbye!')
                    exit()
                if topic == '':
                    print(df.loc[df['Grade'].idxmax()])
                elif 'limit' in topic:
                    print(df.loc[df['Limits'].idxmax()])
                elif 'function' in topic:
                    print(df.loc[df['Functions'].idxmax()])
                elif 'trigonometry' in topic:
                    print(df.loc[df['Trigonometry'].idxmax()])



        except ValueError:
            print('Invalid input. Please try again.')
            print('Please choose from the following: \nmin, max, mean, std, functions, limits, trigonometry.')


    def vizualization(self):
        try:
            choice = input('What would you like shown? (Grades, Functions, Limits, Trigonometry) ').lower().strip()
            if choice not in {'grades', 'functions', 'limits', 'trigonometry', 'q', 'Q'}:
                raise ValueError

            elif choice == 'q' or choice == 'Q':
                print('Goodbye!')
                exit()

            choice2 = input('How would you like to visualize the data? (Scatter plot, bar chart, stem plot) ').lower().strip()
            if choice2 not in {'bar chart', 'scatter plot', 'stem plot', 'q', 'Q'}:
                raise LookupError

            elif choice == 'grades':
                if choice2 == 'q' or choice2 == 'Q':
                    print('Goodbye!')
                    exit()
                elif choice2 == 'bar chart':
                    plt.figure(figsize=(14,10))
                    plt.bar(df['Name'], df['Grade'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Grade')
                    plt.title('Final Grade For Each Student', fontsize=20)
                    plt.show()
                elif choice2 == 'scatter plot':
                    plt.figure(figsize=(14,10))
                    plt.scatter(df['Name'], df['Grade'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Grade')
                    plt.title('Final Grade For Each Student', fontsize=20)
                    plt.show()
                elif choice2 == 'stem plot':
                    plt.figure(figsize=(14,10))
                    plt.stem(df['Name'], df['Grade'])
                    plt.xticks(rotation=75)
                    plt.title('Final Grade For Each Student', fontsize=20)
                    plt.show()


            elif choice == 'limits':
                if choice2 == 'q' or choice2 == 'Q':
                    print('Goodbye!')
                    exit()
                elif choice2 == 'bar chart':
                    plt.figure(figsize=(14,10))
                    plt.bar(df['Name'], df['Limits'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Limits')
                    plt.title('Final Limits Grade For Each Student', fontsize=20)
                    plt.show()
                elif choice2 == 'scatter plot':
                    plt.figure(figsize=(14,10))
                    plt.scatter(df['Name'], df['Limits'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Limits')
                    plt.title('Final Limits Grade For Each Student', fontsize=20)
                    plt.show()
                elif choice2 == 'stem plot':
                    plt.figure(figsize=(14,10))
                    plt.stem(df['Name'], df['Limits'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Limits')
                    plt.title('Final Limits Grade For Each Student', fontsize=20)
                    plt.show()


            elif choice == 'trigonometry':
                if choice2 == 'q' or choice2 == 'Q':
                    print('Goodbye!')
                    exit()
                elif choice2 == 'bar chart':
                    plt.figure(figsize=(14,10))
                    plt.bar(df['Name'], df['Trigonometry'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Trigonometry Grade')
                    plt.title('Final Trigonometry Grade For Each Student', fontsize=20)
                    plt.show()
                elif choice2 == 'scatter plot':
                    plt.figure(figsize=(14,10))
                    plt.scatter(df['Name'], df['Trigonometry'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Trigonometry Grade')
                    plt.title('Final Trigonometry Grade For Each Student', fontsize=20)
                    plt.show()
                elif choice2 == 'stem plot':
                    plt.figure(figsize=(14,10))
                    plt.scatter(df['Name'], df['Trigonometry'])
                    plt.scatter(df['Name'], df['Trigonometry'])
                    plt.xticks(rotation=75)
                    plt.ylabel('Final Trigonometry Grade')
                    plt.title('Final Trigonometry Grade For Each Student', fontsize=20)
                    plt.show()



        except ValueError:
            print('Invalid input. Please try again.')
            print('Please choose from the following: \nGrades, Functions, Limits, Trigonometry.')
        except LookupError:
            print('Invalid input. Please try again.')
            print('Please choose from the following: \nBar Chart, Scatter Plot, Stem Plot')




menu = Menu()
data = Data()
while menu.choice != '4':
    if menu.choice == '1':
        data.gradedislpay()
        menu = Menu()
    elif menu.choice == '2':
        data.filterdata()
        menu = Menu()
    elif menu.choice == '3':
        data.vizualization()
        menu = Menu()
else:
    print('Goodbye!')
