from tkinter import *
import tkinter as tk

from os import getcwd
from os.path import join
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answers_given = []


class MyCommands(tk.Tk):
    '''
    This class stores and loads the pages for the tkinter program.
    '''

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Location, EnterAddress,
                  Cuisine, Rating, EndPage, Results, LinkRedirect):
            # looping thru diff. classes, stored pages of program

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        # Call this function when we want to switch between pages

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    '''
    This is the class corresponding to the first page of the program.
    It displays a single button that, when clicked, uses show_frame function
    to take the user to the Location page for the first question.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''

        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Welcome to your Restaurant Guide ~")
        label.pack(pady=10, padx=10)
        label = tk.Label(
            self, text="Find restaurants that cater to your cravings...")
        label.pack(pady=10, padx=10)
        label = tk.Label(
            self, text="within or outside the Baltimore area!")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Let's Start!",
                           command=lambda: controller.show_frame(Location))
        button.pack()


class Location(tk.Frame):

    '''
    This is the class corresponding to the second page of the program.
    It asks the first question to the user. Displayed are 4 options for answers
    and an exit button that closes out of the program w/o running any search.
    Clicking the first three options leads to the Cuisine page.
    Clicking the fourth option leads to a new page with a text box,
    where user is prompted to enter in their desired address (EnterAddress).
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''

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

    '''
    The following functions are called when user clicks the first 3 options.
    They save the answer into the array "answers_given".
    '''

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

    '''
    This is the class corresponding to the third page of the program.
    It asks the second question and displays 4 answer buttons
    as well as the exit button.
    An additional button here is the reset button,
    which takes user back to StartPage.
    All answers entered by the user are erased from the system
    and the program starts from
    scratch when the reset button is clicked.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''

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

    '''
    The following functions are called when user clicks the first 3 options.
    They save the answer into the array "answers_given".
    '''

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

    '''
    This class corresponds with an alternative page of the program.
    It is only called when the user (in question 1) answers that they want
    to enter in an address.
    The user types in an address and clicks the enter button,
    which initiates the btn_add_press function.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please enter a "
                         "valid address/location/area name, "
                         "similar to how you would in Google.", bd='5')
        label.pack(pady=10, padx=10)
        address_input = tk.Text(self, height=2, width=20)
        address_input.pack(pady=10, padx=10)
        btn_address_enter = Button(self, text="Enter", bd='5',
                                   command=lambda:
                                   [self.btn_add_press(address_input),
                                    controller.show_frame(Cuisine)])
        btn_address_enter.pack(pady=10, padx=10)

    '''
    This function saves the text entered by user into
    "answers_given" in the correct format.
    '''

    def btn_add_press(self, address_input):
        address_answer = address_input.get(1.0, "end")
        address_answer = address_answer.strip('\n')
        answers_given.append(address_answer)


