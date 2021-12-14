from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://deepi:deepi@cluster0.1msoo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["bakery"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    response = MessagingResponse()


    user = users.find_one({"number": number})
    if bool(user) == False:
        msg = response.message("*Hey*, Happy  to see you here 😃🎁")
        msg.media("https://drive.google.com/uc?id=17nojMBo7lW11HGnsrRRXF-wWkq4mlk7k")
        response.message("Hi, Thanks for contacting *Deepanshu.* \nWhat do you want to know about him""\n\n*Please choose one of the option below based on your interest:*\n1️⃣ *Family* \n2️⃣ *Hobbies* \n3️⃣ *Address* \n4️⃣ *Education* \n5️⃣ *Achievements* \n6️⃣ *Goals* \n7️⃣ *Some Favourites* \n8️⃣ *Contact*")
        users.insert_one({"number": number, "status": "main" })
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            response.message("Please enter valid response")
            response.message(
                "Hi, Thanks for contacting *Deepanshu.* again \nWhat do you want to know about him""\n\n*Please choose one of the option below based on your interest:*\n1️⃣ *Family* \n2️⃣ *Hobbies* \n3️⃣ *Address* \n4️⃣ *Education* \n5️⃣ *Achievements* \n6️⃣ *Goals* \n7️⃣ *Some Favourites* \n8️⃣ *Contact*")
            return str(response)
        if option == 1:
            response.message("Father : Mukesh Kumar\n He is a businessman and runs a Cafe in Mundhal Khurd,Bhiwani(127041)")
            response.message(
                "Mother : Geeta Rani\n She is a professional chef, a home economist and a Govt. employee of Haryana Police")
            response.message(
                "Younger brother : Himanshu Rajput\n Currently pursuing BCA from Govt. College Meham,Haryana")
        elif option == 2:
            response.message("You are entered in *Hobbies*")
            response.message(
                "Thrumming Guitar but a bathroom singer 🎸\nBadminton Playing 🏸\nTripping with friends 😉\nLoves to spend quality time with family 💕\nAnd many more 😜")
        elif option == 8:
            response.message("You can contact me through phone or email. \n\n*Phone* 📱: +919728462376 \n*E-mail* 📧: b420021@iiit-bh.ac.in ")
        elif option == 6:
            response.message("You are  entered in *Goals*")
            response.message("Want to be *Software Engineer* and work for nation ")
        elif option == 7:
            response.message("Your are entered in Favourites")
            users.update_one({"number": number}, {"$set": {"status": "favourite"}})
            response.message("Select the one: \n1️⃣Favourite Game \n2️⃣Favourite Fruits \n3️⃣ Favourite Dish \n4️⃣ Favourite Fast Food \n0️⃣ *Back*")
        elif option == 4:
            response.message("You are entered in *Education*")
            users.update_one({"number": number}, {"$set": {"status": "ordering"}})
            response.message( "Please select one: \n\n 1️⃣ Matric \n 2️⃣ Intermediate \n 3️⃣ JEE preparation \n 4️⃣ Graduation \n 0️⃣ *Back*")
        elif option == 3:
            response.message("V.P.O Mundhal Khurd, Bhiwani(127041) Haryana")
        elif option == 5:
            response.message("*Unmarried*😆 \nStill *Single*😉 \nScored *10 cgpa* in Matric \nSecured *A+* in intermediate \nAchieved *96.86* %ile in JEE \n*Still counting on*😎✌" )
        else:
            response.message(
                "Thanks for contacting *Deepanshu.*  \nWhat do you want to know about him""\n\n*Please choose one of the *valid* option below based on your interest:*\n1️⃣ *Family* \n2️⃣ *Hobbies* \n3️⃣ *Address* \n4️⃣ *Education* \n5️⃣ *Achievements* \n6️⃣ *Goals* \n7️⃣ *Some Favourites* \n8️⃣ *Contact*")
    elif user["status"] == "ordering":
        try:
            option = int(text)
        except:
            response.message("Why are you kidding me 😜")
            response.message("I don't know what to say")
            users.update_one({"number": number}, {"$set": {"status": "ordering"}})
            response.message(
                "Please select one: \n\n 1️⃣ Matric \n 2️⃣ Intermediate \n 3️⃣ JEE preparation \n 4️⃣ Graduation \n 0️⃣ *Back*")
            return str(response)
        if option == 0:
            users.update_one({"number": number}, {"$set": {"status": "main"}})
            response.message("What do you want to know more about Deepanshu""\n\n*Please choose one of the option below based on your interest:*\n1️⃣ *Family* \n2️⃣ *Hobbies* \n3️⃣ *Address* \n4️⃣ *Education* \n5️⃣ *Achievements* \n6️⃣ *Goals* \n7️⃣ *Some Favourites* \n8️⃣ *Contact*")
        elif option == 1:
            response.message("Great Choice 😍💕")
            response.message("\nHe did 10th from *Navug Sr. Sec. School* from his Home Town")
        elif option == 2:
            response.message("Excellent Choice ❤😍💕💖")
            response.message("\nHe did Intermediate from *RPS Public School* from nearby city Hansi,(Hisar)")
        elif option == 3:
            response.message("Good Choice 😍💕💖")
            response.message("\nHe prepared for JEE from Kota(Rajasthan) at *Resonance Eduventures Ltd.*")
        elif option == 4:
            response.message("It's going on 😉💖")
            response.message("\nHe is currently pursuing graduation in IT at IIIT Bhubaneswar, Odisha.")
        else:
            response.message(
                "Please select *valid* one: \n\n 1️⃣ Matric \n 2️⃣ Intermediate \n 3️⃣ JEE preparation \n 4️⃣ Graduation \n 0️⃣ *Back*")

    elif user["status"] == "favourite":
        try:
            newoption = int(text)
        except:
            response.message("Please enter a valid response")
            response.message("I don't know what to say 😢")
            response.message(
                "Select the one: \n1️⃣Favourite Game \n2️⃣Favourite Fruits \n3️⃣ Favourite Dish \n4️⃣ Favourite Fast Food \n0️⃣ *Back*")
            return str(response)
        if newoption == 1:
            response.message("Favourite outdoor game : *Badminton*")
            response.message("Favourite indoor game : *Ludo*")
        elif newoption == 2:
            response.message("Favourite  fruits : *Mango, Pineapple and Grapes*")
        elif newoption == 3:
            response.message("Favourite  dish : *Maa k haath ka Churma, Chilli Paneer, Haandi ki Kadhi, Besan Chilla*")
        elif newoption == 4:
            response.message("Although not interested in Fried items,\n still")
            response.message("Favourite  Fast food : Aalo tikki *Burger* with cheese and somewhat *Finger Chips*")
        elif newoption == 0:
            users.update_one({"number": number}, {"$set": {"status": "main"}})
            response.message(
                "What do you want to know more about Deepanshu""\n\n*Please choose one of the option below based on your interest:*\n1️⃣ *Family* \n2️⃣ *Hobbies* \n3️⃣ *Address* \n4️⃣ *Education* \n5️⃣ *Achievements* \n6️⃣ *Goals* \n7️⃣ *Some Favourites* \n8️⃣ *Contact*")
        else:
            response.message(
                "Are you kidding me 😥, please select the *valid* one: \n1️⃣Favourite Game \n2️⃣Favourite Fruits \n3️⃣ Favourite Dish \n4️⃣ Favourite Fast Food \n0️⃣ *Back*")

    return str(response)

if __name__ == "__main__":

    app.run()
