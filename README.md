<h1 align=center>Backend Developer: Technical Assessment</h1>

<div align=center>
<a href="#description">Description</a> |
<a href="#tech">Tech Stack</a> |
<a href="#clone">Clone Project</a> |
<a href="#launch">Execution</a> 
</div>


<div id="description"></div>

## Description


This project provides a way to calculate the coordinates of a given address, find a neighborhood and find a nearby neighborhood using a Google Map Client.


<div id="tech"></div>

## Tech Stack

**Language:** Python
**Geocoding API:** Google Maps

<div id="requirements"></div>

## Requirements


 * Git
 * Python



<div id="clone"></div>

## Clone the project


To be able to execute the project the first thing to do is clone this repository 


<div id="launch"></div>

## Execution 


**Define API KEY**

First of all we need to create our `.env` file in the root of the project, this file need to have the following variable to connect to the ***Google Maps Client***.
```
API_KEY = <OUR_API_KEY>
```

**Create a virtual ENV**

To execute the project we need first to create a virtual environment in python, for this first need to install the following module.

```
pip install virtualenv
```

After that we need to create a virtual environment

```
py -m venv env
```

This will create a folder with our virtual env files, after that we need to activate our environment.

```
.\env\Scripts\activate
```

**Install dependencies**

We need to install the dependencies into our virtual env

```
pip install -r .\requirements.txt
```

**Execute the app**

After that the environment will be activated and we just need to execute the main script.

```
py .\src\main.py
```