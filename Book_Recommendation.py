'''
   CISC-121 2022W

   Name:   Raif Rizwan Karkal
   Student Number: 20261498
   Email:  20rrk2@queensu.ca

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
'''

# imports for use throughout the program
import tkinter as tk
from tkinter.filedialog import askdirectory
import glob


def Jaccard_Similarity (text_files_signature):
    """
    This function is responsible for calculating the Jaccard Similarity. This function
    takes in the text files signature which is a dictionary with list of top 25 common words
    of each book in the file book text. The function reads through each top 25 common words
    for each book which is its signature and than determines which two books are similar to each other
    through a set calculation of the signature. It than returns another new dictionary with the key representing
    a book and value representing a similar book.

    Parameters:  text files signature
    Return Value: similar book dict
     """

    # empty dictionary assigned to variable similar book dict
    similar_book_dict = {}

    # for loop in which variable keys assigned to each key in the dictionary text files signature
    for keys in text_files_signature.keys():
        # each value in the dictionary changed to become a set
        text_files_signature[keys] = set(text_files_signature[keys])

    # for loop in which variable keys assigned to each key in the dictionary text files signature
    for keys in text_files_signature.keys():
        # variable max assigned value 0
        max = 0

        # for loop in which variable keys_2 assigned to each key in the dictionary text files signature
        for keys_2 in text_files_signature.keys():
            # if statement in which if one dictionary value is not equal to the other dictionary values, program continues here
            if text_files_signature[keys] != text_files_signature[keys_2]:
                # union calculated for a dictionary value with other dictionary values
                union_set = text_files_signature[keys] | text_files_signature[keys_2]
                # intersection calculated for a dictionary value with other dictionary values
                intersection_set = text_files_signature[keys] & text_files_signature[keys_2]
                # jaccard similarity calculated by dividing the len of intersection set with len of union set
                jaccard_similarity_calc = len(intersection_set) / len(union_set)
                print(keys)
                print(jaccard_similarity_calc)
                print(keys_2)
                # if jaccard similarity calc is greater than max value, program continues here
                if jaccard_similarity_calc > max:
                    # max value changed to the jaccard similar calc value
                    max = jaccard_similarity_calc
                    # similar book dict added a new key which represents a book and new value which represents a similar book
                    similar_book_dict[keys] = keys_2

    # returning similar book dictionary
    return similar_book_dict


def text_signature (text_files, stop_word_list):
    """
    This function is responsible for determining the signature of each book in the file. The function
    determines the top 25 most common words in each book ignoring the words in the stop words list,
    this is the signature of each book. Once the signature is determined, it is placed into a dictionary
    which the key representing the book file address and value representing the top 25 words.

    Parameters:  text file, stop word list
    Return Value: text file signature
     """

    # word check variable assigned to empty string
    word_check = ""
    # word counter variable assigned to empty dictionary
    word_counter = {}
    # text files signature assigned to empty dictionary
    text_files_signature = {}
    # word frequencies assigned to empty list
    word_frequencies = []
    # top 25 words assigned to empty list
    top_25_words = []

    # for loop in which variable z assigned to values from range 0 to length of text_files
    for z in range(len(text_files)):
        # opening each text file in reading mode and assigning to the variable text open
        text_open = open(text_files[z], "r", encoding="UTF-8")
        # reading each text file and assigning the string of each text file to text read variable
        text_read = text_open.read()

        # for loop in which the variable word assigned to list of string of text read
        for word in text_read.split():
            # the string in variable word is lower cased
            word = word.lower()

            # for loop in which variable i assigned to each letter in variable word
            for i in word:
                # if i is an alphabet, program continues here
                if i.isalpha():
                    # word check string variable added string i
                    word_check += i

            # if word check is not in stop word list and the length of word check is greater than 0
            if word_check not in stop_word_list and len(word_check) > 0:
                # if word check is in word counter dictionary, program continues here
                if word_check in word_counter:
                    # within word counter dictionary the key - word check is increased by + 1
                    word_counter[word_check] += 1
                # else statement in which new key added to dictionary with value 1
                else:
                    word_counter[word_check] = 1

            # word check variable assigned empty string
            word_check = ""

        # for loop in which variable w c assigned to the iteration of wrd counter.items
        for w, c in iter(word_counter.items()):
            # word frequencies list appended with variable w and c
            word_frequencies.append((w, c))

        # word frequencies sorted using key lambda x:x[1] and reversed
        word_frequencies.sort(key=lambda x: x[1], reverse=True)
        # word frequencies top 25 variable assigned word frequencies values from 0 to 25
        word_frequencies_top_25 = word_frequencies[0:25]

        # for loop in which variable x assigned to each value from range 0 to length of word frequencies top 25
        for x in range(len(word_frequencies_top_25)):
            # top_25_word list appended with different values from word frequencies top 25[x][0]
            top_25_words.append(word_frequencies_top_25[x][0])

        # text files signature dictionary key created using text files [z] with different values of top 25 words
        text_files_signature[text_files[z]] = top_25_words

        # top 25 words variable assigned empty list
        top_25_words = []
        # word frequencies variable assigned empty list
        word_frequencies = []
        # word counter variable assigned empty dictionary
        word_counter = {}

    # return text files signature
    return text_files_signature


