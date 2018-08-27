cookbook

This is an online recepie book where anyone can access and add recepies to. The user needs to describe their recepies and provide an image for it. 
Then after submitting their recepie, users can like or edit this recepie. As a catalogue the user can also sort the recepies by like, view a specific
type of recepie or view only recepies based on their dietery needs.


UX

The front design is more extensive than the previous projects. We have used a library as recommended in the module, materialize css. This libray has provided us with many
css and js components. Some icons are also driven from a related icon library. The design is very responsive and steamlined with most other UI 
(most resembling google/android user interface). It is intuitive and easy to use as a result.


Features

The main page displays the list of recepies in no particular order. Each shown as a row which the user can expand to view with more details.
The first seen details from the recpie is its name and the number of its like. Then by expanding the user can view a picture of the recepie,
ingredients, instructions, category in which the dish belongs and the dietary class of it. The user also has access to edit and like buttons
after expanding the element. Upon selecting click the page refreshes with the like count of the element incremented by 1. Upon selecting edit
the user is redirected to an edit page. In the menu there is also an add page that redirects the user to the add page which is very similar to
this edit page.
The navbar is a horizontal and classic navigation bar which contains a home button and browse by category buttons. The latter redirect the user to
according pages which only display recepies within that category/diet. The navbar however transforms to a sidebar in mobile view. It is triggered
by clicking a menu button that looks very intuitively to the user.
The add and the edit page use a form driven from materialize css. This form is responsive, neat and easy to use. All fields are required and 
the img source field is validated. There are two fields represented by select dropdowns (diets and categories). After submission if another
recepie with the same name exits we will be redirected to an error message (same as if there exists no diet/category found upon clicking
view category buttons in menu).


Deployment

The website is deployed in Heroku.
Credits
I received css and js from https://materializecss.com/
and icons from https://material.io/
​