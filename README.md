# C$50 Exchange
#### Video demo: https://youtu.be/D_1OoNaUm8k
#### Description:
This is a simple currency exchange tool. Type the amount that you would like to convert in the first box, and then select which currency
you want to convert to. The tool will tell you how much the amount that you inputted is worth in the second currency. The data is updated
frequently using the free api from currencyexchangesapi.io.

#### Prerequisites:
The web application will need a web server to host the application and so it can be run. Heroku is a popular choice.

User will need to register with currencyexchangesapi.io in order to get an api key. The free plan includes 100 requests per month. The amount
of requests used can be checked on their website.
The key will need to be exported into the environment using the "export API_KEY=" command. Ensure that there are no spaces after the equal
sign.

### Usage:
The currency exchange tool can convert any number into another currency. It won't accept negative numbers or characters, and will
advise the user to input a number. Similarly, if currency 1 and currency 2 are the same currencies, then the application will
prompt the user to choose two different currencies. This is to ensure that the input is usable and the application can function successfully.

### Design choices:
One of the struggles was to not make the website look incredibly ugly. I used bootstrap in order to make a nice-looking navigation bar
and a nice-looking background. Jinja was used so that the website design could easily stay the same no matter where you are on the website.
I opted for simplicity in the website design, and focused on the utility of the tool. I think that websites can look ugly when it's overcrowded. The navigation bar was made more interesting using a linear fade. The button matches the navigation bar color. The background is a pleasant color and easy for reading the text.

Similarly, there are only two pages for the web application: a homepage (that includes the tool) and an about page. Keeping utility in mind,
this made the most sense. I thought to redirect the user to another page that displays the currency exchange result would be excessive.
I looked at other currency exchange websites for reference and they would similarly pop up the result instead of redirecting the user to a
new page. I also used a similar philosophy for creating error messages; there was no need for the user to be redirected. They could see their
error and then correct it.

I thought that a dropdown menu would be useful because sometimes the user might not remember the exact abbreviation for a currency and the
options could prompt their memory. Also, I allow any positive number to be entered, being flexible for the user's needs.

The about page just gives a short description with my name and my intention with the project. It gives the context of the project and furthermore, my desire to continue learning more programming to develop more projects in the future.


#### Built with:
Flask - Web framework
<br>
Jinja - Web templates
<br>
Bootstrap - Styling
<br>
Python - Application
