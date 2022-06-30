# AKSE: Cloud Computing SoSe 2022
## mealtracker - Hallo-Mahlzeit.de
### Mia Depta (200792), SEB 9
https://git.it.hs-heilbronn.de/it/courses/seb/cc1/ss22/mealtracker

## Chapter 1: Introduction
### What is your application doing?
The mealtracker provides a simple interface to see what meals you have eaten.

### What is the functionality?
The current mealtracker exists in a simple form. Students can submit and see orders. Due to timeconstraints the frontend has basic features.

![](https://hack.depta.dev/uploads/upload_f60575c49d7bd53f1bb5fe634b8cad46.png)
Basic Userinterface

![](https://hack.depta.dev/uploads/upload_ef00c22909071d0ce38805bdd2800367.png)
Basic API Interface

## Chapter 2: Architecture
### How did you setup the architecture and why?


### What services are you using and for why?
The backend code runs on Azure Functions. They are serverless and provide easy setup as well as maintenance. Their pricing is very good since you pay per Requests.

The database is Azure Cosmos DB. It provides the flexibility of having sql or nosql models and was fairly easy to set up.

The frontend is hosted on Azure static web app. It uses knockout.js, which is a simple and lightweight static library to make simple use interfaces.

### How does your application scale?
Azure Functions and CosmosDB scale automatically by demand. Especially the functions are scaled by requests load and can spin up very fast

### What does your data model look like?

| Actor                 | Subject                     | Location              |
| --------------------- | --------------------------- | --------------------- |
| Customer (Student)    | Order (Mahlzeit)            | Canteen (Mensa)       |
| - ID (Matrikelnummer) | - ID (Essensid per Student) | - ID (Mensa Standort) |
| - Name                | - Beschreibung              |                       |
|                       | - Preis                     |                       |
|                       | - Gewicht                   |                       |
|                       | - Timestamp                 |                       |


### What APIs does your app expose?
A simple REST Api is exposed. It is documented in the openapi.yml file inside the docs folder. Due to timeconstraints the api was drastically reduced in the V2

### How does the communication between all components work?
The Functions are the heart of the application. They have a connection endpoint to the CosmosDB and talk directly with the databases.
On the other side the Functions expose the REST Api and the frontend implements the Api

## Chapter 3: Tooling
### How does a developer work on your application?
The code is developed on github due to azure and github being a product of microsoft. Azure functions require VSCode Plugins to be able to run locally. Changes to the frontend in the repo are recognized by the static web app and automatically build.

### What does the docker stack look like?
The app does not use docker

### How are code changes deployed?
Code changes for the frontend are directly deployed when pushed to the main branch. Code for the functions have to be manually be deployed

### How is your infrastructure automated?
Apart from the automated frontend build the infrastructure isn't updated automatically

## Chapter 4: Lessons learned
### What have you learned?
Don't split a project hard between people. My project was planned with a partner that sadly threw the towel 1 1/2 weeks before the assignment was due. No matter the cloud provider they all are very deep when it comes to customization and they all have way too many guides or tutorials be it first or third party

### What was easy? What was complicated?
Knockout.js was a tip from a friend of mine. For super simple static sites it is quite amazing. Dealing with the functions and how they interact was in the beginning a pain. Understanding, how to split up your api to different functions and how they handle the http methods for example too quite a lot of researching

### Have you been surprised by anything?
Considering how simple functions seemed to be, they were quite complex to get into. But they also offer quite good price to request when a larger system isn't needed.
