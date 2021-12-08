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

        for F in (StartPage, Location, EnterAddress,
                  Cuisine, Rating, EndPage, Results):

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
        btn_none = Button(self, text='None! I want to enter an address.',
                          bd='5', command=lambda:
                          controller.show_frame(EnterAddress))
        btn_none.pack(pady=10, padx=10)
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


class EnterAddress(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please enter a "
                         " valid address/location/area name, "
                         "similar to how you would in Google.", bd='5')
        label.pack(pady=10, padx=10)
        address_input = tk.Text(self, height=2, width=20)
        address_input.pack(pady=10, padx=10)
        btn_address_enter = Button(self, text="Enter", bd='5',
                                   command=lambda:
                                   [self.btn_add_press(address_input),
                                    controller.show_frame(Cuisine)])
        btn_address_enter.pack(pady=10, padx=10)

    def btn_add_press(self, address_input):
        address_answer = address_input.get(1.0, "end")
        address_answer = address_answer.strip('\n')
        answers_given.append(address_answer)


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
                           command=lambda: [controller.show_frame(Results),
                                            self.webscrape(answers_given)])
        button.pack(pady=10, padx=10)

    def webscrape(self, answers_given):
        '''
        This function will open Chrome and search on Google Maps
        to find nearby restaurants.
        **Parameters**
            answers_given: *list
                First str: the location to search for nearby restaurants
                Second str: the type of cuision you prefer
                Third str: the minimum value of rating the restaurant
                needs to have
        **Returns**
            restaurants: *list
                A list of all the restaurants found
            ratings: *list
                A list of the ratings for each restaurant
            links: *list
                A list of the hyperlinks of each restaurant
        '''

        # open Google Maps with Chrome driver
        url = 'https://maps.google.com/'
        # we are getting the chrome driver here
        # make sure the chrome driver is in the same folder as this code
        # and is named as "chromedriver"
        driver_path = join(getcwd(), 'chromedriver')
        driver = Chrome(driver_path)
        # open the Google Maps page
        driver.get(url)

        # Timeout Exception if search bar not clickable in 15 seconds
        wait = WebDriverWait(driver, 15)
        # the search bar name is 'q'
        # waiting until the search bar is clickable
        wait.until(EC.element_to_be_clickable((By.NAME, 'q')))

        if answers_given[0] == 'Homewood':
            address = '3400 North Charles Street, Baltimore, MD 21218'

        elif answers_given[0] == 'Peabody':
            address = '1 E Mt Vernon Pl, Baltimore, MD 21202'

        elif answers_given[0] == 'Medical':
            address = '733 N Broadway, Baltimore, MD 21205'

        else:
            address = answers_given[0]

        # locating the search bar
        loc_search_box = driver.find_element_by_name('q')
        # enter the keywords in search bar
        loc_search_box.send_keys(address)
        # click the search button
        loc_search_box.send_keys(Keys.ENTER)

        # sleep to mimic human activity
        sleep(3)

        # click "restaurants" from Google results
        wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'uEubGf.gm2-subtitle-alt-2')))
        restaurant = driver.find_element_by_class_name(
            'uEubGf.gm2-subtitle-alt-2')
        restaurant.click()

        # type cuisine type into Google search
        wait.until(EC.element_to_be_clickable((By.NAME, 'q')))
        box = driver.find_element_by_name('q')
        box.click()

        # enter the keywords (user's input cuisine type) in search bar
        box.send_keys(' ' + answers_given[1])
        box.send_keys(Keys.ENTER)

        # wait until elements are clickable to fetch the restaurant names
        wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'qBF1Pd.gm2-subtitle-alt-1')))
        sleep(3)
        res = driver.find_elements_by_class_name('qBF1Pd.gm2-subtitle-alt-1')
        rating = driver.find_elements_by_class_name('ZkP5Je')
        link = driver.find_elements_by_class_name(
            'a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')

        # get the restaurant names
        # convert WebElement to str and append to list
        restaurants = [(elem.text) for elem in res]

        # get the restaurant ratings
        # convert WebElement to str and append to list
        # stripping away the number of ratings
        # take the rating digits only
        ratings = [(elem.text)[:3] for elem in rating]

        # get the hyperlinks
        links = [elem.get_attribute('href') for elem in link]

        # discard restaurants below a certain rating
        index = [i for i, v in enumerate(
            ratings) if float(v) < float(answers_given[2])]

        # delete the unwanted elements for all three lists
        # need to reverse it so the rest of the indecies
        # we refer to will remain the same
        for elem in sorted(index, reverse=True):
            del restaurants[elem]
            del ratings[elem]
            del links[elem]

        # close Chrome
        driver.close()

        return restaurants, ratings, links


class Results(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="See your results below:")
        label.pack(pady=10, padx=10)
        btn_exit = Button(self, text='Exit', bd='5',
                          command=self.quit)
        btn_exit.pack(pady=10, padx=10)


if __name__ == '__main__':
    app = MyCommands()
    app.mainloop()
    print(self.webscrape(answers_given))