def User_Interface (similar_book_dict):
    """
    This function is responsible for displaying the user interface to the user.
    This function uses tkinter to display the different books with its similar
    counter part. It goes through the similar book dict which is a dictionary
    with each book and its similar counter part. It than displays it in an
    organized manner.

    Parameters:  similar book dict
    Return Value: None
     """

    # window variable assigned tk.Tk()
    window = tk.Tk()
    # the geometry of the window pop up is 1200 by 800
    window.geometry("1200x800")
    # the text displayed on top of column 0 is Books
    col_0_head = tk.Label(window, text=" Books ", pady=20)
    # grind created under column 0 with 0 rows
    col_0_head.grid(row=0, column=0)
    # the text displayed on top of column 1 is Similar Books
    col_1_head = tk.Label(window, text=" Similar Books ")
    # grind created under column 1 with 0 rows
    col_1_head.grid(row=0, column=1)

    # row variable assigned value 1
    row = 1
    # while loop which loops as long as row is under 26
    while row < 26:
        # for loop in which variable key and values assigned to each key and value in dictionary similar book dict
        for key, values in similar_book_dict.items():
            # displaying the key of the dictionary similar book dict in the column 0
            x = tk.Label(window, text=str(key))
            x.grid(row=row, column=0)

            # displaying the values of the dictionary similar book dict in the column 1
            y = tk.Label(window, text=str(values))
            y.grid(row=row, column=1)

            # increasing the value of row by + 1
            row +=1

    # looping the window
    window.mainloop()


def main ():
    """
    The main function controls the program flow. This is where execution will start. The main function
    creates the stop word list by reading through the stop word file and appending to the stop word
    list. It also calls the different functions for execution.

    Parameters: None
    Return Value: None
     """

    # stop word list variable assigned empty list
    stop_word_list = []
    # opening stop word.txt file in reading mode and assigning to the variable stop word file
    stop_word_file = open("StopWords.txt", "r", encoding = "UTF-8")

    # for loop in which variable i assigned to each word in stop word file
    for i in stop_word_file:
        # stop word list appended with i.strip
        stop_word_list.append(i.strip())

    data_dir = askdirectory(initialdir="/Users/raif/PycharmProjects/Assignment_3/Books Text")
    text_files = glob.glob(data_dir + "/" + "*.txt")

    # text signature function called with parameter text files and stop word list. Result returned assigned to variable text files signature
    text_files_signature = text_signature(text_files, stop_word_list)
    # Jaccard_Similarity function called with parameter text files signature. Result returned assigned to variable similar book dict
    similar_book_dict = Jaccard_Similarity(text_files_signature)
    # User Interface function called with parameter similar book dict.
    User_Interface(similar_book_dict)

# calling main function in order for the program to be executed
main()

