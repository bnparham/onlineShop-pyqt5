# Project summary

This project was one of the final projects of our Advanced Programming course at the [Guilan University](https://guilan.ac.ir/en/home "Guilan University"), which was instructed by [Prof. Sadegh Eskandari](https://staff.guilan.ac.ir/eskandari/?lg=1 "Prof. Sadegh Eskandari"), that I implemented one of them to pass the course.In this project, an online store simulator program is written using Python language with pyqt5 library.

# Program structure
![Program structure](https://i.postimg.cc/MHpFNtwx/Program-structure.png "Program structure")

The program is divided into 4 main sections, in the Datalayer section, it is tried to use the repository pattern and design a system like ORM to make it easier to use the queries used in the program.

In the program section, the modules used in the program have been placed.
Also, the executable file of the program . main.py is located in this section

The tools section contains the images used in the program as well as validations used throughout the program

The uiDesign section also contains executable files of the graphical environment that are made by pyqt5

## How to run Program
in program directory , open main.py file to excute program

------------






### Explanations about the program environment :




## Home Page
![home-page](https://i.postimg.cc/ZKtm3hp7/Home-Page.png")

## Login Page
![Login-Page](https://i.postimg.cc/nrVKrLps/Login-Page.png "Login-Page")

## sign-up Page
![signup-page](https://i.postimg.cc/yYMPXsTG/Signup-Page.png "signup-page")


------------


The user can log in to the program or register a new account.
This process is stored by sql in the database in the Data file of the DataLayer/context path
**The basic information to enter the program is included in the login file.**
Two types of users are defined for this program. Site admin and regular user who have their own access
## Home Page After Login in to Program


After logging in to the program, the user can view his account profile, shopping cart and list of favorite products.

![Home Page after Login](https://i.postimg.cc/TYMq5pzJ/Home-Page-login.png "Home Page after Login")


## User Profile section

In this section, the user can view his username, email, password, registration date, user ID, and account balance (amount in "Toman" currency in Iran).
Also, increasing the inventory (green button) and viewing the purchase invoice (blue button) and viewing comments registered by the user (orange button) are other features available in the user panel.

![userProfile](https://i.postimg.cc/52zhqYy9/user-Profile.png "userProfile")

## Shoping Cart

The products added to the shopping cart can be seen in this section as a table. After making the final decision, the user can buy these products or delete the products from his shopping cart
Product name, product code, discount code, selected number of products along with final price and price after discount can be seen in this table.

![Shopping Cart](https://i.postimg.cc/gJMcFXvF/Shoping-cart.png "Shopping Cart")


## Payment Section

To register the purchase, the user must enter his information including name and surname, residential address, contact number, etc

![Payment Section](https://i.postimg.cc/L697gQKT/payment-Section.png "Payment Section")


## User orders

After placing the order, the user can track the status of the order
(The green text means confirming the order and sending it, the red color means canceling the order by the seller, and the black color means that the user's order is being checked)

![userOrders](https://i.postimg.cc/hGc7Km7f/MyOrders.png "userOrders")


# Login to the program as an operator (site admin)
On the login page, you must click on the login as operator button to open the login page for operators (black button).

# Operator Page

The operator can view registered users in the store and target or edit their information, can register or cancel users' orders, edit products in the store, register new discount codes or edit or delete codes. also register or delete or edit the sellers of their products

![Operator Page](https://i.postimg.cc/26TM8gjg/Operator.png "Operator Page")
