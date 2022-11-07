Learning Goal: I'm working on a website development project and need an explanation and answer to help me learn.

https://rapidapi.com/collection/best-bitcoin-api

The topic would be crypto and you can design however just meet all requirements. you can chooce any api from the link provided



Preliminaries

A web application is an interactive computer program developed using web technologies (HTML, CSS, JS), which stores (Database, Files) and manipulates data (CRUD - create, read, update and delete). Webapps can be used by a team or single user to perform tasks over the internet.

The goal of this project is to apply the Usability Goals and Design Principles learned in class into the development of a web application using Streamlit. Your project needs to manipulate data requested through an API. The format of the documents received can be of any type, but I highly recommend JSON, XML, or CSV. Here is a list of possible APIs that might be of interest to you:

https://github.com/public-apis/public-apis

https://rapidapi.com/collection/list-of-free-apis

Choose APIs that collect data that is of interest to you so that the development of the Web Application becomes more pleasant.

Use this discussion page to enter the names of all group members.

Requirements

The web application needs to be developed using Python programming languages version 3 (3.9 or 3.10 recommended) and the open-source framework Streamlit. Your objective is to create a web application that manipulates data and displays information to the users in the form of:

At least 1 interactive table (https://docs.streamlit.io/library/api-reference/da... to an external site.)

At least 2 chart elements, such as line, area or bar charts (matplotlib is allowed). To display:

a line chart - https://docs.streamlit.io/library/api-reference/ch... to an external site.

an area chart - https://docs.streamlit.io/library/api-reference/ch... to an external site.

a bar chart - https://docs.streamlit.io/library/api-reference/ch... to an external site.

At least 1 map with points marked on it (a simple map can be created using https://docs.streamlit.io/library/api-reference/ch... to an external site. or a more complex 3d map at https://docs.streamlit.io/library/api-reference/ch... to an external site.)

At least 1 button widget (https://docs.streamlit.io/library/api-reference/widgets/st.button)

At least 1 checkbox widget (https://docs.streamlit.io/library/api-reference/widgets/st.checkbox)

At least 2 of the essential feedback and messages boxes to the users:

Success box - https://docs.streamlit.io/library/api-reference/st... to an external site.

Information box - https://docs.streamlit.io/library/api-reference/st... to an external site.

Warning box - https://docs.streamlit.io/library/api-reference/st... to an external site.

Error box - https://docs.streamlit.io/library/api-reference/st... to an external site.

Exception message (optional) - https://docs.streamlit.io/library/api-reference/st... to an external site.

At least any 5 different widgets chosen from the following:

Radio button - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Selectbox - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Multiselect - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Slider - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Select-slider - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Text input - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Number input - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Text-area - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Date input - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Time input - https://docs.streamlit.io/library/api-reference/wi... to an external site.

File uploader - https://docs.streamlit.io/library/api-reference/wi... to an external site.

Color - https://docs.streamlit.io/library/api-reference/wi... to an external site.

You may include a progress bar for certain components of your application; however, this is not mandatory

You may include media elements such as image, audio or video, which are not a requirement but can add to the overall harmony of the web application being developed

The biggest HCI challenges will be the selection of appropriate layouts and containers. For example, you will need to study your target audience and the data being manipulated to decide, for example, whether to have 3 columns or 1 single column, or even whether an input data should be entered as a radio button or a text field, or whether to display a certain data output as a line chart or a map. Ask yourselves throughout the development process some of these questions:

What do the users expect to find or do on this web app?

What are my users trying to accomplish?

Is this web app’s primary aim to inform, to sell, or to amuse?

What competitor apps, if any, exist, and how should this app be inspired by/different than, those competitors?

What kind of experiences do my users find appealing and rewarding?

How can my product’s functions be most effectively organized? List Usability Goals and Design Principles utilized in the interface design.

How will my product introduce itself to first-time users?

How can my product put an understandable, appealing, and controllable face on technology?

How can my product deal with problems that users encounter?

How will my product help infrequent and inexperienced users understand how to accomplish their goals?

How can my product provide sufficient depth and power for expert users?

Streamlit allows you to display a sidebar, insert containers laid out as side-by-side columns, insert a multi-element container that can be expanded/collapsed, among many other features:

Sidebar - https://docs.streamlit.io/library/api-reference/la... to an external site.

Columns - https://docs.streamlit.io/library/api-reference/la... to an external site.

Expander - https://docs.streamlit.io/library/api-reference/la... to an external site.

Initial Steps

Choose a topic of interest to you (examples: sports, geology, music, cryptocurrency, farming, etc.)

Search for free and public datasets or free public APIs where you can request data to be manipulated and visualized in your web application

Start developing your web application:

Download and install Python programming language version 3

Download and Install PyCharm IDE Professional version by applying for a student license using your FIU email

Create a new Python project in PyCharm IDE and:

Install the necessary packages: pip install streamlit numpy pandas

Import the above packages:

import streamlit as st

import pandas as pd

import numpy as np

Include the components listed in REQUIREMENTS according to the goal of your web application and to the type of data being manipulated.

Distribute text elements in the form of title, header, subheader, caption or pre-formatted text across the web application so that the content of your web app engages readers and drives them to taken the necessary actions to fulfill your apps’s goals. Avoid dull, lifeless, and overlong prose. Try keeping text short and intriguing. This will encourage users to click through to other elements. Group content into cohesive categories by breaking it up into short paragraphs enriched with visual elements. This can help you make your web app have a light and engaging feel.

You are ready to submit it!

Don’t worry. I know this was so much fun. But this is not the end of this project. You will need it for our final and, arguably the most important branch of HCI, project, the Usability Test Project.

RUBRIC
This is how you will receive a score for your project submission:

Criteria

Exemplary (10)

Proficient (😎

Adequate (6)

Insufficient (4)

Identification of target users

Users clearly identified and web app clearly caters for them

Users partially identified, but web app caters for this group

Users identified but web application does not necessarily cater for them

No users identified or mentioned in the project submission

Goal Identification

The web app's purpose is readily apparent to the user.

The web app has a firm purpose, but may occasionally digress from the purpose

The purpose is not always clear

The purpose is generally unclear

Link between the goal Identification and the target audience

The problem poses a novel perspective or a major opportunity for innovation

Web app provides firm support for the goal identification and displays evidence of a basic analysis of a sufficiently limited topic. User gains some insights

The problem is somewhat clear but solution feels like a hammer trying to find a nail

The problem is unclear, unimportant or not well-motivated.

Dataset properly identified

Dataset clearly identified and used either through pre-selected XML, CSV or JSON files or through API requests

Dataset is identified and used either through pre-selected XML, CSV or JSON files or through API requests, but insufficient for the goal of the application

Dataset not properly used for the web app’s goal

No dataset identified

Dataset properly manipulated

Data was correctly manipulated from the requested documents using the API

Data was correctly manipulated from the requested documents using the API; however, it did not match with the goal identified for this web app

The data was not properly managed from the JSON, CSV, or XML files.

No dataset identified

Execution

The web app is ready to be deployed and used

All relevant aspects of the project have been completed, but they have minor flaws

The basic elements of the research are complete, but either they are flawed or important aspects are still missing

The project has some complete components, but critical aspects are incomplete

Organization

The ideas are arranged logically to support the web app’s goal. They flow smoothly from one to another and are clearly linked to each other. User can follow line of reasoning.

The ideas are arranged logically to support the web app’s goal. They are usually clearly linked to each other. For the most part, user can follow line of reasoning.

The elements of the web app are not arranged logically. Frequently, ideas fail to make sense together. User can figure out what the developer probably intends but may not be motivated to do so.

The elements of the web application lacks any semblance of logical organization. The user cannot identify a line of reasoning and loses interest.

Streamlit properly used

All elements of Streamlit listed in the requirements were used

Not all elements of Streamlit listed in the requirements were used

Just some elements of Streamlit listed in the requirements were used

Just a few elements of Streamlit listed in the requirements were used

Submission

On time

1 day late

2 days late

4 days late

Presentation

Web application was presented well with HCI elements clearly identified and correctly used

Web application was presented well, but HCI elements were not clearly identified or correctly used

Presentation lacked organization, identification of HCI elements, and did not meet the requirements

No presentation of the web application

Requirements: Complete   |   .doc file | Python