class Rating(tk.Frame):

    '''
    This is the class corresponding to the fourth page of the program.
    This class asks the third (final) question & presents user with a text box
    to enter in their rating.
    The user is also presented with the same exit and reset buttons as before.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label_error = tk.Label(self, text="Please enter a valid value.")
        # The above (label_error) should be displayed ONLY when user enters:
        # not a number (letters/punctuation/etc.) or leaves the textbox blank.
        # We don't pack label_error so that it doesn't appear until
        # the user makes that mistake.
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
        # The command to pack_forget the label_error is so that error doesn't
        # keep displaying a ton of them one below the other
        # each time user enters something invalid.
        btn_rating_enter.pack()
        btn_exit = Button(self, text='Exit', bd='5',
                          command=self.quit)
        btn_exit.pack(pady=10, padx=10)
        btn_reset = Button(self, text='Reset', bd='5', command=lambda:
                           [self.controller.show_frame(StartPage),
                            answers_given.clear()])
        btn_reset.pack(pady=10, padx=10)

    '''
    This function checks what user entered into textbox to see if it's valid.
    If not, it displays error message.
    '''

    def btn_enter_press(self, rating_input):
        rating_answer = rating_input.get(1.0, "end")
        rating_answer = rating_answer.strip('\n')
        try:
            rating_answer = float(rating_answer)
            # This checks to make sure that the text entered is a value.
        except ValueError:
            # If it's not a value, then the program gets the ValueError error.
            # To prevent the program from crashing and let user
            # know their mistake,
            # the program displays (ie. pack) the label_error.
            self.label_error.pack(pady=10, padx=10)
            rating_input.delete(1.0, "end")
            # This line deletes whatever text the user entered into textbox.
        else:
            if rating_answer <= 5:
                # if the answer is a number and below/equal to 5,
                # then we save the answer into "answers_given".
                answers_given.append(rating_answer)
                print(answers_given)
                self.controller.show_frame(EndPage)
                rating_input.delete(1.0, "end")
            else:
                self.label_error.pack(pady=10, padx=10)
                rating_input.delete(1.0, "end")
                # again, if it is not valid,
                # we clear the textbox and display error message.


class EndPage(tk.Frame):

    '''
    This is the class corresponding to the last page of the program.
    It lets the user know that the questions are done and prompts them to
    click a button to submit answers and run the search.
    The page that the user is taken to when clicking the button is Results page
    # and that's where the answers are displayed.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''
        tk.Frame.__init__(self, parent)
        self.controller = controller
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
            A GUI with buttons of restaurant names and their ratings (in texts)
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
        loc_search_box = driver.find_element(By.NAME, 'q')
        # enter the keywords in search bar
        loc_search_box.send_keys(address)
        # click the search button
        loc_search_box.send_keys(Keys.ENTER)

        # sleep to mimic human activity
        sleep(3)

        # click "restaurants" from Google results
        wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'uEubGf.gm2-subtitle-alt-2')))
        restaurant = driver.find_element(By.CLASS_NAME,
                                         'uEubGf.gm2-subtitle-alt-2')
        restaurant.click()

        # type cuisine type into Google search
        wait.until(EC.element_to_be_clickable((By.NAME, 'q')))
        box = driver.find_element(By.NAME, 'q')
        box.click()

        # enter the keywords (user's input cuisine type) in search bar
        box.send_keys(' ' + answers_given[1])
        box.send_keys(Keys.ENTER)

        # wait until elements are clickable to fetch the restaurant names
        wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'qBF1Pd.gm2-subtitle-alt-1')))
        sleep(3)
        res = driver.find_elements(By.CLASS_NAME, 'qBF1Pd.gm2-subtitle-alt-1')
        rating = driver.find_elements(By.CLASS_NAME, 'ZkP5Je')
        link = driver.find_elements(By.CLASS_NAME,
                                    'a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
        trial = driver.find_elements(By.CLASS_NAME,
                                     'V0h1Ob-haAclf.OPZbO-KE6vqe.o0s21d-HiaYvf'
                                     )

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

        # get the texts to check if it contains 'No review'
        # because the list would miss an element and it would
        # throw off an IndexError
        texts = [elem.text for elem in trial]

        # looping to see if 'No reviews is in'
        result = []
        for term in texts:
            ans = term.find('No reviews')
            result.append(ans)

        # get the index of the place with 'No reviews'
        index = [i for i, val in enumerate(result) if val > -1]

        # put 0.0 for the rating for the ones that does not have a review
        for ind in index:
            ratings.insert(ind, '0.0')

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

        for i in range(len(restaurants)):
            btn = tk.Button(
                app, text=restaurants[i])
            btn.config(
                command=lambda t=restaurants[i],
                l=links[i]: self.select_restaurant(l))
            btn.pack()
            label = tk.Label(app, text="Rating: " + ratings[i])
            label.pack()

    def select_restaurant(self, links):
        self.controller.frames[LinkRedirect].change_label_text(links)
        self.controller.show_frame(LinkRedirect)


class LinkRedirect(tk.Frame):

    '''
    This class will display the link for the restaurant website.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''

        tk.Frame.__init__(self, parent)
        self.links = tk.Label(self, text='')
        self.links.pack()

    def change_label_text(self, links):
        '''
        This function will display the link to the restaurant website.
        ** Inputs **
        self: current object
        links: text, link to the restaurant
        '''

        self.links.config(text=links)


class Results(tk.Frame):

    '''
    This is the class that corresponds to the Results page.
    This displays the restaurants that the program found that fit
    what the user entered in the questions.
    '''

    def __init__(self, parent, controller):
        '''
        ** Inputs **
        self: current object
        parent: widget, parent of the current object (self)
        controller: object that allows pages of widget
        to interact w/ one another.
            For example, show_frame is defined in separate class and controller
            allows us to access that class from other classes.
        '''
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Search Completed! "
                         "See your results below. "
                         "Click on each result to display restaurant link.")
        label.pack()
        btn_exit = tk.Button(self, text='Exit', bd='5',
                             command=self.quit)
        btn_exit.pack()


if __name__ == '__main__':
    app = MyCommands()
    app.mainloop()
