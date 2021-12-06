from tkinter import *
import tkinter as tk

from os import getcwd
from os.path import join
from time import sleep
from time import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from requests import get

answers_given = []

class MyCommands(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Location, Cuisine, Rating, EndPage, Results):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Welcome to your Baltimore Restaurant Guide!")
        label.pack(pady=10, padx=10)
        label = tk.Label(
            self, text="Find the restaurant that best caters your cravings!")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Let's Start!",
                           command=lambda: controller.show_frame(Location))
        button.pack()

class Location(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Question 1: Which JHU campus are you closest to?")
        label.pack(pady=10, padx=10)
        btn_homewood = Button(self, text='Homewood', bd='5',
                              command=lambda: [controller.show_frame(Cuisine),
                                               self.btn_homewood_press()])
        btn_homewood.pack(pady=10, padx=10)
        btn_peabody = Button(self, text='Peabody', bd='5',
                             command=lambda: [controller.show_frame(Cuisine),
                                              self.btn_peabody_press()])
        btn_peabody.pack(pady=10, padx=10)
        btn_med = Button(self, text='Medical', bd='5',
                         command=lambda: [controller.show_frame(Cuisine),
                                          self.btn_med_press()])
        btn_med.pack(pady=10, padx=10)
        btn_exit = Button(self, text='Exit', bd='5',
                          command=self.quit)
        btn_exit.pack(pady=10, padx=10)

    def btn_homewood_press(self):
        answers_given.append("Homewood")
        print(answers_given)

    def btn_peabody_press(self):
        answers_given.append("Peabody")
        print(answers_given)

    def btn_med_press(self):
        answers_given.append("Medical")
        print(answers_given)


class Cuisine(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Question 2: Which regional cousine would you like?")
        label.pack(pady=10, padx=10)
        btn_murica = Button(self, text='American', bd='5',
                            command=lambda: [controller.show_frame(Rating),
                                             self.btn_murica_press()])
        btn_murica.pack(pady=10, padx=10)
        btn_mex = Button(self, text='Mexican', bd='5',
                         command=lambda: [controller.show_frame(Rating),
                                          self.btn_mex_press()])
        btn_mex.pack(pady=10, padx=10)
        btn_ind = Button(self, text='Indian', bd='5',
                         command=lambda: [controller.show_frame(Rating),
                                          self.btn_ind_press()])
        btn_ind.pack(pady=10, padx=10)
        btn_chn = Button(self, text='Chinese', bd='5',
                         command=lambda: [controller.show_frame(Rating),
                                          self.btn_chn_press()])
        btn_chn.pack(pady=10, padx=10)
        btn_exit = Button(self, text='Exit', bd='5',
                          command=self.quit)
        btn_exit.pack(pady=10, padx=10)
        btn_reset = Button(self, text='Reset', bd='5',
                           command=lambda: [controller.show_frame(StartPage),
                                            answers_given.clear()])
        btn_reset.pack(pady=10, padx=10)

    def btn_murica_press(self):
        answers_given.append("American")
        print(answers_given)

    def btn_mex_press(self):
        answers_given.append("Mexican")
        print(answers_given)

    def btn_ind_press(self):
        answers_given.append("Indian")
        print(answers_given)

    def btn_chn_press(self):
        answers_given.append("Chinese")
        print(answers_given)

class Rating(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label_error = tk.Label(self, text="Please enter a valid value.")
        label = tk.Label(
            self, text="Question 3: What is the minimum Google reviews "
            "rating of your desired restaurant?")
        label.pack(pady=10, padx=10)
        label = tk.Label(
            self, text="Please enter a value equal to or less than 5. "
            "Decimal points accepted.")
        label.pack(pady=10, padx=10)
        rating_input = tk.Text(self, height=1, width=5)
        rating_input.pack()
        btn_rating_enter = Button(
            self, text='Enter', bd='5',
            command=lambda: [self.label_error.pack_forget(),
                             self.btn_enter_press(rating_input)])
        btn_rating_enter.pack()
        btn_exit = Button(self, text='Exit', bd='5',
                          command=self.quit)
        btn_exit.pack(pady=10, padx=10)
        btn_reset = Button(self, text='Reset', bd='5', command=lambda:
                           [self.controller.show_frame(StartPage),
                            answers_given.clear()])
        btn_reset.pack(pady=10, padx=10)

    def btn_enter_press(self, rating_input):
        rating_answer = rating_input.get(1.0, "end")
        rating_answer = rating_answer.strip('\n')
        try:
            rating_answer = float(rating_answer)
        except ValueError:
            self.label_error.pack(pady=10, padx=10)
            rating_input.delete(1.0, "end")
        else:
            if rating_answer <= 5:
                answers_given.append(rating_answer)
                print(answers_given)
                self.controller.show_frame(EndPage)
                rating_input.delete(1.0, "end")
            else:
                self.label_error.pack(pady=10, padx=10)
                rating_input.delete(1.0, "end")


class EndPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Thank you for answering the questions. "
            "Click below to submit.")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="I'm done! Get me my results!",
                           command=lambda: controller.show_frame(Results))
        button.pack(pady=10, padx=10)


class Results(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="See your results below:")
        label.pack(pady=10, padx=10)
        btn_exit = Button(self, text='Exit', bd='5',
                          command=self.quit)
        btn_exit.pack(pady=10, padx=10)
        
        
def webscrape(answers):
    '''
    This function returns the restaurants that are found on Google
    based on the user's selection.
    input: location and preferred food category *list*
    output: restaurant names *list*
    '''

    # search on Google
    url = "https://www.google.com/"
    driver_path = join(getcwd(), 'chromedriver')  # get chrome driver
    driver = Chrome(driver_path)
    driver.get(url)

    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.NAME, 'q')))

    # enter the key words in search bar
    search = 'jhu homewood restaurant' + ' ' + str(answers[0]) + ' ' + str(answers[1])
    loc_search_box = driver.find_element_by_name('q')
    loc_search_box.send_keys(search)
    loc_search_box.send_keys(Keys.ENTER)

    sleep(3)

    # click "more" from google results
    wait.until(EC.element_to_be_clickable((
        By.CLASS_NAME, 'MXl0lf.tKtwEb.wHYlTd')))
    loc_more = driver.find_element_by_class_name('MXl0lf.tKtwEb.wHYlTd')
    loc_more.click()

    sleep(3)

    # get the restaurant names
    wait.until(EC.element_to_be_clickable((
        By.CLASS_NAME, 'dbg0pd.OSrXXb.eDIkBe')))
    names = driver.find_elements_by_class_name('dbg0pd.OSrXXb.eDIkBe')
    restaurants = []
    for elem in names:
        # convert WebElement to text and append to list
        restaurants.append((elem.text))

    return restaurants


if __name__ == '__main__':
    app = MyCommands()
    app.mainloop()
    print(webscrape(ans))
